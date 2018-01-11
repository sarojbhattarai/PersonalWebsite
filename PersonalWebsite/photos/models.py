from django.db import models

# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(upload_to = 'my_photos')
    alt = models.CharField(max_length=30)
    description = models.TextField()
    published_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.alt

