# Generated by Django 3.1 on 2020-08-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_auto_20200831_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='register_date',
            field=models.DateTimeField(verbose_name='date registered'),
        ),
    ]