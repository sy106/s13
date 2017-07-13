from django.shortcuts import render

from django import conf

# Create your views here.
#print("dj conf:",conf.settings)



from kingadmin import app_config
from kingadmin import base_admin


def app_index(request):

    # for app in conf.settings.INSTALLED_APPS:
    #     print(app)
    print("registered_sites",base_admin.site.registered_sites)
    return render(request, 'kingadmin/app_index.html',{"site":base_admin.site})


def table_data_list(request,app_name,model_name):

    admin_obj = base_admin.site.registered_sites[app_name][model_name]
    admin_obj.querysets =  admin_obj.model.objects.all()

    return render(request,"kingadmin/table_data_list.html",locals())


