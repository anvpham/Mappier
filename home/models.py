from django.db import models

# Create your models here.


class Category(models.Model):
    text = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.text}"


class Place(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.text}"
