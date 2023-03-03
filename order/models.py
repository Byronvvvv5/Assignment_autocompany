from django.db import models
from product.models import product
from datetime import date
from django.utils.datetime_safe import datetime


class client(models.Model):

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class order(models.Model):

    client_id = models.ForeignKey(client, null=False, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255, default='created')
    delivery_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    update_date = models.DateTimeField(null=True, auto_now=True)


class orderItem(models.Model):

    order_id = models.ForeignKey(order, null=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, null=False, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(null=True, auto_now_add=True)

