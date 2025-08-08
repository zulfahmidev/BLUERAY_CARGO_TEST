from django.db import models
from django.core.validators import FileExtensionValidator
import hashlib
import os
from datetime import datetime

def hashed_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    name_hash = hashlib.sha256((filename + str(datetime.now())).encode()).hexdigest()
    hashed_name = f"{name_hash}.{ext}"
    return os.path.join('country_flags/', hashed_name)

class Country(models.Model):
    id               = models.AutoField(primary_key=True)
    country_name     = models.CharField(max_length=50)
    country_flag     = models.FileField(null=False, blank=False, upload_to=hashed_upload_to, validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    country_currency = models.CharField(max_length=3)

    class Meta:
        db_table = 'countries'