from django.db import models
CART_STATUS = (
    (1, "GIVEN"),
    (2, 'IN_PROGRESS'),
    (3, 'DELIVERED'),
)


class ProductsCategory(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    is_visible = models.BooleanField(default=False)

    def str(self):
        return self.name


class Products(models.Model):
    products_name = models.CharField(max_length=200)
    products_category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image')
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    is_visible = models.BooleanField(default=False)

    def str(self):
        return self.products_name


class Type(models.Model):
    name = models.CharField(max_length=256)
    type = models.FloatField()

    def str(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    # description = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='image', null=False, blank=False)
    created = models.DateField(auto_now_add=True, blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def str(self):
        return self.name


class User(models.Model):
    telegram_id = models.CharField(max_length=200)
    location = models.CharField(max_length=256, null=False, blank=False)
    user_name = models.CharField(max_length=256)

    def str(self):
        return f'{self.id}. {self.user_name}  {self.telegram_id}'


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.IntegerField(choices=CART_STATUS, default=1)
    location = models.FloatField()
    telegram_id = models.FloatField()

    def str(self):
        return f'{self.cart_id}.{self.location} {self.status}'
