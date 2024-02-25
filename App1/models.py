from django.db import models
from django.core.files.storage import FileSystemStorage


product_image_storage = FileSystemStorage(location='../media', base_url='/media')

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField()
    photo = models.ImageField(storage=product_image_storage, upload_to='product_photos/', blank=True, null=True)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()