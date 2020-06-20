from rest_framework import routers
from events.views import EventViewSet, UserViewSet


router = DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', views.UserViewSet)