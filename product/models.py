from django.db import models


class product(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class productDetail(models.Model):

    product_id = models.ForeignKey(product, null=False, on_delete=models.CASCADE)
    product_detail = models.CharField(max_length=255)

    def __str__(self):
        return self.product_detail