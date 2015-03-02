from django.db import models


class License(models.Model):
    title = models.CharField(max_length=500)
    date_applied = models.DateTimeField('date applied')
    date_granted = models.DateTimeField('date applied')
    date_expires = models.DateTimeField('date applied')
