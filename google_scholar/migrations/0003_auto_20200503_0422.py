# Generated by Django 2.2.5 on 2020-05-03 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_scholar', '0002_auto_20200503_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='image_url',
            field=models.CharField(default='/', max_length=100),
        ),
        migrations.AddField(
            model_name='journal',
            name='introduction',
            field=models.CharField(default='/', max_length=1000),
        ),
    ]
