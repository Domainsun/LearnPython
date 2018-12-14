
#coding=gbk
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
# engine = create_engine("mysql+pymysql://root:""@localhost/domaindb",
#                        encoding='utf-8', echo=False)  #echo=true ���ִ�е�sql ���
engine = create_engine("mysql+pymysql://root:domain123@139.199.81.219/test",
                       encoding='utf-8', echo=False)  #echo=true ���ִ�е�sql ���

Base = declarative_base()  # ����orm����


class User(Base):
    __tablename__ = 'user'  # ����
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


    def __repr__(self):
        return "id:%s  name:%s"%(self.id,self.name)


Base.metadata.create_all(engine)  # ������ṹ

# ��ʼ��������
Session_class = sessionmaker(bind=engine)  # ���������ݿ�ĻỰsession class ,ע��,���ﷵ�ظ�session���Ǹ�class,����ʵ��
Session = Session_class()  # ����sessionʵ��

# user_obj = User(name="alex", password="alex3714")  # ������Ҫ���������ݶ���
# user_obj1 = User(name="domain", password="123456")  # ������Ҫ���������ݶ���
# print(user_obj.name, user_obj.id)  # ��ʱ��û���������أ��������ӡһ��id���ֻ���None
#
# Session.add(user_obj)  # ��Ҫ���������ݶ�����ӵ����session� һ��ͳһ����
# Session.add(user_obj1)  # ��Ҫ���������ݶ�����ӵ����session� һ��ͳһ����
# print(user_obj.name, user_obj.id)  # ��ʱҲ��Ȼ��û����

# Session.commit()  # �ִ˲�ͳһ�ύ����������



# ��ʼ��ɾ�Ĳ�
# ��
# data= Session.query(User).filter_by().all()  #��ѯ����
# data= Session.query(User).filter(User.id>1).filter(User.id<3).all() # ������ѯ filter ��������

# ��
# data= Session.query(User).filter(User.id>1).filter(User.id<10).first() # ������ѯ ��ȡ����һ����Ȼ������ֱ�Ӹ������� ���ĺ�commit
# data.name="aaa"
# data.password="111"
# Session.commit()
#
# # ɾ
# data= Session.query(User).filter(User.id>1).filter(User.id<20).first() # ������ѯ ��ȡ����һ����Ȼ������ֱ�Ӹ������� ���ĺ�commit
# Session.delete(data)
# Session.commit()
#
# # �ع�
#
# fake_user = User(name='Rain', password='12345')  #����һ��
# Session.add(fake_user)  #��ӵ�������
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # ��ʱ��session���������Ӻ��޸ĵ�����
# Session.rollback()  # ��ʱ��rollbackһ��
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # �ٲ�ͷ��ָղ���ӵ�����û���ˡ�
#
# # ͳ��
# data=Session.query(User).filter(User.name.like("do%")).count()
# print(data)
#
# # ����
# from sqlalchemy import func
# data=Session.query(func.count(User.name),User.name).group_by(User.name).all()
# print(data)


#---------------���---------------


def add_user(name,password):
    user= Session.query(User).filter(User.name==name).all() # ������ѯ filter ��������
    print(user)
    if user:
        return '�Ѿ�ע���'
    user_obj = User(name=name, password=password)  # ������Ҫ���������ݶ���
    Session.add(user_obj)  # ��Ҫ���������ݶ�����ӵ����session� һ��ͳһ����
    Session.commit()  # �ִ˲�ͳһ�ύ����������
    return None

def query_user(name,password):
    user= Session.query(User).filter(User.name==name).first() # ������ѯ filter ��������
    print(user)
    if user:
      if user.password!=password:
        return '�������'
      else:
          return None
    else:
        return '�û�û��ע�ᣬ����ע�ᣡ'



