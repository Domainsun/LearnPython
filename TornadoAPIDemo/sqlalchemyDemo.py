
#coding=gbk
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# engine = create_engine("mysql+pymysql://root:""@localhost/domaindb",
#                        encoding='utf-8', echo=False)  #echo=true 输出执行的sql 语句
engine = create_engine("mysql+pymysql://root:domain123@139.199.81.219/test",
                       encoding='utf-8', echo=False)  #echo=true 输出执行的sql 语句

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


    def __repr__(self):
        return "id:%s  name:%s"%(self.id,self.name)


Base.metadata.create_all(engine)  # 创建表结构

# 开始插入数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
# user_obj1 = User(name="domain", password="123456")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj1)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建

# Session.commit()  # 现此才统一提交，创建数据



# 开始增删改查
# 查
# data= Session.query(User).filter_by().all()  #查询所有
# data= Session.query(User).filter(User.id>1).filter(User.id<3).all() # 条件查询 filter 增加条件

# 改
# data= Session.query(User).filter(User.id>1).filter(User.id<10).first() # 条件查询 获取到第一个，然后下面直接辅助更改 更改后commit
# data.name="aaa"
# data.password="111"
# Session.commit()
#
# # 删
# data= Session.query(User).filter(User.id>1).filter(User.id<20).first() # 条件查询 获取到第一个，然后下面直接辅助更改 更改后commit
# Session.delete(data)
# Session.commit()
#
# # 回滚
#
# fake_user = User(name='Rain', password='12345')  #生成一项
# Session.add(fake_user)  #添加到表里面
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
# Session.rollback()  # 此时你rollback一下
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。
#
# # 统计
# data=Session.query(User).filter(User.name.like("do%")).count()
# print(data)
#
# # 分组
# from sqlalchemy import func
# data=Session.query(func.count(User.name),User.name).group_by(User.name).all()
# print(data)


#---------------外键---------------


def add_user(name,password):
    user= Session.query(User).filter(User.name==name).all() # 条件查询 filter 增加条件
    print(user)
    if user:
        return '已经注册过'
    user_obj = User(name=name, password=password)  # 生成你要创建的数据对象
    Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
    Session.commit()  # 现此才统一提交，创建数据
    return None

def query_user(name,password):
    user= Session.query(User).filter(User.name==name).first() # 条件查询 filter 增加条件
    print(user)
    if user:
      if user.password!=password:
        return '密码错误！'
      else:
          return None
    else:
        return '用户没有注册，请先注册！'



