from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = 'Todo List Admin'
admin.site.site_title = 'Welcome to ToDo List'+'s dhashboard'
admin.site.index_title = 'Welcome to this portal'

urlpatterns = [
    path('', views.home , name='home'),
    path('tasks' , views.tasks , name = 'tasks'),
    path('update/<int:id>/', views.update_task, name='update_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task')
]