# Generated by Django 4.2.10 on 2024-07-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_task_status_alter_userstory_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userstory',
            name='acceptance_criteria',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
