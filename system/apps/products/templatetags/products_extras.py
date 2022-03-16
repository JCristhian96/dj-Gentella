from django import template

register = template.Library()


# Funcion para dar formato a el precio
@register.filter()
def price_format(value):
    return 'S/. {0:.2f}'.format(value)