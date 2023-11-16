from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)    # 제목
    content = models.TextField(null=True,blank=True)    # 내용
    view = models.PositiveBigIntegerField(default=0)    # 조회 수
    created_at = models.DateTimeField(auto_now_add=True)    # 처음 생성될 때만 
    updated_at = models.DateTimeField(auto_now=True)    # 수정될 때마다 

    # __str__는 객체를 Print 했을 때 어떻게 보여지는지 정하는 함수 - migrations로는 인식하지 못한다.
    def __str__(self):

        return f"{self.title} ({self.id})"