from django.db import models

class Converter(models.Model):
    fromAmount = models.FloatField()
    fromCurrency = models.CharField(max_length=3)
    toCurrency = models.CharField(max_length=3)

    def __str__(self):
        return self.fromAmount

