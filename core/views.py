from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, SubTask, Category, Priority, Note


class TaskListView(ListView):
    model = Task
    template_name = 'core/task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'core/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'core/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'core/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')


class SubTaskListView(ListView):
    model = SubTask
    template_name = 'core/subtask_list.html'
    context_object_name = 'subtasks'

class SubTaskCreateView(CreateView):
    model = SubTask
    fields = '__all__'
    template_name = 'core/subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    fields = '__all__'
    template_name = 'core/subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'core/subtask_confirm_delete.html'
    success_url = reverse_lazy('subtask-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'core/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'core/category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'core/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


class PriorityListView(ListView):
    model = Priority
    template_name = 'core/priority_list.html'
    context_object_name = 'priorities'

class PriorityCreateView(CreateView):
    model = Priority
    fields = '__all__'
    template_name = 'core/priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    fields = '__all__'
    template_name = 'core/priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'core/priority_confirm_delete.html'
    success_url = reverse_lazy('priority-list')


class NoteListView(ListView):
    model = Note
    template_name = 'core/note_list.html'
    context_object_name = 'notes'

class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    template_name = 'core/note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    template_name = 'core/note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'core/note_confirm_delete.html'
    success_url = reverse_lazy('note-list')