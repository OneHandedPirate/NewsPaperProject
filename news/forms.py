from django import forms
from .models import Post
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].empty_label = 'Выбор автора'

    class Meta:
        model = Post
        fields = ['author', 'type', 'category', 'title', 'text']
        labels = {
            'author': 'Автор',
            'type': 'Тип поста',
            'category': 'Категории',
            'title': 'Название',
            'text': 'Текст'
        }

        widgets = {
            'author': forms.Select(attrs={'class': 'form-select form-select-sm'}, ),
            'type': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Введите название'}),
            'text': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Введите текст'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-select', 'size': 2}),
        }

class CustomSignupForm(SignupForm):
    become_author = forms.BooleanField(label='Стать автором', required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        common_group = Group.objects.get(name='common')
        common_group.user_set.add(user)
        if self.cleaned_data['become_author']:
            authors_group = Group.objects.get(name='authors')
            authors_group.user_set.add(user)
        return user






