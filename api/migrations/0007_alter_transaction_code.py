# Generated by Django 3.2.6 on 2021-08-24 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210824_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='code',
            field=models.TextField(default=''),
        ),
    ]
