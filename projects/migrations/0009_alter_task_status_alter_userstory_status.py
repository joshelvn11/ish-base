# Generated by Django 4.2.10 on 2024-06-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_epic_description_alter_epic_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('TO DO', 'TO DO'), ('IN PROGRESS', 'IN PROGRESS'), ('REVIEW', 'REVIEW'), ('DONE', 'DONE')], null=True),
        ),
        migrations.AlterField(
            model_name='userstory',
            name='status',
            field=models.CharField(blank=True, choices=[('TO DO', 'TO DO'), ('IN PROGRESS', 'IN PROGRESS'), ('REVIEW', 'REVIEW'), ('DONE', 'DONE')], null=True),
        ),
    ]