from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django .views.generic import ListView, DetailView, CreateView

from .models import *
from .forms import *
# Create your views here.

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Create Blog', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Register', 'url_name': 'register'}
]


class NewsHome(ListView):
    model = News
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Головна сторінка'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Головна сторінка'
        context['categories_selected'] = 0
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class AddPage(CreateView):
    form_class = AddNewsForm
    template_name = 'mainapp/addpage.html'
    success_url = reverse_lazy('home')
    #context_object_name = 'posts'
    # extra_context = {'title': 'Головна сторінка'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Додати новину'
        return context



# def index(request):
#     posts = News.objects.filter(is_published=True)
#     #categories = Category.objects.all()
#     context = {
#         'posts': posts,
#         #'categories': categories,
#         'menu': menu,
#         'title': 'Головна сторінка',
#         'categories_selected': 0
#     }
#     return render(request, 'mainapp/index.html', context)
#

def about(request):
    return render(request, 'mainapp/about.html', {'menu': menu, 'title': 'Про Нас'})


# def add_page(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             try:
#                 News.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Помилка додавання запису')
#
#     else:
#         form = AddNewsForm()
#     return render(request, 'mainapp/addpage.html', {'form': form, 'menu': menu, 'title': 'Додати новину'})
#

def contact(request):
    return HttpResponse('Контакти')


def login(request):
    return HttpResponse('Логін')


def register(request):
    return HttpResponse('Реєстрація')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')


# def show_post(request, post_slug):
#     post = get_object_or_404(News, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'categories_selected': post.categories_id,
#     }
#     return render(request, 'mainapp/post.html', context=context)


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


class ShowPost(DetailView):
    model = News
    template_name = 'mainapp/post.html'
    slug_url_kwargs = 'slug'
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context




class NewsCategory(ListView):
    model = News
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(categories__slug=self.kwargs['slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категорія: ' + str(context['posts'][0].categories)
        context['menu'] = menu
        context['categories_selected'] = context['posts'][0].categories_id
        return context

# def show_category(request, category_slug):
#     posts = News.objects.filter(categories__slug=category_slug)
#
#     #categories = Category.objects.all()
#
#     context = {
#              'posts': posts,
#              #'categories': categories,
#              #'menu': menu,
#              'title': 'Тема: ',
#              'categories_selected': category_slug,
#     }
#
#     return render(request, 'mainapp/index.html', context)
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
