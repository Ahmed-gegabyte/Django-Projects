from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=225)
    desc = models.TextField()
    time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return 'Tasks: ' + self.task