from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def calcular_clase(tipo_mensage):
    if tipo_mensage == 'error':
        return 'danger'
    return tipo_mensage