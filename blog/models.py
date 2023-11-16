from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.id})"

    class Meta:
        db_table = 'blog'