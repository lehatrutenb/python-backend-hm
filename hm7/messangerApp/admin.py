from django.contrib import admin
from .models import User, Comment, Post, MarkComment, MarkPost
# Register your models here.

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(MarkComment)
admin.site.register(MarkPost)