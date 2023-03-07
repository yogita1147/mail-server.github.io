from django.db import models
class mail(models.Model):
    mailfrom=models.CharField(max_length=30)
    mailto = models.CharField(max_length=30)
    subject = models.CharField(max_length=40)
    contents = models.CharField(max_length=700)


# Create your models here.