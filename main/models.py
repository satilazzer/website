from django.db import models


class Center(models.Model):
    name = models.CharField('name', max_length=100)
    address = models.CharField(max_length=100)
    whatsapp = models.TextField()
    instagram = models.TextField()
    map = models.TextField()
    break_day = models.CharField('break', max_length=100, default='break')

    def __str__(self):
        return self.name


class Cosmetic(models.Model):
    name = models.CharField('cosmetic', max_length=100)
    img = models.ImageField('img', upload_to='uploads/')
    price = models.IntegerField()
    description = models.TextField('desc')

    def __str__(self):
        return self.name
