from django.db import models

# Create your models here.

MOOD_CHOICE = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('normal', 'Normal'),
    )

class Event(models.Model):
    date = models.DateField()
    headline = models.CharField(max_length=50)
    mood = models.CharField(max_length=6, choices=MOOD_CHOICE)
    description = models.TextField()
    image = models.ImageField(upload_to='My_Life', blank=True, null=True)

    def __str__(self):
        return "{}_{}".format(self.date, self.headline)



