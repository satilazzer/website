# Generated by Django 3.2.4 on 2023-05-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20230523_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='master',
            name='specialized',
            field=models.CharField(max_length=100, verbose_name='specialized'),
        ),
    ]
