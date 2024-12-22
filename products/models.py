from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/')
    product_category = models.CharField(max_length=100)


    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])