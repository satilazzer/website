# Generated by Django 3.2.4 on 2023-06-18 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_center_slider1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='center',
            name='slider1',
        ),
        migrations.RemoveField(
            model_name='center',
            name='slider2',
        ),
        migrations.RemoveField(
            model_name='center',
            name='slider3',
        ),
        migrations.RemoveField(
            model_name='center',
            name='slider4',
        ),
        migrations.RemoveField(
            model_name='center',
            name='slider5',
        ),
        migrations.RemoveField(
            model_name='center',
            name='slider6',
        ),
    ]
