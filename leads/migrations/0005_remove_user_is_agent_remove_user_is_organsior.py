# Generated by Django 5.0.6 on 2024-07-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_user_is_agent_alter_user_is_organsior'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_agent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_organsior',
        ),
    ]
