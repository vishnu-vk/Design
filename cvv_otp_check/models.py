from django.db import models
from django.conf import settings
import os
# Create your models here.
base_dir=settings.BASE_DIR

class User(models.Model):
    Id=models.SmallIntegerField(null=False,primary_key=True)
    number=models.BigIntegerField(null=False)
    name=models.CharField(max_length=50,null=False)
    cvc=models.SmallIntegerField(null=False)
    mm=models.SmallIntegerField(null=False)
    yyyy=models.SmallIntegerField(null=False)
    Phone=models.BigIntegerField(null=False)
    otp=models.SmallIntegerField(null=False)

    def __int__(self):
        return self.Id
