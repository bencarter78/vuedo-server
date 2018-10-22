from django.db import models
from django.contrib.auth.models import User


DEFAULT_USER_ID = 1

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    question = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    completed = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.name