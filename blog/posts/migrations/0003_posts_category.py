# Generated by Django 4.0.2 on 2022-02-23 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.CharField(default='movies', max_length=100),
        ),
    ]
