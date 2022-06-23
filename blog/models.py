from getpass import getuser
from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import CharField
import datetime

# Create your models here.


class get_user_model(models.Model):
    pass


class Post (models.Model):
    Title = models.CharField(max_length=250)
    Text = models.TextField()
    Author = models.ForeignKey(
        get_user_model, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
