from django.core.management import BaseCommand
import sys
from blog.models import Blog


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Make Blog Command")

        for i in range(1, 101):
            # blog = Blog.objects.create{
            #     title=f"테스트 Blog{i}"
            # }

            blog, created = Blog.objects.get_or_create(
                title=f"테스트 Blog{i}"
                # content=f"테스트 Blog {i} 내용입니다."
            )

            blog.content = f"테스트 Blog {i} 내용입니다."
            blog.view = i
            blog.save() 

            if created:
                print(f"{i}번째 Blog가 생성되었습니다.")
            else:
                print(f"{i}번째 Blog가 이미 있습니다.")

        sys.stdout.write(self.style.SUCCESS("Blog Command Success :)"))