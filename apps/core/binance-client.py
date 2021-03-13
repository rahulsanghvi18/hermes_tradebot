from apps.core.common import django_settings
from binance.client import Client
import datetime as dt
import pandas as pd
import pytz
from apps.core.common.helper import daterange, to_date_obj
from hermes_tradebot.models import HistoricalData, DataStats
from django.db import transaction
import tqdm
from decouple import config


class BinanceClient:
    api_key: str = None
    api_secret: str = None
    client: Client = None

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(self.api_key, self.api_secret)
        self.ticker_df = pd.DataFrame(self.client.get_all_tickers())
        self.ticker_df = self.ticker_df[
            self.ticker_df["symbol"].str.contains("USDT") | self.ticker_df["symbol"].str.contains("BUSD")]

    def get_historical_data(self, symbol: str, interval: str, start_time: dt.datetime, end_time: dt.datetime):
        start_time = start_time.replace(tzinfo=pytz.UTC)
        end_time = end_time.replace(tzinfo=pytz.UTC)
        start_time = start_time.isoformat()
        end_time = end_time.isoformat()
        col = ["openTime", "open", "high", "low", "close", "volume", "closeTime", "quoteAssetVolume", "numberOfTrades",
               "takerBuyBaseAssetVolume", "takerBuyQuoteAssetVolume", "ignore"]
        df = pd.DataFrame(self.client.get_historical_klines(symbol, interval, start_time, end_time), columns=col)
        df["trading_symbol"] = symbol
        df = df[["trading_symbol", "openTime", "open", "high", "low", "close", "volume"]]
        df.rename(columns={"openTime": "date_time"}, inplace=True)
        df["date_time"] = pd.to_datetime(df["date_time"], unit="ms", utc=True)
        return df

    @transaction.atomic
    def save_to_db(self, df: pd.DataFrame, last_date):
        if df.empty:
            return

        li = []
        for x in df.to_dict('records'):
            li.append(HistoricalData(**x))
        HistoricalData.objects.bulk_create(li, batch_size=200)
        self.hist_obj.stats["last_update"] = str(last_date)
        self.hist_obj.save()

    def store_all_securities(self, start_date: dt.date, end_date: dt.date):
        for symbol in tqdm.tqdm(self.ticker_df["symbol"]):
            self.hist_obj, created = DataStats.objects.get_or_create(trading_symbol=symbol)
            if not created:
                end_date = to_date_obj(self.hist_obj.stats["last_update"]) + dt.timedelta(days=1)
                self.hist_obj.stats = {}
            if end_date >= dt.datetime.now(tz=pytz.UTC).date() or start_date >= end_date:
                continue

            for x in daterange(start_date=start_date, end_date=end_date):
                start_time = dt.datetime(day=x.day, month=x.month, year=x.year, hour=0, minute=0, second=0)
                end_time = dt.datetime(day=x.day, month=x.month, year=x.year, hour=23, minute=59, second=0)
                ans_df = self.get_historical_data(symbol, Client.KLINE_INTERVAL_1MINUTE, start_time, end_time)
                print(x)
                self.save_to_db(df=ans_df, last_date=x)


obj = BinanceClient(api_key=config("API_KEY"), api_secret=config("API_SECRET"))
obj.store_all_securities(start_date=dt.date(2017, 8, 15), end_date=dt.date(2021, 3, 11))
