from django import template


register = template.Library()


@register.inclusion_tag('tags/input.html')
def input_field(field, field_type='text'):

    return {
        'field': field,
        'field_type': field_type
    }
