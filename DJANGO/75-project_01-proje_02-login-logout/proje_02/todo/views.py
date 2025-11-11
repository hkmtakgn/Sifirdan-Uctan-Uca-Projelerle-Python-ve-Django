from django.shortcuts import render
from todo.models import Todo

# Create your views here.


def todo_views (request):
    tasks = Todo.objects.all().order_by("-pk")
    context = dict (tasks=tasks,)
    return render (request,"todo/todo_home.html",context)


from django.shortcuts import render
from todo.models import Todo

def todo_manager(request):
    tasks = Todo.objects.all().order_by("-pk")
    if request.method == "POST":
        todo_task = request.POST.get("todo_input")
        if todo_task:
            Todo.objects.create(title=todo_task)
        tasks = Todo.objects.all().order_by("-pk")
    if request.method == "GET":
        if request.GET.get ("delete-item"):
            del_id = request.GET.get ("delete-item")
            Todo.objects.filter (id=del_id).delete ()
        if request.GET.get ("delete-item-all"):
            tasks.delete()

    context = dict (
        tasks=tasks,
    )
    return render(request, "todo/todo_home.html", context)
