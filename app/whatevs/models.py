from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Forum(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Thread(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    body = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.forum.title + " - " + self.title
