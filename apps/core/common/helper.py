import datetime as dt


def to_date_obj(_date):
    if type(_date) == str:
        return dt.datetime.strptime(_date, "%Y-%m-%d").date()
    else:
        return _date


def daterange(start_date, end_date):
    start_date = to_date_obj(start_date)
    end_date = to_date_obj(end_date)
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + dt.timedelta(n)
