# Generated by Django 4.0 on 2022-07-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blogauthor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogitem',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
