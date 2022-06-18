from django.db import models
from django.conf import settings

class Post(models.Model):
	Title = models.CharField(max_length=200)
	Text = models.TextField()
	Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	Created_date = models.DateTimeField()
	Published_date = models.DateTimeField(auto_now=True)
# Create your models here.
