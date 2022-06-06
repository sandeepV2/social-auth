from django.db import models

# Create your models here.

class Post(models.Model):
 title = models.CharField(max_length=100)
 contest = models.TextField(blank=True, null=True)
 data = models.DateField(auto_now=True)