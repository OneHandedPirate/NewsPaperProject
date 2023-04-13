from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['author__author_user__username__icontains'].\
            field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Author'})
        self.filters['title__icontains']. \
            field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Post title'})
        self.filters['publish_time__gte']. \
            field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Publish date'})

    class Meta:
        model = Post
        fields = {
            'author__author_user__username': ['icontains'],
            'title': ['icontains'],
            'publish_time': ['gte'],
            }
