from django.db import models
from datetime import date
# Create your models here.

class UserFeedback (models.Model):
    fb_id = models.AutoField(primary_key=True)
    rating = models.CharField (verbose_name = 'Rating', db_column="rating", max_length=50, blank=False, null=False)
    hotel_id = models.CharField (verbose_name = 'Hotel_id', db_column="hotel_id", max_length=50, blank=False, null=True)
    comments = models.TextField(verbose_name='Comments', db_column="comments", max_length=50, blank=False,
                                  null=False)
    agency_id = models.CharField(verbose_name='Agency_id', db_column="agency_id", max_length=50, blank=False,
                                  null=True)
    email = models.EmailField(verbose_name='Email', db_column="email", max_length=50, blank=False,
                                  null=True)
    class Meta:
        db_table='user_feedback'