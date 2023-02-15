from django.db import models


class category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=250, blank=True)
    cat_image = models.ImageField(upload='photos/categories/', blank=True)

    def __str__(self):
        return self.category_name
