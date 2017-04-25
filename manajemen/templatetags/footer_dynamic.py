from django import template

from public.models import SettingsVariable

register = template.Library()

@register.simple_tag
def email_footer():
    return SettingsVariable.objects.get(key='email').value

@register.simple_tag
def call1_footer():
    return SettingsVariable.objects.get(key='phone1').value

@register.assignment_tag
def call2_footer():
    phone2 = SettingsVariable.objects.get(key='phone2').value
    if phone2 == '': phone2=None
    return SettingsVariable.objects.get(key='phone2').value


@register.simple_tag
def address_footer():
    return SettingsVariable.objects.get(key='address').value
