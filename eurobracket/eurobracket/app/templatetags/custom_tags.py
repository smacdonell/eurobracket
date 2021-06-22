from django import template


register = template.Library()


@register.inclusion_tag('tags/input.html')
def input_field(form, field, field_type='text', show_label=False):

    return {
        'form': form,
        'field': field,
        'field_type': field_type,
        'show_label': show_label
    }
