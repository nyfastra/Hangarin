from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task, SubTask, Category, Priority, Note
from django.views.generic import TemplateView
from .models import Task

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['completed_tasks'] = Task.objects.filter(status='Completed').count()
        context['pending_tasks'] = Task.objects.filter(status='Pending').count()
        context['in_progress_tasks'] = Task.objects.filter(status='In Progress').count()
        return context


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )

        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        priority = self.request.GET.get('priority')
        if priority:
            queryset = queryset.filter(priority_id=priority)

        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category_id=category)

        sort_by = self.request.GET.get('sort')
        if sort_by in ['title', '-title', 'due_date', '-due_date', 'priority', 'status']:
            queryset = queryset.order_by(sort_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['priorities'] = Priority.objects.all()
        return context

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')


class SubTaskListView(ListView):
    model = SubTask
    template_name = 'subtask_list.html'
    context_object_name = 'subtasks'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().select_related('parent_task')
        
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(parent_task__title__icontains=query)
            )

        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)

        sort_by = self.request.GET.get('sort')
        if sort_by in ['title', '-title', 'status', '-status']:
            queryset = queryset.order_by(sort_by)
            
        return queryset

class SubTaskCreateView(CreateView):
    model = SubTask
    fields = '__all__'
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    fields = '__all__'
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        sort_by = self.request.GET.get('sort')
        if sort_by in ['name', '-name']:
            queryset = queryset.order_by(sort_by)
        return queryset

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')


class PriorityListView(ListView):
    model = Priority
    template_name = 'priority_list.html'
    context_object_name = 'priorities'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        sort_by = self.request.GET.get('sort')
        if sort_by in ['name', '-name']:
            queryset = queryset.order_by(sort_by)
        return queryset

class PriorityCreateView(CreateView):
    model = Priority
    fields = '__all__'
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    fields = '__all__'
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')


class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'notes'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().select_related('task')

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(content__icontains=query))

        created_at = self.request.GET.get('created_at')
        if created_at:
            queryset = queryset.filter(created_at__date=created_at)

        sort_by = self.request.GET.get('sort')
        if sort_by in ['content', '-content']:
            queryset = queryset.order_by(sort_by)

        return queryset

class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')