from django import template

register = template.Library()


@register.filter(name='mod')
def mod(value, arg):
    return value % arg
