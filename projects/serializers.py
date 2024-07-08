from rest_framework import serializers
from .models import Project, Epic, Sprint, Item


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        # Set the owner to the requesting user
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class EpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = '__all__'


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
