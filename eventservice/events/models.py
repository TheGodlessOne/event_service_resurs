from django.db import models

# Create your models here.
class Event(models.Model): 
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=30)
    event_description = models.TextField(max_length=280)
    event_date = models.DateTimeField()
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)