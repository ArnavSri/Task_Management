from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, get_user_tasks, get_users

router = DefaultRouter()
router.register(r'tasks', TaskViewSet) # API: /api/tasks/
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # ✅ Register ViewSet-based APIs

    # ✅ Fix: Ensure assign_task_to_users API is correctly mapped as a POST request
    #path('tasks/assign/', assign_task_to_users, name='assign_task_to_users'),

    path('users/<int:user_id>/tasks/', get_user_tasks, name='get_user_tasks'),
    path('users/', get_users, name='get_users'),
]
