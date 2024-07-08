from rest_framework import permissions


class IsProjectOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of the related project to access the object.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the object has a 'project' attribute and if the owner of the project is the requesting user
        print("Checking permissions")
        if hasattr(obj, 'project'):
            print(obj.project)
            print(obj.project.owner)
            return obj.project.owner == request.user
        # Fallback to check if the object itself has an 'owner' attribute
        return obj.owner == request.user
