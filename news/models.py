from django.db.models import Sum
from django.urls import reverse_lazy
from django.db import models
from django.contrib.auth.models import User

class Attitude:
    '''Миксин-класс для моделей с полем rating'''

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

class Author(models.Model):
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.author_user.get_username()

    def update_rating(self):
        #post_set.all() - объекты post, связанные с автором.
        posts_rating = self.post_set.all().aggregate(posts_rating=Sum('rating'))
        p_r = posts_rating.get('posts_rating', 0) * 3

        comments_ratings = self.author_user.comment_set.all().aggregate(c_rating=Sum('rating'))
        c_r = comments_ratings.get('c_rating', 0)
        self.rating = p_r + c_r
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model, Attitude):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1,
                            choices=[('N', 'Новость'), ('A', 'Статья')],
                            default='A')
    publish_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=150)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return f'{self.text[:124]}...'

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return reverse_lazy('post', kwargs={'pk': self.id})


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model, Attitude):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text


