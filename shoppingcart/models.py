from django.db import models
from product.models import product
from order.models import client, order
from datetime import date
from django.utils.datetime_safe import datetime


class shoppingCart(models.Model):

    client_id = models.ForeignKey(client, null=False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    update_date = models.DateTimeField(null=True,auto_now=True)


class cartProducts(models.Model):

    cart_id = models.ForeignKey(shoppingCart, null=False, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, null=False, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


