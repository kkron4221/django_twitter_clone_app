# Generated by Django 2.1.5 on 2019-05-04 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190504_0838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.NewTweet')),
            ],
        ),
    ]
