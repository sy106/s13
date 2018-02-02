from django.shortcuts import render,HttpResponse,redirect
from django.db import models

def login(request):
    # models.UserGroup.objects.create(caption='DBA')
    error_msg = ""
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 数据库中执行 select * from user where usernam='x' and password='x'
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # obj = models.UserInfo.objects.filter(username=u,password=p).first()
        # print(obj)# obj None,
        # count = models.UserInfo.objects.filter(username=u, password=p).count()
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            error_msg = "用户名或密码错误"
            return render(request, 'login.html',{'error_msg': error_msg})
    else:
        # PUT,DELETE,HEAD,OPTION...

        # 用户密码不配

        return redirect('/index/')


def index(request):
    return render(request, 'index.html')

def user_info(request,nid):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        obj = models.UserInfo.objects.filter(id=nid).first()
        group_list = models.UserGroup.objects.all()

        return render(request, 'user_info.html', {'user_list': user_list, "group_list": group_list,'obj': obj})

    elif request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        c = request.POST.get('group_id')
        models.UserInfo.objects.create(username=u,password=p,user_group_id=c)
        return redirect('/cmdb/user_info/')
        # user_list = models.UserInfo.objects.all()
        # return render(request, 'user_info.html', {'user_list': user_list})


def user_group(request):
    if request.method == "GET":

        group_list = models.UserGroup.objects.all()

        return render(request, 'user_group.html', {"group_list": group_list})
    elif request.method == 'POST':

        c = request.POST.get('caption')
        models.UserGroup.objects.create(caption=c)
        return redirect('/cmdb/user_group/')
        # user_list = models.UserInfo.objects.all()
        # return render(request, 'user_info.html', {'user_list': user_list})

def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # 去单挑数据，如果不存在，直接报错
    # models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})

def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')

def group_del(request, uid):
    models.UserGroup.objects.filter(uid=uid).delete()
    return redirect('/cmdb/user_group/')

def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_edit.html',{'obj': obj,"group_list": group_list})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        c = request.POST.get('group_id')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p,user_group_id=c)
        return redirect('/cmdb/user_info/')

def group_edit(request, uid):
    if request.method == "GET":
        group_list = models.UserGroup.objects.all()
        obj = models.UserGroup.objects.filter(uid=uid).first()
        return render(request, 'group_edit.html', {'obj': obj, "group_list": group_list})
    elif request.method == "POST":
        uid = request.POST.get('uid')#原来的UID
        c = request.POST.get('group_caption')#改动后的caption

        obj1=models.UserGroup.objects.filter(uid=uid).first()
        for item in models.UserGroup.objects.all():
            if c == item.caption:
                error_msg = "group 的名字重复！请重新编辑！"
                group_list = models.UserGroup.objects.all()
                obj = models.UserGroup.objects.filter(uid=uid).first()
                return render(request, 'group_edit.html',{'error_msg': error_msg,'obj': obj, "group_list": group_list})
        obj1.caption = c
        obj1.save()



        return redirect('/cmdb/user_group/')
from app01 import models
def orm(request):
    # 创建
    # models.UserInfo.objects.create(username='root',password='123')

    # dic = {'username': 'eric', 'password': '666'}
    # models.UserInfo.objects.create(**dic)

    # obj = models.UserInfo(username='alex',password='123')
    # obj.save()

    # 查
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='root',password='123')
    #
    # result,QuerySet => Django => []
    # [obj(id,username,password),obj(id,username,password), obj(id,username,password)]
    # for row in result:
    #     print(row.id,row.username,row.password)
    # print(result)

    # 删除
    # models.UserInfo.objects.filter(username="alex").delete()

    # 更新
    # models.UserInfo.objects.filter(id=3).update(password="69")


    # 一对多
    # user_list = models.UserInfo.objects.all()

    # models.UserInfo.objects.create(
    #     username='root1',
    #     password='123',
    #     email="asdfasdf",
    #     test="asdfasdf",
    #     user_group = models.UserGroup.objects.filter(id=1).first()
    # )
    models.UserInfo.objects.create(
        username='root1',
        password='123',
        email="asdfasdf",
        test="asdfasdf",
        user_group_id = 1
    )


    return HttpResponse('orm')







# def home(request):
#     return HttpResponse('Home')
from django.views import View
class Home(View):

    def dispatch(self, request, *args, **kwargs):
        # 调用父类中的dispatch
        print('before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self,request):
        print(request.method)
        return render(request, 'home.html')

    def post(self,request):
        print(request.method,'POST')
        return render(request, 'home.html')

