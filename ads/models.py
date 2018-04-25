from django.db import models

class Ad(models.Model):
    advertiser = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ad end')
    play_count = models.IntegerField(default=0)

    def __str__(self):
        "Set to display advertiser name in the ads table"

        return self.advertiser


class Device(models.Model):
    pass
