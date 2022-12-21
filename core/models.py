from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    rasm = models.CharField(max_length=255)
    context = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tanlov = models.CharField(max_length=60)

    def __str__(self):
        return self.name