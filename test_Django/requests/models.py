from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField
from django.http import request


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']


class RequestMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    requestapp = models.ForeignKey(Request,
                                   on_delete=models.CASCADE,
                                   related_name='requests',)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
