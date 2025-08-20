from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from list.models import Task, Tag
from django.views import generic
from list.forms import TaskCreate, TaskUpdate
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, "list/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "list/form.html"
    success_url = reverse_lazy("list:homepage")
    form_class = TaskCreate


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "list/form.html"
    success_url = reverse_lazy("list:homepage")
    form_class = TaskUpdate


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "list/delete_confirm.html"
    success_url = reverse_lazy("list:homepage")


class TagListView(generic.ListView):
    model = Tag
    template_name = "list/tags.html"
    fields = ["name"]


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "list/form.html"
    success_url = reverse_lazy("list:tags-list")
    fields = ["name"]


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "list/form.html"
    success_url = reverse_lazy("list:tags-list")
    fields = ["name"]


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "list/delete_confirm.html"
    success_url = reverse_lazy("list:tags-list")
    fields = ["name"]


class UpdateDoneView(generic.View):
    def post(self, request, pk, action):
        task = Task.objects.get(id=pk)
        if action == "complete":
            task.is_done = True
        elif action == "undo":
            task.is_done = False
        task.save()
        return redirect("list:homepage")
