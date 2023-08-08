from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('dashboard/', views.dashboard_view, name="dashboard_view"),
    path('auth/register/', views.register_view, name="register_view"),
    path("auth/login/", views.login_view, name="login_view"),
    path('auth/logout/', views.logout_view, name="logout_view"),

]
