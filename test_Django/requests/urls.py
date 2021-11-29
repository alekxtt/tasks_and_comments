from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'requests'

urlpatterns = [
    path('', views.create_requestapp, name='index'),
    path('create_requestapp/',
         views.create_requestapp,
         name='create_requestapp'),
    path('create_request_message/<int:request_id>/',
         views.create_request_message,
         name='create_request_message'),
    path('find_request_id/<int:request_id>/',
         views.find_request_id,
         name='find_request_id'),
    path('find_request_id_sub/',
         views.find_request_id_sub,
         name='find_request_id_sub'),
    path('find_messages_request_id/<int:request_id>/',
         views.find_messages_request_id,
         name='find_messages_request_id'),
    path('list_of_requests/',
         views.list_of_requests,
         name='list_of_requests'),
    path(
        'login/',
        LoginView.as_view(template_name='requests/login.html'),
        name='login'
    ),
    ]
