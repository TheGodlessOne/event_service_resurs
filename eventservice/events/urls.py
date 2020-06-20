from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from events import views
from .routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('router.urls'))
]
