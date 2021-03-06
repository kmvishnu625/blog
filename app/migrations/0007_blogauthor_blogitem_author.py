# Generated by Django 4.0 on 2022-07-14 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_commentitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='blogitem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.blogauthor'),
        ),
    ]
