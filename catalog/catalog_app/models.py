from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.description}'


class Product(models.Model):
    sku = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    height = models.DecimalField(max_digits=9, decimal_places=2)
    width = models.DecimalField(max_digits=9, decimal_places=2)
    length = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f'{self.sku}, {self.name}, {self.description},{self.price},\
                 {self.height}, {self.width}, {self.length}, {self.weight}'


class Seller(models.Model):
    name = models.CharField(max_length=150)
    active = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.name}, {self.active}'


class CatalogAnalysis(models.Model):
    #fk_product = models.IntegerField(null=False)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    #fk_seller = models.IntegerField(null=False)
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    #fk_category = models.IntegerField(null=False)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    approved = models.BooleanField(null=False)

    def __str__(self):
        return f'{self.fk_product}, {self.dk_seller}, {self.fk_category},\
                 {self.approved}'
