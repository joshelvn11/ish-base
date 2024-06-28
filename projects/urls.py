from django.urls import path
from .views import ProjectListCreateAPIView, ProjectDetailAPIView, EpicListCreateAPIView, EpicDetailAPIView, UserStoryListCreateAPIView, UserStoryDetailAPIView

urlpatterns = [
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/<int:pk>/epics/', EpicListCreateAPIView.as_view(), name='epic-list-create'),
    path('projects/<int:pk>/user-stories/', UserStoryListCreateAPIView.as_view(), name='user-story-list-create'),
]
