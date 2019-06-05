from django.db import models


class Img(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/')
