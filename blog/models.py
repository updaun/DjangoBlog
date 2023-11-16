from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.id})"