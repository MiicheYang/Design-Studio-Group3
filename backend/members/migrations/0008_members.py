# Generated by Django 3.1 on 2020-08-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_deposit_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.BigIntegerField()),
                ('deposit', models.IntegerField()),
                ('points', models.IntegerField()),
                ('level', models.SmallIntegerField()),
                ('discount', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]
