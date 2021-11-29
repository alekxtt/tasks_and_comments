from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('requests/', include('requests.urls', namespace='requests')),
    path('admin/', admin.site.urls),
    path('', include('requests.urls', namespace='index')),
    path('', include('api.urls', namespace='api')),
]
