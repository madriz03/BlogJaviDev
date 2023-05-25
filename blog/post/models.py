from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(max_length=3000, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}  -  {naturaltime(self.date)}'

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=250, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} - {naturaltime(self.date)}'