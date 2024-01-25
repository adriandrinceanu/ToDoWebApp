
from django import forms
from .models import Todo, ChecklistItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        
class ChecklistItemForm(forms.ModelForm):
    class Meta:
        model = ChecklistItem
        fields = "__all__"