#coding=gbk
# orm 外键学习
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
engine = create_engine("mysql+pymysql://root:""@localhost/studentdb",
                       encoding='utf-8', echo=False)  #echo=true 输出执行的sql 语句

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "id:%s name%s"%(self.id,self.name)

class StudyRecord(Base):
    __tablename__="study_record"  # 表名
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status=Column(String(32),nullable=False)
    student_id=Column(Integer,ForeignKey("student.id"))
    def __repr__(self):
        return "id:%s day%s name %s status %s"%(self.id,self.day,self.student.name,self.status)

    student = relationship("Student", backref="my_study_record")  # 这个nb，允许你在Student表里通过backref字段反向查出所有它在StudyRecord表里的关联项

Base.metadata.create_all(engine)  # 创建表结构


# 开始插入数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例，用它做增删查改

# 要插入的数据，示例化出一个个对象
# s1 = Student(name="alex", register_date="2014-01-01")  # 生成你要创建的数据对象
# s2 = Student(name="domain", register_date="2014-02-01")  # 生成你要创建的数据对象
# s3 = Student(name="huang", register_date="2015-01-01")  # 生成你要创建的数据对象
# s4 = Student(name="kong", register_date="2016-01-01")  # 生成你要创建的数据对象
# s5 = Student(name="alex", register_date="2017-01-01")  # 生成你要创建的数据对象
#
r1 = StudyRecord(day="1",status="YES",student_id=1)  # 生成你要创建的数据对象
r2 = StudyRecord( day="1",status="NO",student_id=1)  # 生成你要创建的数据对象
# r3 = StudyRecord( day="1",status="NO",student_id=3)  # 生成你要创建的数据对象
#
# Session.add_all([s1,s2,s3,s4,s5,r1,r2,r3]) # 把数据都添加进Session
session.add_all([r1,r2]) # 把数据都添加进Session
#
# Session.commit() # 提交

stu_obj=session.query(Student).filter(Student.name=="alex").first()

print(stu_obj.my_study_record)

session.commit() # 提交