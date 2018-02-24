from django.db import models

# Create your models here.


class Work(models.Model):
    title = models.CharField(max_length=200)
    work_url = models.URLField()
    photo = models.ImageField(upload_to='works')
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


    def __str__(self):
        return self.title
