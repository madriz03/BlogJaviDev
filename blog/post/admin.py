from django.contrib import admin
from .models import  Post, Comment
from .forms import BlogAdminForm
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)
