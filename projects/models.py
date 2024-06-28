from django.db import models
from django.contrib.auth.models import User

PRIORITY = [(1, "CRITICAL"),
            (2, "ESSENTIAL"),
            (3, "BENEFICIAL"),
            (4, "OPTIONAL")]

STATUS = [("TO DO", "TO DO"),
          ("IN PROGRESS", "IN PROGRESS"),
          ("REVIEW", "REVIEW"),
          ("DONE", "DONE")]


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
    status = models.CharField(choices=STATUS, default="TO DO")

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
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    user_story = models.TextField(null=True, blank=True)
    subtasks = models.JSONField(null=True, editable=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY, null=True, blank=True)
    status = models.CharField(choices=STATUS, default="TO DO")


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, on_delete=models.CASCADE, null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    subtasks = models.JSONField(null=True, editable=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY, null=True, blank=True)
    status = models.CharField(choices=STATUS, default="TO DO")
