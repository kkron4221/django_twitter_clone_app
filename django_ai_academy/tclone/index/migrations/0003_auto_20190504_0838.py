# Generated by Django 2.1.5 on 2019-05-04 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='new_tweet',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
