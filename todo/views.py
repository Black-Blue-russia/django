from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.
def todoview(request):
    all = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_items':all})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content =c)
    new_item.save()
    return HttpResponseRedirect('/todo/')
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
