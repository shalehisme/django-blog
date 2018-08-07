from django.urls import path

from .views import users_signin, users_register, users_logout, users_dashboard, users_action

app_name = 'users'
urlpatterns = [
    path('signin', users_signin, name='signin'),
    path('create', users_register, name='register'),
    path('logout', users_logout, name='logout'),
    path('dashboard', users_dashboard, name='dashboard'),
    path('action/<int:pk>/<int:action>', users_action, name='action')
]
