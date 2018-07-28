from django.db import models
from adaptor.model import CsvModel
# Create your models here.


class Bubble(models.Model):
    date=models.CharField(max_length=100)
    coin=models.CharField(max_length=50)
    open=models.FloatField()
    market_cap=models.FloatField()
    volume=models.FloatField()

    def __str__(self):
        return "date:"+self.date+","+"coin:"+self.coin+","+"open:"+str(self.open)+","+"market_cap:"+str(self.market_cap)
