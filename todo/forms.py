from django import forms


class TodoForm(forms.Form):
    input_text = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'id': 'input', 'placeholder': 'Enter todo e.g. Commit git',
               'required': 'required'}
    ))
