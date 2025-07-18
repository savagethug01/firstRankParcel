# Generated by Django 5.2.3 on 2025-06-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0004_remove_shippingdetail_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetail',
            name='carrier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='departure_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='expected_delivery_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='pick_up_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='pick_up_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='receiver_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='shipper_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='shippment_destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='shippment_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
