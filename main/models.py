from django.db import models


class Center(models.Model):
    name = models.CharField('name', max_length=100)
    slider1 = models.ImageField(upload_to=f'uploads/slider/', default=None)
    slider2 = models.ImageField(upload_to=f'uploads/slider/', default=None)
    slider3 = models.ImageField(upload_to=f'uploads/slider/', default=None)
    slider4 = models.ImageField(upload_to=f'uploads/slider/', default=None)
    slider5 = models.ImageField(upload_to=f'uploads/slider/', default=None)
    slider6 = models.ImageField(upload_to=f'uploads/slider/', default=None)
    address = models.CharField(max_length=100)
    whatsapp = models.TextField()
    instagram = models.TextField()
    map = models.TextField()

    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField('name', max_length=100)
    specialized = models.CharField('specialized', max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    master_img = models.ImageField(upload_to=f'uploads/masters/', default=None)

    def __str__(self):
        return self.name
