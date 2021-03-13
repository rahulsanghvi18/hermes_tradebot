from django.db import models


class DataStats(models.Model):
    trading_symbol = models.CharField(max_length=100, db_index=True)
    stats = models.JSONField(default=dict)
