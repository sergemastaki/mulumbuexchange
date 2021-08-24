# Generated by Django 3.2.6 on 2021-08-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210710_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account_number',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='transaction',
            name='moyen',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='transaction',
            name='tx_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.CharField(default='', max_length=100),
        ),
    ]
