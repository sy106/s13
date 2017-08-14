# Create your views here.

from django.shortcuts import redirect
from django.shortcuts import render
from sqlalchemy.orm import sessionmaker

from cmdb import orm

Session_class = sessionmaker(bind=orm.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例 #cursor

def login(request):
    # 包含用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    error_msg = ""
    if request.method == "POST":
        # 获取用户通过POST提交过来的数据
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        # user=request.POST['user']
        # pwd=request.POST['pwd']
        # console.log(v);
        print("==========1:",user,pwd)
        obj= session.query(orm.User).filter(orm.User.username == user).first()
        print ("========2:",obj.username,obj.pwd)
        if user ==obj.username and pwd == obj.pwd:
            # 去跳转到
            return redirect('/home')
        else:
            # 用户密码不配
            error_msg = "用户名或密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})



def home(request):
    USER_LIST=[]

    obj = session.query(orm.PC_Info).filter(orm.PC_Info.id!=None).all()
    print("============3",obj)
    for i in obj:
        temp1 = {'id': i.id, 'ip': i.ip, "register_date": i.register_date,"HostModel":i.HostModel,
                "Expire":i.Expire}
        print("===========4",i.id,i.ip)
        USER_LIST.append(temp1)
    print("=======5",USER_LIST)

    # if request.method == "POST":
    #     # 获取用户提交的数据 POST请求中
    #     d = request.POST.get('id')
    #     p = request.POST.get('ip')
    #     r = request.POST.get('register_date')
    #     h = request.POST.get('HostModel')
    #     e = request.POST.get('Expire')
    #     temp2 = {'id': d, 'ip': p, "register_date": r, "HostModel": h,
    #             "Expire": e}
    #     USER_LIST.append(temp2)
    return render(request, 'home.html', {'user_list': USER_LIST})

def detail(request):
    nid = request.GET.get("nid")
    print("===nid",nid)
    obj = session.query(orm.PC_Info).filter(orm.PC_Info.id == nid).first()
    USER_DETAIL = {'id': obj.id, 'ip': obj.ip, "register_date": obj.register_date, "HostModel": obj.HostModel,
             "Expire": obj.Expire,"email":obj.email,"operating_System":obj.operating_System,
             "MAC_address":obj.MAC_address,"domain":obj.domain}
    print("===USER_DETAIL",USER_DETAIL)
    return render(request, 'detail.html', {'user_list': USER_DETAIL})

def delete_host(request):
    print(request.method)
    nid = request.POST.get("nid")

    obj=session.query(orm.PC_Info).filter(orm.PC_Info.id == nid).first()
    print("test delete",obj)
    session.delete(obj)
    session.commit()
    return redirect('/home')

def add_host(request):
    print("addhost====",request.method)
    ip = request.POST.get("ip")
    register_date = request.POST.get("register_date")
    HostModel = request.POST.get("HostModel")
    Expire = request.POST.get("Expire")
    email = request.POST.get("email")
    operating_System = request.POST.get("operating_System")
    MAC_address = request.POST.get("MAC_address")
    domain = request.POST.get("domain")
    # User_list={ip,register_date,HostModel,Expire,email,operating_System,MAC_address,domain}
    # obj = session.query(orm.PC_Info).add(User_list)
    obj = orm.PC_Info(ip=ip, HostModel=HostModel, register_date=register_date, Expire=Expire,
                 email=email, operating_System=operating_System, MAC_address=MAC_address, domain=domain)
    print("add_host",obj)
    session.add_all([obj])
    session.commit()
    return redirect('/home')


