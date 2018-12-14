#coding=gbk
# orm ���ѧϰ
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
engine = create_engine("mysql+pymysql://root:""@localhost/studentdb",
                       encoding='utf-8', echo=False)  #echo=true ���ִ�е�sql ���

Base = declarative_base()  # ����orm����

class Student(Base):
    __tablename__ = 'student'  # ����
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "id:%s name%s"%(self.id,self.name)

class StudyRecord(Base):
    __tablename__="study_record"  # ����
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status=Column(String(32),nullable=False)
    student_id=Column(Integer,ForeignKey("student.id"))
    def __repr__(self):
        return "id:%s day%s name %s status %s"%(self.id,self.day,self.student.name,self.status)

    student = relationship("Student", backref="my_study_record")  # ���nb����������Student����ͨ��backref�ֶη�������������StudyRecord����Ĺ�����

Base.metadata.create_all(engine)  # ������ṹ


# ��ʼ��������
Session_class = sessionmaker(bind=engine)  # ���������ݿ�ĻỰsession class ,ע��,���ﷵ�ظ�session���Ǹ�class,����ʵ��
session = Session_class()  # ����sessionʵ������������ɾ���

# Ҫ��������ݣ�ʾ������һ��������
# s1 = Student(name="alex", register_date="2014-01-01")  # ������Ҫ���������ݶ���
# s2 = Student(name="domain", register_date="2014-02-01")  # ������Ҫ���������ݶ���
# s3 = Student(name="huang", register_date="2015-01-01")  # ������Ҫ���������ݶ���
# s4 = Student(name="kong", register_date="2016-01-01")  # ������Ҫ���������ݶ���
# s5 = Student(name="alex", register_date="2017-01-01")  # ������Ҫ���������ݶ���
#
r1 = StudyRecord(day="1",status="YES",student_id=1)  # ������Ҫ���������ݶ���
r2 = StudyRecord( day="1",status="NO",student_id=1)  # ������Ҫ���������ݶ���
# r3 = StudyRecord( day="1",status="NO",student_id=3)  # ������Ҫ���������ݶ���
#
# Session.add_all([s1,s2,s3,s4,s5,r1,r2,r3]) # �����ݶ���ӽ�Session
session.add_all([r1,r2]) # �����ݶ���ӽ�Session
#
# Session.commit() # �ύ

stu_obj=session.query(Student).filter(Student.name=="alex").first()

print(stu_obj.my_study_record)

session.commit() # �ύ