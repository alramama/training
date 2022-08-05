from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Film(models.Model):
    bid_description  = models.CharField(blank = True, max_length =255 )
    End_user = models.CharField(blank = True, max_length =255 )
    activity_type = models.CharField(blank = True, max_length =255 )
    reference_no = models.CharField(blank = True, max_length =50 )
    last_date_of_clarifications = models.DateField()
    bid_file = models.FileField(upload_to='media',blank = True)
    

