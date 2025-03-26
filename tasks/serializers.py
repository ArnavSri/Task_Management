from rest_framework import serializers
from .models import Task, User

class UserSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = User
        fields = ['userId', 'username', 'email', 'mobile']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  
            password=validated_data['password']
        )
        return user

class TaskSerializer(serializers.ModelSerializer):
    task_id = serializers.IntegerField(source='id', read_only=True)  # ✅ Renamed `id` to `task_id`

    class Meta:
        model = Task
        fields = ['task_id', 'task_name', 'description', 'created_at', 'task_type', 'completed_at', 'status']
