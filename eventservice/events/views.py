from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, filters
from events.models import Event
from events.serializers import EventSerializer, UserSerializer
from events.permissions import IsOwner


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    serializer_class = UserSerializer
