from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, get_user_tasks, get_users

router = DefaultRouter()
router.register(r'tasks', TaskViewSet) # API: /api/tasks/
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)), 
   

    path('users/<int:user_id>/tasks/', get_user_tasks, name='get_user_tasks'),
    path('users/', get_users, name='get_users'),
]
