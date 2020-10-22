from django.db import models
from django.utils import timezone


class Comment(models.Model):

    name = models.CharField(max_length=20)
    comment = models.TextField(max_length=200)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)

# Create your models here.
