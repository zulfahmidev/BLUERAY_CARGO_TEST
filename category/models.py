from django.db import models
from country.models import Country

class Category(models.Model):
    id               = models.AutoField(primary_key=True)
    country          = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countries')
    category_title   = models.CharField(max_length=50)
    price_per_kilo   = models.IntegerField()

    class Meta:
        db_table = 'categories'