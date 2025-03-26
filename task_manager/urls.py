from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple Home Page Response
def home(request):
    return HttpResponse("<h1>Welcome to the Task Manager</h1>")

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin Panel
    path("api/", include("tasks.urls")),  # API routes
    path("", home),  # Add this line for root URL
]
