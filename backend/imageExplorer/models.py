from django.db import models
from django.core.validators import FileExtensionValidator

#  現状はprimaryNumberから連鎖的にリクエストを飛ばす

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    nice = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.image, self.created_at, self.updated_at, self.nice)


class Video(models.Model):
    video = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    nice = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.video,self.nice, self.created_at, self.updated_at)


class Main(models.Model):
    title = models.SlugField(default='No Title')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Card(models.Model):
    main = models.ForeignKey(Main, related_name='cards', on_delete=models.CASCADE)
    url = models.SlugField()
    thumbnail = models.OneToOneField(Image, on_delete=models.CASCADE)
    title = models.CharField(default='No Title', max_length=30)
    second_title = models.CharField(blank=True, max_length=60)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Page(models.Model):
    main = models.OneToOneField(Main, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # header = 
    # footer = 
    # sidebar = 


class Address(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=8)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Zoo(models.Model):
    name = models.CharField(max_length=50)
    official_url = models.SlugField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE)


class Animal(models.Model):
    zoo = models.ManyToManyField(Zoo)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

