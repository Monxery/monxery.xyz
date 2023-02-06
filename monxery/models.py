from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
