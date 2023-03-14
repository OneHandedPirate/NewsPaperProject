from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .filter import PostFilter
from .utils import get_filter_params
from .forms import *


menu = [{'title': 'Home', 'url_name': 'home'},
        {'title': 'Search', 'url_name': 'search'},
        {'title': 'Add post', 'url_name': 'add'},
        {'title': 'About Us', 'url_name': ''},
        {'title': 'Contact Us', 'url_name': ''},]


class News(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-publish_time')
    extra_context = {'menu': menu}
    paginate_by = 10


class PostView(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'
    extra_context = {'menu': menu}


class PostUpdateView(UpdateView):
    template_name = 'news/add_post.html'
    form_class = PostForm
    extra_context = {'menu': menu}

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        #Делаем редирект на ту же страницу из которой было вызвано представление
        referer = self.request.META.get('HTTP_REFERER')
        if referer and referer != self.request.build_absolute_uri():
            return referer

        return super().get_success_url()


class SearchPost(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['filter_params'] = get_filter_params(self.request)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return PostFilter(self.request.GET, queryset=queryset).qs


class AddPost(CreateView):
    form_class = PostForm
    template_name = 'news/add_post.html'
    extra_context = {'menu': menu}

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return redirect('home')

