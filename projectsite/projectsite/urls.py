from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', RedirectView.as_view(pattern_name='task-list', permanent=False)),

    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    path('subtasks/', views.SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/create/', views.SubTaskCreateView.as_view(), name='subtask-create'),
    path('subtasks/<int:pk>/update/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<int:pk>/delete/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),

    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('priorities/', views.PriorityListView.as_view(), name='priority-list'),
    path('priorities/create/', views.PriorityCreateView.as_view(), name='priority-create'),
    path('priorities/<int:pk>/update/', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priorities/<int:pk>/delete/', views.PriorityDeleteView.as_view(), name='priority-delete'),

    path('notes/', views.NoteListView.as_view(), name='note-list'),
    path('notes/create/', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='note-delete'),
]