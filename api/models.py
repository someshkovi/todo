from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_time = models.DateTimeField(auto_now=True)
    to_be_completed = models.DateTimeField(blank=True, null=True)
    completed_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
