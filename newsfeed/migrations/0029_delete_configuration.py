# Generated by Django 2.2.17 on 2021-02-23 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0028_news_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Configuration',
        ),
    ]
