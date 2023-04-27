from django.urls import path
# from django.urls.resolvers import URLPattern
from django.urls import path
from .views import (
    PostList, PostDetail, PostSearch, PostCreate, NewsCreate, PostUpdate, NewsUpdate, PostDelete, NewsDelete,
    subscriptions
)  # Импортируем представления, написанные в файле "views.py"
from django.views.decorators.cache import cache_page  # Кэш страниц (использовать кэширование можно только с GET
# HTTP-запросами, т. к. POST-запрос отправляет данные клиента на сервер, что не совсем подходит под случай,
# когда можно использовать кэширование)

urlpatterns = [
    path('', cache_page(60)(PostList.as_view()), name='post_list'),  # Кэш списка постов
    # path('<int:pk>', cache_page(120)(PostDetail.as_view()), name='post_detail'),  # pk — это первичный ключ новости или статьи,
    # # который будет выводиться у нас в шаблон int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='posts_search'),  # Поиск публикаций
    path('articles/create/', PostCreate.as_view(), name='post_create'),  # Создание поста
    path('news/create/', NewsCreate.as_view(), name='news_create'),  # Создание новости
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),  # Редактирование поста
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),  # Редактирование новости
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),  # Удаление поста
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),  # Удаление новости
    path('subscriptions/', subscriptions, name='subscriptions')
]
# Path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, чуть позже станет ясно почему.
# Т.к. наше объявленное представление является классом, а Django ожидает функцию, нам надо представить этот класс в
# виде view. Для этого вызываем метод f as_view.