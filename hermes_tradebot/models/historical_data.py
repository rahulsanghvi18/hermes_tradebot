from django.db import models


class HistoricalData(models.Model):
    trading_symbol = models.CharField(max_length=100, db_index=True)
    date_time = models.DateTimeField(max_length=100, db_index=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
