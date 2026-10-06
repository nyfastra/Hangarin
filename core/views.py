from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, SubTask, Category, Priority, Note

class TaskListView(ListView):
    model = Task
    template_name = 'core/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        sort_by = self.request.GET.get('sort')
        if sort_by in ['title', '-title', 'due_date', '-due_date', 'priority', 'status']:
            queryset = queryset.order_by(sort_by)
        return queryset

class SubTaskListView(ListView):
    model = SubTask
    template_name = 'core/subtask_list.html'
    context_object_name = 'subtasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        sort_by = self.request.GET.get('sort')
        if sort_by in ['title', '-title', 'status', '-status']:
            queryset = queryset.order_by(sort_by)
        return queryset

class CategoryListView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        sort_by = self.request.GET.get('sort')
        if sort_by in ['name', '-name']:
            queryset = queryset.order_by(sort_by)
        return queryset

class PriorityListView(ListView):
    model = Priority
    template_name = 'core/priority_list.html'
    context_object_name = 'priorities'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        sort_by = self.request.GET.get('sort')
        if sort_by in ['name', '-name']:
            queryset = queryset.order_by(sort_by)
        return queryset

class NoteListView(ListView):
    model = Note
    template_name = 'core/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(content__icontains=query))
        sort_by = self.request.GET.get('sort')
        if sort_by in ['content', '-content']:
            queryset = queryset.order_by(sort_by)
        return queryset