Оптимизировал запросы к бд (при авторизированном пользователе их количество при загрузке главной страницы доходило до 85(!), удалось снизить до 4-6 путем включения кэширования, использования переменных в шаблонах и методов annotate и prefetch_related). 

Добавил задание D6. Отписка/подписка реализована через AJAX-запросы. Механизм реализован как из списка постов, так и на странице конкретного поста.

Добавил модальное окно для добавления категорий.

Добавил возможность оставлять комментарии на странице новостей. 

Добавил задание D4. Вместо отдельной страницы с подтверждением удаления сделал модальное окно.

Shell-команды:

Импортируем модели для работы с ними:

```
from django.contrib.auth.models import User
from news.models import *
```

Создаем двух юзеров:

```
User.objects.create_user(username='OneHandedPirate', email='some@email.com', password='12345')
User.objects.create_user(username='SomeRandomGuy', email='another@email.com', password='54321')
```


Создаем 2 авторов из ранее созданных юрезов:

```
Author.objects.create(author_user=User.objects.get(username='OneHandedPirate'))
Author.objects.create(author_user=User.objects.get(username='SomeRandomGuy'))
```


Создаем 4 категории:

```
Category.objects.create(name='Спорт')
Category.objects.create(name='Политика')
Category.objects.create(name='Технологии')
Category.objects.create(name='Развлечения')
```


Создаем 3 поста:

```
Post.objects.create(author=Author.objects.get(author_user__username='OneHandedPirate'), title='О спорт ты мир!', text='Статья о Пьере де Кубернете')
Post.objects.create(author=Author.objects.get(author_user__username='SomeRandomGuy'), type='N', title='Новости технологических развлечений', text='Репортаж из Япони
и')
Post.objects.create(author=Author.objects.get(author_user__username='OneHandedPirate'), title='Статья о политике', text='Какой-то текст')
```


Задаем катеогории статьям: 

```
Post.objects.get(title='Статья о политике').category.set([Category.objects.get(name='Политика'), Category.objects.get(name='Развлечения')])  
Post.objects.get(title='О спорт ты мир!').category.set([Category.objects.get(name='Спорт')])
Post.objects.get(title='Новости технологических развлечений').category.set([Category.objects.get(name='Развлечения'), Category.objects.get(name='Технологии')])
```


Создаем комментарии:

```
Comment.objects.create(post=Post.objects.get(title='О спорт ты мир!'), user=User.objects.get(username='OneHandedPirate'), text='Отличная статья!')
Comment.objects.create(post=Post.objects.get(title='О спорт ты мир!'), user=User.objects.get(username='SomeRandomGuy'), text='Подтверждаю!')
Comment.objects.create(post=Post.objects.get(title='Новости технологических развлечений'), user=User.objects.get(username='OneHandedPirate'), text='Вот это да!')
Comment.objects.create(post=Post.objects.get(title='Статья о политике'), user=User.objects.get(username='OneHandedPirate'), text='Политика- грязное дело!')
```

Ставим лайки/дизлайки постам и комментариям:

```
Post.objects.get(title='О спорт ты мир!').like()
Comment.objects.get(text='Вот это да!').like()
Post.objects.get(pk=2).dislike()
Comment.objects.get(pk=2).dislike()
```

Обновляем рейтинг авторов:

```
Author.objects.get(author_user__username='OneHandedPirate').update_rating()
Author.objects.get(author_user__username='SomeRandomGuy').update_rating()
```

Определяем лучшего автора и выводим его поля:

```
best_author = Author.objects.all().order_by('-rating')[0]
best_author.author_user
best_author.rating
```

Определяем лучший пост и выводим его поля: 

```
best_post = Post.objects.order_by('-rating')[0]
best_post.publish_time.strftime('%d.%m.%Y')
best_post.author
best_post.title
best_post.preview()
```

Выводим поля комментариев лучшего поста:

```
n = 0
for i in best_post.comment_set.all():
  n+=1
  print(f‘Комментарий #{n}’)    
  i.publish_time.strftime('%d.%m.%Y')
  i.user
  i.rating
  i.text
```
