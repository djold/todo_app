from django.shortcuts import render, redirect,get_object_or_404
from .models import TaskModel
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks_done = TaskModel.objects.filter(status=True)
    tasks_not_done = TaskModel.objects.filter(status=False)
    form = TaskForm()
    return render(request, template_name='index.html', context={'tasks_done': tasks_done, 'tasks_not_done': tasks_not_done, 'form': form})


def create_view(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/')

def done_view(request, pk):
    task = get_object_or_404(TaskModel, id=pk)
    task.status = True
    task.save()
    return redirect('/')

