from django.db import models


class Product(models.Model):
    photo = models.ImageField(upload_to='media/product_photos/', blank=True)
