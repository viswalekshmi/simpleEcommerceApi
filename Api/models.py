from django.db import models

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=200, unique=True)

    description =models.TextField(max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.name
    
class Size(models.Model):

    name = models.CharField(max_length=100, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.name
    
class Brand(models.Model):

    name = models.CharField(max_length=100, unique=True)

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    
    def __str__(self):

        return self.name


class Product(models.Model):

    title=models.CharField(max_length=200)

    description=models.TextField(max_length=200)

    category_object=models.CharField(max_length=200)

    size_object=models.ManyToManyField(Size)
    
    brand_object = models.CharField(max_length=200)

    image = models.ImageField(upload_to='product_images', null=True, blank=True, default='product_images/default.jpg')

    price = models.PositiveIntegerField()


    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):

        return self.title
    
    