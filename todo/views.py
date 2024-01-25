from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models
 
from .forms import TodoForm, ChecklistItemForm
from .models import Todo, ChecklistItem

# Create your views here.
def index(request):
    
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
    
    
    page = {
        "forms" : form,
        "list" : item_list ,

        "title" : "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed!")
    return redirect('todo')

#
#new view

def checklist(request):
    if request.method == 'POST':
        checklist = ChecklistItemForm(request.POST)
        if checklist.is_valid():
            checklist.save()
            return redirect('checklist')
    else:
        checklist = ChecklistItemForm()

    checklist_items = ChecklistItem.objects.order_by('completed', '-id')
    return render(request, 'todo/index.html', {'checklist': checklist, 'checklist_items': checklist_items})
