from django.db import models

class Track(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    image = models.ImageField(upload_to='tracks/images/')
    audio = models.FileField(upload_to='tracks/audio/')

    def __str__(self):
        return self.title