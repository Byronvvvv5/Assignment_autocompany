# Generated by Django 4.1.4 on 2023-03-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]