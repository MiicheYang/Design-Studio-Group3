# Generated by Django 3.1 on 2020-08-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('transaction_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('volume', models.FloatField(default=0.0)),
                ('unit', models.CharField(max_length=10)),
                ('time_date', models.DateTimeField(auto_now_add=True)),
                ('resource', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=10)),
                ('explanation', models.CharField(max_length=100)),
            ],
        ),
    ]
