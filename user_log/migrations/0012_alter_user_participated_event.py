# Generated by Django 4.1.2 on 2024-01-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_log', '0011_user_participated_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='participated_event',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
