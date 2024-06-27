from django.db import models
from django.contrib.auth.models import User

PRIORITY = [(1, "CRITICAL"),
            (2, "ESSENTIAL"),
            (3, "BENEFICIAL"),
            (4, ("OPTIONAL"))]


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)

    def __str__(self):
        return f"[USER] {self.owner.username} [PROJECT] {self.name}"


class Epic(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)

    def __str__(self):
        return f"[EPIC] {self.name} [PROJECT] {self.project.name} [USER] {self.project.owner.username}"


class Sprint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class UserStory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    user_story = models.TextField(null=True)
    subtasks = models.JSONField(null=True, editable=True)
    due_date = models.DateField(null=True)
    priority = models.IntegerField(choices=PRIORITY, null=True)


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE, null=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    subtasks = models.JSONField(null=True, editable=True)
    due_date = models.DateField(null=True)
    priority = models.IntegerField(choices=PRIORITY, null=True)
