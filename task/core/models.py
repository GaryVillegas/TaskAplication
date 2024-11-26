from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, help_text="Enter a task title", null= True, blank=True)
    time_task = models.DateField(help_text="how long it will take you to finish")
    create_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, help_text="Enter your task here", null=True, blank=True)

    def __Str__(self):
        return self.title