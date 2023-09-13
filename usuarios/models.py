from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField('E-mail',unique=True)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username
