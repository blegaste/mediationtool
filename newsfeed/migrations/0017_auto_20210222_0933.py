# Generated by Django 2.2.17 on 2021-02-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0016_auto_20210216_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logaction',
            name='log_instance_id',
        ),
        migrations.AddField(
            model_name='logaction',
            name='log_instance_name',
            field=models.CharField(default='not provided', max_length=200),
        ),
    ]