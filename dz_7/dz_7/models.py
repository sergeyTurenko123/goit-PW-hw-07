from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

m2m = Table(
    "m2m",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("group", Integer, ForeignKey("groups.id", ondelete="CASCADE")),
    Column("subject", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
)

class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_number = Column(String(50), nullable=False)
    records = relationship("Students", cascade="all, delete", backref="group")

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student = Column(String(50), nullable=False)
    student_id = Column(Integer, ForeignKey(Groups.id, ondelete="CASCADE"))
    
class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=False)
    records = relationship("Teachers", cascade="all, delete", backref="subject")

class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Subjects.id, ondelete="CASCADE"))

class Evaluations(Base):
    __tablename__ = "evaluations"
    id = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey(Students.id, ondelete="CASCADE"))
    evaluation = Column(String(50), nullable=False)
    subject = Column(Integer, ForeignKey(Subjects.id, ondelete="CASCADE"))
    created = Column(DateTime, default=datetime.now())
