from django import template
from menu.models import *

register = template.Library()


@register.inclusion_tag('menu/list_menu.html')
def draw_menu(cat_selected=None):
    categories = Category.objects.all()
    return {'categories': categories, 'cat_selected': cat_selected}


@register.inclusion_tag('menu/list_products.html')
def draw_products(cat_selected=None):
    category = Category.objects.get(slug=cat_selected)
    products = Product.objects.filter(category=category)
    return {'products': products, 'cat_selected': cat_selected}
