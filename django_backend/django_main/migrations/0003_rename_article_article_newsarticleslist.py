# Generated by Django 4.1.6 on 2023-02-27 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_main', '0002_alter_article_likes_alter_article_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='article',
            new_name='newsarticleslist',
        ),
    ]
