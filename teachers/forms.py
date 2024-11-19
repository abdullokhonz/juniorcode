from django.forms import ModelForm, TextInput, DateInput, Textarea
from .models import Teachers


class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'birth_date', 'bio']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заполните это поле',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заполните это поле',
            }),
            'birth_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Не обязательно',
            }),
            'bio': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Не обязательно',
            }),
        }

    def __init__(self, *args, **kwargs):
        readonly = kwargs.pop('readonly', False)
        super().__init__(*args, **kwargs)

        if readonly:
            for field in self.fields.values():
                field.widget.attrs['readonly'] = 'readonly'
                field.widget.attrs['disabled'] = 'disabled'
