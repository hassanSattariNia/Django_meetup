from django.db import models
# Create your models here.
# Django create one table per model automatically in database

class Meetup(models.Model): 
    title = models.CharField(max_length=200)
    #models.slug built with django to provide text have slug format
    slug = models.SlugField(unique=True)
    description=models.TextField()