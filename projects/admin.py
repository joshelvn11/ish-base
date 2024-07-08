from django.contrib import admin
from .models import Project, Epic, Sprint, Item, Task

admin.site.register(Project)
admin.site.register(Epic)
admin.site.register(Sprint)
admin.site.register(Item)
admin.site.register(Task)
