# Generated by Django 3.2.4 on 2023-05-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230523_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='slider1',
            field=models.ImageField(default=None, upload_to='uploads/slider/'),
        ),
        migrations.AlterField(
            model_name='center',
            name='slider2',
            field=models.ImageField(default=None, upload_to='uploads/slider/'),
        ),
        migrations.AlterField(
            model_name='center',
            name='slider3',
            field=models.ImageField(default=None, upload_to='uploads/slider/'),
        ),
        migrations.AlterField(
            model_name='center',
            name='slider4',
            field=models.ImageField(default=None, upload_to='uploads/slider/'),
        ),
        migrations.AlterField(
            model_name='center',
            name='slider5',
            field=models.ImageField(default=None, upload_to='uploads/slider/'),
        ),
        migrations.AlterField(
            model_name='center',
            name='slider6',
            field=models.ImageField(default=None, upload_to='uploads/slider/'),
        ),
        migrations.AlterField(
            model_name='master',
            name='master_img',
            field=models.ImageField(default=None, upload_to='uploads/masters/'),
        ),
    ]
