from django.db.models import Count

from .models import *

menu = [
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Create Blog', 'url_name': 'add_page'},
    {'title': 'Develop', 'url_name': 'dev_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Register', 'url_name': 'register'}
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.annotate(Count('news'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop(1)

        context['menu'] = user_menu

        context['categories'] = categories
        if 'categories_selected' not in context:
            context['categories_selected'] = 0
        return context

