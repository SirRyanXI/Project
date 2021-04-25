from django.contrib import admin
from .models import Forum, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ForumAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(Forum, ForumAdmin)
admin.site.register(Comment)