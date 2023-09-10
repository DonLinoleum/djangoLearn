from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render

menu = [
    {'title': "О сайте", "url_name": "about"},
    {'title': "Добавить статью", "url_name": "add_page"},
    {'title': "Обратная связь", "url_name": "contact"},
    {'title': "Войти", "url_name": "login"},
]

data_db = [
    {'id': 1, 'title': 'Софокл', 'content': 'О Софокле', 'is_published': True},
    {'id': 2, 'title': 'Марк Антоний', 'content': 'О Марке Антонии', 'is_published': False},
    {'id': 3, 'title': 'Вильгельм', 'content': 'О Вильгельме', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'women/index.html', data)


def about(request: HttpRequest):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def show_post(reqeust: HttpRequest, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
