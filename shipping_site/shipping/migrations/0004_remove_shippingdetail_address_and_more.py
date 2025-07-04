# Generated by Django 5.2.3 on 2025-06-22 16:00

import shipping.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_remove_shippingdetail_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingdetail',
            name='address',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='current_location',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='description',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='parcel_image',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='shippingdetail',
            name='tracking_id_image',
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='carrier',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='comments',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='contents',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='departure_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='expected_delivery_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='origin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='pick_up_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='pick_up_time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='receiver_address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='receiver_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='receiver_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='receiver_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='shipper_address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='shipper_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='shipper_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='shipper_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='shippment_destination',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='shippingdetail',
            name='shippment_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='code',
            field=models.CharField(default=shipping.models.generate_shippment_code, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='shippingdetail',
            name='status',
            field=models.CharField(blank=True, choices=[('processing', 'Processing'), ('in_transit', 'In Trransit'), ('out_for_delivery', 'Out for Delivery'), ('delivered', 'Delivered')], max_length=50, null=True),
        ),
    ]
