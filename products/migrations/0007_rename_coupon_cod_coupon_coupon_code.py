# Generated by Django 4.2.3 on 2023-10-09 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='coupon_cod',
            new_name='coupon_code',
        ),
    ]