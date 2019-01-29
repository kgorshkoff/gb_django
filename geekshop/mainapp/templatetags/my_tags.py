from django import template

register = template.Library()


def allcaps(text):
    result = text.upper()
    return result


register.filter('allcaps', allcaps)
