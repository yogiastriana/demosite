from django.db import models


class Ticker(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10, unique=True)  # Symbol is unique for each ticker
    shortname = models.CharField(max_length=255)
    longname = models.CharField(max_length=255)
    sector = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    marketcap = models.BigIntegerField()
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    longbusinesssummary = models.TextField()

    class Meta:
        db_table = 'tickers'  # Specifies the database table name
        verbose_name = "Ticker"
        verbose_name_plural = "Tickers"

    def __str__(self):
        return f"{self.symbol} - {self.shortname}"
