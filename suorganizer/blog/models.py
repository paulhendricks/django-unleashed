from django.db import models

from organizer.models import Startup, Tag

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63, help_text='A label for the URL config.')
    text = models.TextField()
    pub_date = models.DateField('date published', auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog posts')
    startups = models.ManyToManyField(Startup, related_name='blog posts')
