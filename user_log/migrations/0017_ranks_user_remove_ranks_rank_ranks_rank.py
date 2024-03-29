# Generated by Django 4.1.2 on 2024-02-01 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_log', '0016_remove_ranks_rank_one_ranks_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranks',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_log.user'),
        ),
        migrations.RemoveField(
            model_name='ranks',
            name='rank',
        ),
        migrations.AddField(
            model_name='ranks',
            name='rank',
            field=models.IntegerField(null=True),
        ),
    ]
