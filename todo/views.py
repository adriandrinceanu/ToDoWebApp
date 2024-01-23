from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models
 
from .forms import TodoForm, CheckboxItemForm
from .models import Todo, CheckboxItem

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
#checkboxex
#

def checkboxex(request):
    items = CheckboxItem.objects.all()
    return render(request, 'todo/index.html', {'items': items})

def add_checkbox(request):
    if request.method == "POST":
        checkbox = CheckboxItemForm(request.POST)
        if checkbox.is_valid():
            checkbox.save()
            messages.info(request, "item added!")
            return redirect('checkboxex')
    else:
        checkbox = CheckboxItemForm()
    return render(request, 'todo/index.html', {'checkbox': checkbox})