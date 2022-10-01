from django import forms


class AddEditForm(forms.Form):
    author = forms.CharField(max_length=200, required=True, label='Author',
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Введите автора',
                                        'type': 'text', 'class': 'form-control mb-2'}))
    email = forms.CharField(max_length=254, required=True, label='Email',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Введите email',
                                       'type': 'text', 'class': 'form-control mb-2'}))
    text = forms.CharField(max_length=200, required=True, label='Text',
                           widget=forms.Textarea(
                               attrs={'placeholder': 'Введите текст', 'rows': '3', 'class': 'form-control mb-2'}))
