# Generated by Django 4.1.6 on 2023-04-17 14:03

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_main', '0006_article_approved_article_email_article_opinion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Sports', 'Sports'), ('Politics', 'Politics'), ('Business', 'Business'), ('Technology', 'Technology'), ('Environment', 'Environment'), ('Relgion', 'Religion'), ('Events', 'Events')], default=None, max_length=20),
        ),
    ]
