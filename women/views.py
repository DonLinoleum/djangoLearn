from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request):
    return HttpResponse("Хуй с маслом")


def categories(request: HttpRequest, cat_id: int) -> HttpResponse:
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat_id}</p>")


def categories_by_slug(request: HttpRequest, cat_slug: str):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat_slug}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{year}</p>")