from django import template

register = template.Library()


@register.simple_tag
def total_price(price, count):
    sum1 = int(price) * int(count)
    return sum1
