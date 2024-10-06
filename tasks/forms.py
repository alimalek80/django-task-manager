from django import forms
from .models import Task, Category


class TaskForm(forms.ModelForm):
    new_category = forms.CharField(max_length=100, required=False, label="New Category")
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'category',
            'due_date',
            'start_time',
            'end_time'
        ]
        widgets = {
            'due_date': forms.SelectDateWidget(),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def save(self, commit=True):
        # Check if the user provided a new Category
        new_category_name = self.cleaned_data.get('new_category')
        if new_category_name:
            # Create the new category
            category, created = Category.objects.get_or_create(name=new_category_name)
            self.instance.category = category
        return super().save(commit=commit)
