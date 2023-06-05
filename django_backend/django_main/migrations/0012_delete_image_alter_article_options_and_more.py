# Generated by Django 4.1.6 on 2023-05-15 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_main', '0011_article_profile_pic_article_title_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='profile_pic',
            new_name='profile_pic_url',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title_img',
            new_name='title_img_url',
        ),
    ]