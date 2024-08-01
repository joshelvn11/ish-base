from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProjectSettings, Project, Epic


@receiver(post_save, sender=Project)
def create_user_project_settings(sender, instance, created, **kwargs):
    if created:
        # Define the default backlog filter options
        default_backlog_filter_options = {
            "sortBy": "",
            "sortOrder": "",
            "filterType": ["USER STORY", "TASK", "BUG", "DOCUMENTATION"],
            "filterStatus": ["TO DO", "IN PROGRESS", "REVIEW", "DONE"],
            "filterPriority": ["OPTIONAL", "BENEFICIAL", "ESSENTIAL", "CRITICAL"],
            "filterSprint": "",
            }
        # Create UserProjectSettings for the owner of the project
        UserProjectSettings.objects.create(user=instance.owner, project=instance, backlog_filter_options=default_backlog_filter_options)
