from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key):
    """Return the value of a dictionary key in templates."""
    return dictionary.get(str(key)) or dictionary.get(key)

@register.filter(name='multiply')
def multiply(value, arg):
    """Multiply two numbers safely."""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
