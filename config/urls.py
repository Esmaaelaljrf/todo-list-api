"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView ## This view validates the email and password, then returns access and refresh tokens.
from tasks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.UserCreatingView.as_view()),    #as_view: we use it when we work with basic-class views
    path('login/',TokenObtainPairView.as_view()),
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>/',views.TaskUpdateDeleteview.as_view())


]
