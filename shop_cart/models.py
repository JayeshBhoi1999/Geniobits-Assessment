from django.db import models


# Create your models here.
class Product (models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=50,default="")    
    p_img_1 = models.ImageField(upload_to='static/images/',default="")
    product_price = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-date_added']

class Order (models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    grand_total = models.CharField(max_length=50)
    items_json = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']