from django.db import models

class BID(models.Model):
    publish_date = models.CharField(max_length = 50 )
    bid_description  = models.EmailField(blank = True )
    End_user = models.CharField(blank = True, max_length =255 )
    activity_type = models.CharField(blank = True, max_length =255 )
    reference_no = models.CharField(blank = True, max_length =50 )
    last_date_of_clarifications = models.FileField(upload_to='media',blank = True)
