from django.db import models

class instagal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')