from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Epic, UserStory, Task, Sprint
from .serializers import ProjectSerializer, EpicSerializer, UserStorySerializer, TaskSerializer, SprintSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404
from .permissions import IsProjectOwner


@permission_classes([IsAuthenticated])
class ProjectListCreateAPIView(APIView):
    def get(self, request):
        # Get all the project objects that belong to the requesting user
        projects = Project.objects.filter(owner=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_object(self, pk):
        # Get the object and check permissions
        obj = get_object_or_404(Project, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProjectSerializer(project, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        if project is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EpicListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_objects(self, pk):
        # Retrieve epics for the request project
        project = get_object_or_404(Project, pk=pk)
        epics = Epic.objects.filter(project=project)
        # Check the permissions for the project object
        self.check_object_permissions(self.request, project)
        return epics

    def get(self, request, pk):
        epics = self.get_objects(pk)
        serializer = EpicSerializer(epics, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = EpicSerializer(data=request.data)
        project = get_object_or_404(Project, pk=pk)
        self.check_object_permissions(self.request, project)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EpicDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_object(self, project_pk, epic_pk):
        # Retrieve the requested epic
        epic = get_object_or_404(Epic, pk=epic_pk, project=project_pk)
        # Check if the requesting user own the epic's related project
        self.check_object_permissions(self.request, epic)
        return epic

    def get(self, request, project_pk, epic_pk):
        epic = self.get_object(project_pk, epic_pk)
        serializer = EpicSerializer(epic)
        return Response(serializer.data)

    def put(self, request, project_pk, epic_pk):
        epic = self.get_object(project_pk, epic_pk)
        serializer = EpicSerializer(epic, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        epic = self.get_object(pk)
        epic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SprintListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_objects(self, pk):
        # Retrieve sprints for the request project
        project = get_object_or_404(Project, pk=pk)
        sprints = Sprint.objects.filter(project=project)
        # Check the permissions for the project object
        self.check_object_permissions(self.request, project)
        return sprints

    def get(self, request, pk):
        sprints = self.get_objects(pk)
        serializer = SprintSerializer(sprints, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = SprintSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SprintDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_object(self, pk):
        obj = get_object_or_404(Sprint, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        sprint = self.get_object(pk)
        serializer = SprintSerializer(sprint)
        return Response(serializer.data)

    def put(self, request, pk):
        sprint = self.get_object(pk)
        serializer = SprintSerializer(sprint, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sprint = self.get_object(pk)
        sprint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserStoryListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_objects(self, pk):
        # Retrieve user stories for the request project
        project = get_object_or_404(Project, pk=pk)
        user_stories = UserStory.objects.filter(project=project)
        # Check the permissions for the project object
        self.check_object_permissions(self.request, project)
        return user_stories

    def get(self, request, pk):
        user_stories = self.get_objects(pk)
        serializer = UserStorySerializer(user_stories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserStorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserStoryDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_object(self, pk):
        obj = get_object_or_404(UserStory, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        user_story = self.get_object(pk)
        serializer = UserStorySerializer(user_story)
        return Response(serializer.data)

    def put(self, request, pk):
        user_story = self.get_object(pk)
        serializer = UserStorySerializer(user_story, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_story = self.get_object(pk)
        user_story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_objects(self, pk):
        # Retrieve tasks for the request project
        project = get_object_or_404(Project, pk=pk)
        tasks = Task.objects.filter(project=project)
        # Check the permissions for the project object
        self.check_object_permissions(self.request, project)
        return tasks

    def get(self, request, pk):
        tasks = self.get_objects(pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]

    def get_object(self, pk):
        obj = get_object_or_404(Task, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
