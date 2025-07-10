from django.db import models
from user.models import CustomUser

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE, default = None)
    title = models.CharField(max_length = 100)
    text = models.CharField(max_length = 2000)
    published_date = models.DateField(default=None)
    edited_date = models.DateField(default=None, null=True, blank=True)
    post_image = models.ImageField(null = True, blank = True, upload_to = 'images/')