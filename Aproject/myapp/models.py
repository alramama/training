from django.db import models

# app/models.py

from django.db import models
from django.utils import timezone

class BookLibrary(models.Model):
    class Meta:
        db_table = 'book_library'

    publish_date = models.CharField(max_length = 50 )
    bid_description  = models.CharField(max_length = 255 )
    End_user = models.CharField(blank = True, max_length =255 )
    activity_type = models.CharField(blank = True, max_length =255 )
    reference_no = models.CharField(blank = True, max_length =50 )
    last_date_of_clarifications = models.FileField(upload_to='media',blank = True)
