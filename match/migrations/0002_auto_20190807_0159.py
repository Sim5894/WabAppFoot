# Generated by Django 2.2.4 on 2019-08-06 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joueursselect',
            name='journee',
            field=models.IntegerField(unique=True),
        ),
    ]
