# Generated by Django 2.2.17 on 2021-02-08 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0013_auto_20210208_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginstance',
            name='current_config',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='newsfeed.Configuration'),
            preserve_default='True',
        ),
    ]
