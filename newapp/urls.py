from django.urls import path
from .views import PostsList, PostList  # импортируем наше представление
 
 
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostsList.as_view(), name='posts'), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostList.as_view(), name='post'),  # pk — это первичный ключ поста, который будет выводиться у нас в шаблон
]