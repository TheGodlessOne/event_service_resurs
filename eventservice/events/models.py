from django.db import models


class Event(models.Model): 
    event_title = models.CharField(max_length=30)
    event_description = models.TextField(max_length=280, blank=True, default='')
    event_date = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE, default=None)
