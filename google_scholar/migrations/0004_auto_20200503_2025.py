# Generated by Django 2.2.5 on 2020-05-03 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('google_scholar', '0003_auto_20200503_0422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['topic_name'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='google_scholar.Topic'),
        ),
    ]
