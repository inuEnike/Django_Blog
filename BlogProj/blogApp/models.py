from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django_ckeditor_5.fields import CKEditor5Field
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    BlogCategory = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=75)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    content = CKEditor5Field('Text', config_name='extends')
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    timeRead = models.IntegerField(default=5)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']  ## Post yorumlarını yeniden eskiye sıralar

    def __str__(self):
        return self.author.username+' | '+ self.post.title
    



class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    Description = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.username