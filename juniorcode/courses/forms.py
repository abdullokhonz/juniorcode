from django import forms
from .models import Courses
from students.models import Students
from teachers.models import Teachers


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name', 'description', 'teacher', 'students', 'start_date', 'end_date']

    class CourseForm(forms.Form):
        teacher = forms.ModelChoiceField(
            queryset=Teachers.objects.all(),
            required=False,
            label="Преподаватель:",
            widget=forms.Select(attrs={
                'class': 'form-control',
                'placeholder': "Выберите преподавателя",
            })
        )

        students = forms.ModelMultipleChoiceField(
            queryset=Students.objects.all(),
            required=False,
            label="Студенты:",
            widget=forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            })
        )

    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Заполните это поле',
        })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Не обязательно'
        })
    )

    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Не обязательно'
        })
    )

    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Не обязательно'
        })
    )

    def __init__(self, *args, **kwargs):
        readonly = kwargs.pop('readonly', False)
        super().__init__(*args, **kwargs)

        if readonly:
            for field in self.fields.values():
                field.widget.attrs['readonly'] = 'readonly'
                field.widget.attrs['disabled'] = 'disabled'
