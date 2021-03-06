
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
def print_obj(obj):
    print("DEBUG:::",obj)
    print("DEBUG:::",dir(obj))


@register.simple_tag
def build_table_row(admin_obj,obj):

    row_ele = ""
    if admin_obj.list_display:
        for index,column in enumerate(admin_obj.list_display):
            column_obj = obj._meta.get_field(column)


            if column_obj.choices:
                get_column_data = getattr(obj,"get_%s_display" % column)
                column_data = get_column_data()
            else:
                column_data = getattr(obj, column)
            if index == 0: #首列
                td_ele = '''<td><a href="/kingadmin/{app_name}/{model_name}/{obj_id}/change/">{column_data}</a> </td>'''\
                            .format(app_name=admin_obj.model._meta.app_label,
                                    model_name=admin_obj.model._meta.model_name,
                                    obj_id=obj.id,column_data=column_data)
            else:
                td_ele = '''<td>%s</td>''' % column_data


            row_ele += td_ele
    else:
        row_ele += "<td>%s</td>" % obj
    return mark_safe(row_ele)



@register.simple_tag
def get_filter_field (filter_column,admin_obj):
    print("admin obj",admin_obj.model ,filter_column)

    field_obj = admin_obj.model._meta.get_field(filter_column)
    select_ele = """<select name="%s"> """ %filter_column
    for choice in field_obj.get_choices():
        selected_condtion = admin_obj.filter_condtions.get(filter_column)
        if selected_condtion != None: #if None, 没有过滤这个条件
            print("heoe....",filter_column,selected_condtion,type(selected_condtion))
            if selected_condtion == str(choice[0]): #就是选择的这个条件
                selected = "selected"
            else:
                selected = ""

        else:
            selected = ""

        option_ele = """<option value="%s" %s>%s</option> """ % (choice[0],selected,choice[1])

        select_ele +=option_ele

    select_ele += "</select>"

    return mark_safe(select_ele)


@register.simple_tag
def generate_filter_url(admin_obj):
    url = ''
    for k,v in admin_obj.filter_condtions.items():
        url += "&%s=%s" %(k,v )

    return url


@register.simple_tag
def  get_orderby_key(request,column):
    current_order_by_key = request.GET.get("_o")
    if current_order_by_key != None: #肯定有某列被排序了
        if current_order_by_key ==  column: # 当前这列正在被排序
            if column.startswith("-"):
                return column.strip("-")
            else:
                return "-%s"%column


    return column

@register.simple_tag
def get_current_orderby_key(request):
    #获取当前正在排序的字段名
    current_order_by_key = request.GET.get("_o")
    return current_order_by_key
    #if current_order_by_key != None: #肯定有某列被排序了

@register.simple_tag
def generate_order_by_url (request):
    current_order_by_key = request.GET.get("_o")
    if current_order_by_key != None:  # 肯定有某列被排序了
        return "&_o=%s" % current_order_by_key
    return ''


@register.simple_tag
def get_search_key(request):
    return request.GET.get("_q") or ''

@register.simple_tag
def display_order_by_icon(request, column):

    current_order_by_key = request.GET.get("_o")
    if current_order_by_key != None: #肯定有某列被排序了
        if current_order_by_key.strip("-") == column: ## 当前这列正在被排序


            if current_order_by_key.startswith("-"):
                icon = "fa-arrow-up"
            else:
                icon = "fa-arrow-down"
            ele = """<i class="fa %s" aria-hidden="true"></i>""" % icon
            return mark_safe(ele)
    return ''


@register.simple_tag
def get_admin_actions(admin_obj):

    options = "<option class='form-control' value='-1'>-------</option>"
    actions = admin_obj.default_actions + admin_obj.actions

    for action in actions:
        action_func = getattr(admin_obj,action)
        if hasattr(action_func,"short_description"):
            action_name = action_func.short_description
        else:
            action_name = action
        options += """<option value="{action_func_name}">{action_name}</option> """.format(action_func_name=action,
                                                                                           action_name=action_name)

    return mark_safe(options)
