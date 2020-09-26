from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    created_time = models.DateTimeField(editable=False)
    to_be_completed = models.DateTimeField(blank=True, null=True)
    completed_time = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_time = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
