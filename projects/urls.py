from django.urls import path
from .views import ProjectListCreateAPIView, ProjectDetailAPIView, EpicListCreateAPIView, EpicDetailAPIView, ItemListCreateAPIView, ItemDetailAPIView, SprintListCreateAPIView, UserProjectSettingsDetailAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/<int:pk>/epics/', EpicListCreateAPIView.as_view(), name='epic-list-create'),
    path('projects/<int:project_pk>/epics/<int:epic_pk>/', EpicDetailAPIView.as_view(), name='epic-detail'),
    path('projects/<int:pk>/items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('projects/<int:project_pk>/items/<int:item_pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
    path('projects/<int:pk>/sprints/', SprintListCreateAPIView.as_view(), name='sprint-list-create'),
    path('projects/<int:project_pk>/user-settings/', UserProjectSettingsDetailAPIView.as_view(), name='project-user-settings-detail'),
]
