from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login

import calendar
from calendar import HTMLCalendar, TextCalendar, LocaleHTMLCalendar
from datetime import datetime


from .models import *
from .forms import *
from .utils import *


class NewsHome(DataMixin, ListView):
    # paginate_by = 3
    model = News
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Головна сторінка'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Головна сторінка")
        return dict(list(context.items()) + list(c_def.items()))
        # context['menu'] = menu
        # context['title'] = 'Головна сторінка'
        # context['categories_selected'] = 0

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('categories')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddNewsForm
    template_name = 'mainapp/addpage.html'
    success_url = reverse_lazy('home')
    # login_url = '/admin/'
    login_url = reverse_lazy('home')
    raise_exception = True
    #context_object_name = 'posts'
    # extra_context = {'title': 'Головна сторінка'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Додати новину")
        return dict(list(context.items()) + list(c_def.items()))


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


@login_required
def develop(request):
    develop_list = News.objects.all()
    paginator = Paginator(develop_list, 7)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'mainapp/develop.html', {'page_obj': page_obj, 'menu': menu, 'title': 'Новини розробки'})

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


# def contact(request):
#     return HttpResponse('Контакти')

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'mainapp/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Feedback")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

# def login(request):
#     return HttpResponse('Логін')


# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Ви зареєстровані!')
#             return redirect('login')
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#     else:
#         form = UserCreationForm()
#     return render(request, "mainapp/register.html", {'form': form, 'title': "Реєстрація"})


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


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'mainapp/post.html'
    slug_url_kwargs = 'slug'
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class NewsCategory(DataMixin, ListView):
    # paginate_by = 3
    model = News
    template_name = 'mainapp/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(categories__slug=self.kwargs['slug'], is_published=True).select_related('categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['slug'])
        c_def = self.get_user_context(title='Категорія - ' + str(c.name),
                                      categories_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))
        # context['title'] = 'Категорія: ' + str(context['posts'][0].categories)
        # context['menu'] = menu
        # context['categories_selected'] = context['posts'][0].categories_id
        # return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Реєстрація")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class loginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизація")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def archive(request, year, month):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # Create a Calendar
    cal = LocaleHTMLCalendar(locale='uk_UA.utf8').formatmonth(year, month_number)

    # Get current year
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    # Get current time
    current_time = now.strftime('%H:%M %p')

    contest = {
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "current_month": current_month,
        "current_day": current_day,
        "current_time": current_time,
    }

    return render(request, 'mainapp/archive.html', contest)
