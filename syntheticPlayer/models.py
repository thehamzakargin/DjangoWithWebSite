from django.db import models
from django.utils.text import slugify

    
class categories(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(default="", null=False, unique=True, db_index=True, max_length=40)

    def __str__(self):
        return f"{self.name}"


# Create your models here.
class syntheticPlayer(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",blank=True, null=False, unique=True, db_index=True)
    categories = models.ManyToManyField(categories)
    
    def __str__(self):
        return f"{self.title}"


