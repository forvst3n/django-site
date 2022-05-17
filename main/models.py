from django.db import models
import datetime


class GPU(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=400)
    memory = models.CharField(max_length=50)
    technical_process = models.IntegerField()
    date = models.DateTimeField(datetime.datetime.now(),auto_now_add=True)

    def __str__(self):
        return self.title
class Comment(models.Model):
    gpu = models.ForeignKey(GPU,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=350)
    date = models.DateTimeField(datetime.datetime.now(),auto_now_add=True)

    def __str__(self):
        return self.author