from django.contrib import admin
from .models import Project, Epic, Sprint, UserStory, Task

admin.site.register(Project)
admin.site.register(Epic)
admin.site.register(Sprint)
admin.site.register(UserStory)
admin.site.register(Task)
