# Generated by Django 4.2.10 on 2024-07-08 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_item_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('USER STORY', 'USER STORY'), ('TASK', 'TASK'), ('BUG', 'BUG'), ('DOCUMENTATION', 'DOCUMENTATION')], default='TASK'),
        ),
    ]
