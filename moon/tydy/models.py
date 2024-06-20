from django.db import models

# Create your models here.

class TaskModel(models.Model):
    sagolovok = models.CharField(max_length=60)
    text = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)
