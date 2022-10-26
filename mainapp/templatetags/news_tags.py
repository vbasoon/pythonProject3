from django import template
from mainapp.models import *

register = template.Library()


@register.simple_tag(name="getcategories")
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('mainapp/list_categories.html')
def show_categories(sort=None, categories_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)
    return {"categories": categories, "categories_selected": categories_selected}
