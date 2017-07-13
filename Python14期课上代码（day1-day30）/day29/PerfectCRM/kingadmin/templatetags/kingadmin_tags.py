
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def get_model_verbose_name(model_obj):

    model_name = model_obj._meta.verbose_name if model_obj._meta.verbose_name else model_obj._meta.verbose_name_plural

    if not model_name:
        model_name = model_obj._meta.model_name

    print("model obj",model_obj)
    return model_name

@register.simple_tag
def get_model_name(model_obj):

    return model_obj._meta.model_name

@register.simple_tag
def get_app_name(model_obj):

    return model_obj._meta.app_label



@register.simple_tag
def build_table_row(admin_obj,obj):

    row_ele = ""

    for column in admin_obj.list_display:
        column_obj = obj._meta.get_field(column)
        if column_obj.choices:
            get_column_data = getattr(obj,"get_%s_display" % column)
            column_data = get_column_data()
        else:
            column_data = getattr(obj, column)

        td_ele = '''<td>%s</td>''' % column_data
        row_ele += td_ele

    return mark_safe(row_ele)