# Generated by Django 4.0.1 on 2022-06-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_blogitem_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogitem',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
