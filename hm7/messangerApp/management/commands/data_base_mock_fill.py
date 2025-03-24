from mixer.backend.django import mixer
from django.core.management.base import BaseCommand
from messangerApp.models import User, Post, Comment, MarkPost, MarkComment

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_amt = 10
        post_amt = 30
        comment_amt = 100
        mark_post_amt = 150
        mark_comment_amt = 50

        mixer.cycle(user_amt).blend(User)
        mixer.cycle(post_amt).blend(Post)
        mixer.cycle(comment_amt).blend(Comment)
        mixer.cycle(mark_post_amt).blend(MarkPost)
        mixer.cycle(mark_comment_amt).blend(MarkComment)


    # не очень красивый способ отката, но, с другой стороны
    # в базе с тестовыми данными должны лежать только они
    # Dangerous to use !!!
    def unhandle(self, *args, **kwargs):
        print("\n\nDANGEROUS TO RUN - RM ALL DATA\n\n")

        User.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()
        MarkPost.objects.all().delete()
        MarkComment.objects.all().delete()
