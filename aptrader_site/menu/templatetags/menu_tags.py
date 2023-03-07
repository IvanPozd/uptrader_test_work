from django import template
from django.urls import reverse, NoReverseMatch
from django.utils.safestring import mark_safe
from menu.models import MenuItem


register = template.Library()

def build_menu_tree(menu_items, current_url, context):
    """
    Рекурсивно создает древовидное меню на основе списка объектов MenuItem
    """
    #h1 = menu_items.first().title
    active_url = current_url.split('/')[1]
    menu_html = ""
    #menu_html += f"<h1>{active_url}</h1>"
    menu_html += '<ul>'
    for item in menu_items:
        active_class = "active" if active_url == item.url else ""
        if active_class == "active":
            menu_html += f'<li class="{active_class}"><a style="color: orange; font-size: 25px;" href="{item.url}">{item.title}</a>'
        else:
            menu_html += f'<li class="{active_class}"><a href="{item.url}">{item.title}</a>'
        if item.children.exists():
            menu_html += build_menu_tree(item.children.all(), current_url, context)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Шаблонный тег для вывода древовидного меню по его имени
    """
    current_url = context["request"].path
    menu_items = MenuItem.objects.filter(menu=menu_name)
    menu_html = build_menu_tree(menu_items, current_url, context)
    return mark_safe(menu_html)