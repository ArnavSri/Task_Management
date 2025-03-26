from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from .models import Task, User
from .serializers import TaskSerializer,UserSerializer
from django.db import IntegrityError
from django.http import JsonResponse
from .models import User 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer 
    
    def create(self, request, *args, **kwargs):
        """  Create a new task """
        task_name = request.data.get('task_name')
        description = request.data.get('description')
        task_type = request.data.get('task_type')

        # Validate input fields
        if not task_name or not description or not task_type:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Create task with default values for `completed_at` and `status`
        task = Task.objects.create(
            task_name=task_name,
            description=description,
            task_type=task_type
        )
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'], url_path='assign')
    def assign_task_to_users(self, request):
        """ Assign a task to multiple users """
        task_id = request.data.get('task_id')
        user_ids = request.data.get('user_ids', [])

        if not task_id or not user_ids:
            return Response({"error": "task_id and user_ids are required"}, status=status.HTTP_400_BAD_REQUEST)

        task = get_object_or_404(Task, id=task_id)
        users = User.objects.filter(id__in=user_ids)

        if not users.exists():
            return Response({"error": "Invalid user IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

        task.assigned_users.set(users)

        assigned_users_data = [
            {"user_id": user.id, "username": user.username, "email": user.email, "mobile": user.mobile}
            for user in users
        ]

        response_data = {
            "message": "Task assigned successfully",
            "task": {
                "task_id": task.id,
                "task_name": task.task_name,
                "assigned_users": assigned_users_data
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET']) 
def get_user_tasks(request, user_id): 
    """Fetch all tasks assigned to a specific user."""
    user = get_object_or_404(User, id=user_id)
    tasks = Task.objects.filter(assigned_users=user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data) 


@api_view(['GET'])
def get_users(request):
    """Fetch all users."""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
