from django.db import models

class Ad(models.Model):
    advertiser = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ad end')
    play_count = models.IntegerField()

# Create your models here.
