# Generated by Django 3.2.6 on 2021-08-25 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210825_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='taux',
            field=models.FloatField(default=1),
        ),
    ]
