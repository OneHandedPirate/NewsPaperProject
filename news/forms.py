import django.forms as forms
from .models import Post

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






