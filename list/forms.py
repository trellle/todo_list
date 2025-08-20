from list.models import Task, Tag
from django import forms

class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]


class TaskCreate(TaskForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control"
            }
        ),
        required=False
    )
    
    class Meta(TaskForm.Meta):
        fields = ["content", "deadline", "tags"]


class TaskUpdate(TaskForm):
    class Meta(TaskForm.Meta):
        fields = ["content", "is_done", "tags"]
