from django import forms
from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('titlr', 'description', 'department', 'members', 'project', 'start_time', 'end_time', 'priority', 'status')

class TaskItemForm(forms.ModelForm):
    class Meta:
        model = Task_item
        fields = ('title', 'task', 'description', 'members', 'status')

class TaskImageForm(forms.ModelForm):
    class Meta:
        model = Task_image
        fields = ('title', 'task', 'image')

class TaskFileForm(forms.ModelForm):
    class Meta:
        model = Task_file
        fields = ('title', 'task', 'file')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fieds = ('title', 'image', 'body')