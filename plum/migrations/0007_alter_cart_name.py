# Generated by Django 4.0.4 on 2022-07-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plum', '0006_cart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]