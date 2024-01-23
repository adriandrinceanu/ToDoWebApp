
from django import forms
from .models import Todo, CheckboxItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        
class CheckboxItemForm(forms.ModelForm):
    class Meta:
        model = CheckboxItem
        fields = ['title', 'completed']