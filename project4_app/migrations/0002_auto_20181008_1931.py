# Generated by Django 2.1.1 on 2018-10-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project4_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
