from django.core.management import BaseCommand, CommandParser
import sys 
from blog.models import Blog

class Command(BaseCommand):

    # def add_arguments(self, parser: CommandParser) -> None:
        # return super().add_arguments(parser)
    
    def handle(self, *args,**options) -> str | None:
        
        print("Make Blog Command")

        for i in range(1,101):
            # 타이틀이 test blog i 인게 있으면 생성하지 않고
            # 없으면 생성하라는 get_or_create - 리턴은 튜플로 한다. 
            
            blog, created = Blog.objects.get_or_create(
                title = f"테스트 Blog {i}",
                # content = f"테스트 Blog {i} 내용입니다." 이렇게 해도 되지만,
            )
            # 공부를 위해서 비효율적이지만 사용해보자.
            blog.content = f"테스트 Blog {i} 내용입니다." # blog의 content 필드
            blog.view = i
            blog.save() # 이 save()를 해줘야 데이터베이스에 반영이 된다!(중요)

            
            # blog.save()   # 이렇게 주석처리로 안하면 반영이 안된다! 

            # 없는 아이디를 생성했으면 create 값 True, 있는 아이디면 False
            if created:
                print(f"{i} 번째 Blog가 생성되었습니다.")
            else:
                print(f"{i} 번째 Blog가 이미 있습니다.")

        # 초록색 색깔 표시
        sys.stdout.write(self.style.SUCCESS("Blog Command Success :) "))   
        # return super().handle(*args, **options)