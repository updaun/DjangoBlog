from django.db import models
import random
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="blogs", null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.title} ({self.id})"

    class Meta:
        db_table = 'blog'

    def save(self, *args, **kwargs):
        # 최초 모델이 생성될 때, 만약 image의 값이 없다면 이미지를 더미 이미지로 넣어준다.
        if not self.id and not self.image:
            random_num = random.randint(1, 10000)
            self.image = f"https://picsum.photos/500?random={random_num}"
        super().save(*args, **kwargs)

        