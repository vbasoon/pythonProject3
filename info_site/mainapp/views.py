from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *
# Create your views here.

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Create Blog', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Register', 'url_name': 'register'}
]


def index(request):
    posts = News.objects.all()
    #categories = Category.objects.all()
    context = {
        'posts': posts,
        #'categories': categories,
        'menu': menu,
        'title': 'Головна сторінка',
        'categories_selected': 0
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    return render(request, 'mainapp/about.html', {'menu': menu, 'title': 'Про Нас'})


def add_page(request):
    return HttpResponse('Додати новину')


def contact(request):
    return HttpResponse('Контакти')


def login(request):
    return HttpResponse('Логін')


def register(request):
    return HttpResponse('Реєстрація')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'categories_selected': post.categories_id,
    }
    return render(request, 'mainapp/post.html', context=context)


# def show_category(request, category_id):
#     posts = News.objects.filter(categories_id=category_id)
#     categories = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'categories': categories,
#         'menu': menu,
#         'title': 'Тема: ',
#         'categories_selected': category_id,
#     }
#     return render(request, 'mainapp/index.html', context)

def show_category(request, category_slug):
    posts = News.objects.filter(categories__slug=category_slug)

    #categories = Category.objects.all()

    context = {
             'posts': posts,
             #'categories': categories,
             #'menu': menu,
             'title': 'Тема: ',
             'categories_selected': category_slug,
    }

    return render(request, 'mainapp/index.html', context)
# def categories(request, cat):
#     print(request.GET)
#     return HttpResponse(f"<h1>Статті за категоріями</h1><p>{cat}</p>")
#
#
# def archive(request, year):
#     if int(year) > 2022:
#         return redirect('home', permanent=True)
#
#     return HttpResponse(f"<h1>Архів за роками</h1><p>{year}</p>")
#
