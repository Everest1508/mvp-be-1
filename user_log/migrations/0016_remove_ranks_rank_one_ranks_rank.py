# Generated by Django 4.1.2 on 2024-02-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_log', '0015_ranks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranks',
            name='rank_one',
        ),
        migrations.AddField(
            model_name='ranks',
            name='rank',
            field=models.ManyToManyField(blank=True, null=True, to='user_log.user'),
        ),
    ]
