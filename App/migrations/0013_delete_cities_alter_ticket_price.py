# Generated by Django 5.0.1 on 2024-04-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_rename_booking_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cities',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]
