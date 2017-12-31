from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_on = models.DateTimeField(auto_now_add = True)
    featured_image = models.ImageField(upload_to = 'featued_image')
    slug = models.SlugField(unique=True)
    tags = TaggableManager()
    time_read = models.IntegerField()
    body = models.TextField()
    category = models.ForeignKey('Category', on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

