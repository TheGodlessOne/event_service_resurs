from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from events.models import Event
from events.serializers import EventSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer