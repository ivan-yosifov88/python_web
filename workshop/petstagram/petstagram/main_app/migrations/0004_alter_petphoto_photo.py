# Generated by Django 4.0.2 on 2022-02-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_petphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.IntegerField(),
        ),
    ]