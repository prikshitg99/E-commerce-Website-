# Generated by Django 3.1.2 on 2020-12-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20201209_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
