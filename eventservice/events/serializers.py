from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Event
        fields = ['id', 'event_title', 'event_description', 'event_date', 'owner']


class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'events']
