# Generated by Django 3.2.14 on 2023-05-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medic', '0002_auto_20230516_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
