from django.db import models

# Create your models here.

class SubscribersEmail(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = "Subscriber's Email"
        verbose_name_plural = "Subscriber's Emails"

    def __str__(self):
        return self.email
