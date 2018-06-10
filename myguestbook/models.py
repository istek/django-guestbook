from django.db import models
from django.urls import reverse


# Create your models here.


class Guestbook(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    weburl = models.URLField()
    avatar = models.CharField(
        max_length=200, default='https://avatar.csdn.net/3/9/5/3_lenny_lin.jpg')
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('myguestbook:index')

    def __str__(self):
        return self.name
