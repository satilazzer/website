# Generated by Django 3.2.4 on 2023-06-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_center_slider1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='slider1',
            field=models.ImageField(default=None, upload_to='uploads/slider/name'),
        ),
    ]
