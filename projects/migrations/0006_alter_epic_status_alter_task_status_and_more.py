# Generated by Django 4.2.10 on 2024-06-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_epic_status_alter_task_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epic',
            name='status',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('IN PROGRESS', 'IN PROGRESS'), ('REVIEW', 'REVIEW'), ('DONE', 'DONE')], default='TO DO'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('IN PROGRESS', 'IN PROGRESS'), ('REVIEW', 'REVIEW'), ('DONE', 'DONE')], default='TO DO'),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='status',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('IN PROGRESS', 'IN PROGRESS'), ('REVIEW', 'REVIEW'), ('DONE', 'DONE')], default='TO DO'),
        ),
    ]
