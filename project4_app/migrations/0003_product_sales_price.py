# Generated by Django 2.1.1 on 2018-10-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4_app', '0002_auto_20181008_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales_price',
            field=models.FloatField(null=True),
        ),
    ]
