# Generated by Django 3.0.8 on 2020-08-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.PositiveSmallIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
