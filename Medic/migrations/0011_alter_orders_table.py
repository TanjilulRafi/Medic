# Generated by Django 3.2.14 on 2023-05-19 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medic', '0010_alter_product_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='orders',
            table='Orders',
        ),
    ]