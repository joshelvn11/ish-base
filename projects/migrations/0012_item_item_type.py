# Generated by Django 4.2.10 on 2024-07-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_rename_userstory_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('USER_STORY', 'USER_STORY'), ('TASK', 'TASK'), ('BUG', 'BUG'), ('DOCUMENTATION', 'DOCUMENTATION')], default='TASK'),
        ),
    ]
