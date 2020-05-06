# Generated by Django 2.2.5 on 2020-05-03 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('google_scholar', '0004_auto_20200503_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='authors', to='google_scholar.Topic'),
        ),
    ]
