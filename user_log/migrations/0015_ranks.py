# Generated by Django 4.1.2 on 2024-02-01 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_log', '0014_mainevent_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_log.user')),
                ('sub_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_log.subevents')),
            ],
        ),
    ]
