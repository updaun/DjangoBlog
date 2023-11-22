from django.core.management import BaseCommand
import sys
from blog.models import Blog

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Make Blog Command")

        for i in range(0 , 100):
            blog , created = Blog.objects.get_or_create(
                title = f"Test Blog {i}",
            )

            blog.content = f"Test Blog {i} Content"
            blog.save()

            if created:
                print(f"{i} Blog Created")
            else:
                print(f"{i} Blog Exists")

        sys.stdout.write(self.style.SUCCESS("Makge Blog Command Succdess :)"))