
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum,DATE,Integer, String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://admin:admin@172.16.34.194/PC1db",
                       encoding='utf-8')

Base = declarative_base()  # 生成orm基类


class PC_Info(Base):
    __tablename__ = "PC_info"
    id = Column(Integer, primary_key=True)
    ip = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)
    HostModel = Column(String(32),nullable=False)
    Expire = Column(DATE,nullable=False)
    email = Column(String(64),nullable=False)
    operating_System = Column(String(32),nullable=False)
    MAC_address = Column(String(32),nullable=False)
    domain = Column(String(64),nullable=False)

    def __repr__(self):
        return "<id:%s, ip:%s, register_date:%s, HostModel:%s, Expire:%s,email:%s,operating_System:%s,MAC_address:%s,domain:%s>" \
               % (self.id, self.ip,self.register_date,self.HostModel,self.Expire,
                  self.email,self.operating_System,self.MAC_address,self.domain)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(32),nullable=False)
    pwd = Column(String(64), nullable=False)

    def __repr__(self):
        return "<id:%s, name:%s>" % (self.username, self.pwd)

Base.metadata.create_all(engine)  # 创建表结构



Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例 #cursor

s1 = PC_Info(ip="192.168.1.11",HostModel="Shanghai",register_date="2014-05-21",Expire="2024-05-21",
             email="123@126.com",operating_System="win10",MAC_address="00-50-56-C0-00-01",domain="www.baidu.com")
s2 = PC_Info(ip="192.168.1.10",HostModel="Beijing",register_date="2014-05-20",Expire="2024-05-20",
             email="234@126.com",operating_System="win10",MAC_address="00-50-56-C0-00-02",domain="www.sohu.com")
s3 = PC_Info(ip="192.168.1.9",HostModel="USA",register_date="2014-05-19",Expire="2024-05-19",
             email="345@126.com",operating_System="win10",MAC_address="00-50-56-C0-00-03",domain="www.163.com")

u1 = User(username="alex",pwd="123")
u2 = User(username="peiqi",pwd="234")
u3 = User(username="sy106",pwd="345")


session.add_all([s1,s2,s3,u1,u2,u3])

session.commit()

