from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=True)
    is_status=models.IntegerField(default=0,validators=[MaxValueValidator(1),MinValueValidator(0)])

