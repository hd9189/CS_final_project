# Generated by Django 4.1.6 on 2023-05-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_main', '0008_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default=False, max_length=9999),
        ),
    ]
