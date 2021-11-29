from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import RequestMessage, Request


class RequestMessageForm(ModelForm):
    class Meta:
        model = RequestMessage
        fields = ('text',)


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        exclude = ['user', 'created']
