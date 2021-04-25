from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    sender = models.CharField(max_length=32)
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lat = models.FloatField(default=34.75)
    lng = models.FloatField(default=135.5)

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}, {}, {}'.format(self.image, self.sender, self.title, self.body, self.created_at, self.updated_at, self.lat, self.lng)