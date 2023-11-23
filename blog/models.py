from django.db import models
import random
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)    # 제목
    content = models.TextField(null=True,blank=True)    # 내용
    image = models.CharField(max_length=200,null=True,blank=True)
    view = models.PositiveBigIntegerField(default=0)    # 조회 수
    # CASCADE, PROTECT, SET_NULL 중 SET_NULL은 사용자가 없어져고 글은 작자미상으로 남아있게 된다.
    # blank=True라고 하면 admin페이지에서 효과가 있다.
    # related_name을 따로 안넣어주면 디폴트 값으로, set_blog 가 생기는데, 지금은 따로 blogs라고 넣어줬다.
    # 강사님은 보통 related_name을 모델이름을 따라간다. (blog를 여러개 작성할 수 있으므로 blogs로 표시)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='blogs', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)    # 처음 생성될 때만 
    updated_at = models.DateTimeField(auto_now=True)    # 수정될 때마다 

    # __str__는 객체를 Print 했을 때 어떻게 보여지는지 정하는 함수 - migrations로는 인식하지 못한다.
    def __str__(self):

        return f"{self.title} ({self.id})"
    
    def save(self,*agrs, **kwargs):
        # 최초 모델이 생성될 때, 만약 image 값이 없다면 이미지를 더미 이미지로 넣어준다.
        # save를 타야 id가 생기니까 없다면 최초라는 의미다.
        if not self.id and not self.image:
            random_num = random.randint(1,10000)
            self.image = f"https://picsum.photos/500?random={random_num}"
        super().save(* agrs,**kwargs)