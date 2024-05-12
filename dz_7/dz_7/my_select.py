from sqlalchemy import select, func, desc
from connect_db import session
from models import m2m, Groups, Students, Subjects, Teachers, Evaluations

def select_1():
    q = session.query(Students.student, func.max(func.avg(Evaluations.evaluation), 2).label('avg_grade'))\
        .select_from(Evaluations).join(Students).group_by(Students.id).order_by(desc('avg_grade')).limit(5).all()
    print(q)

def select_2():
    q = session.query(Students.student, func.max(func.avg(Evaluations.evaluation), 2).label('avg_grade'),  Subjects.subject)\
        .select_from(Evaluations).join(Students)\
            .join(Subjects).where(Subjects.subject.like('physics')).group_by(Students.id).order_by(desc('avg_grade')).limit(1).all()
    print(q)

def select_3():
    q = session.query(Students.student_id, func.max(func.avg(Evaluations.evaluation), 2).label('avg_grade'), Evaluations.subject)\
        .select_from(Students).join(Evaluations).where(Evaluations.subject.like('chemistry')).group_by(Students.student_id).order_by(desc('avg_grade')).all()
    print(q)

def select_4():
    q = session.query(func.round(func.avg(Evaluations.evaluation), 2).label('avg_grade'))\
            .select_from(Evaluations).all()
    print(q)

def select_5():
    q = session.query(Subjects.subject, Subjects.subject_id)\
            .select_from(Subjects).all()
    print(q)

def select_6():
    q = session.query(Students.student_id.label("group_number"), Students.student)\
            .select_from(Students).where(Students.student_id.like('3')).all()
    print(q)

def select_7():
    q = session.query(Students.student_id.label("group_number"), Students.student, Evaluations.evaluation, Evaluations.subject)\
            .select_from(Students).join(Evaluations).where(Evaluations.subject.like('chemistry')).where(Students.student_id.like('1')).all()
    print(q)

def select_8():
    q = session.query(Subjects.subject_id.label("teacher"),Subjects.subject, func.max(func.avg(Evaluations.evaluation), 2).label('avg_grade'))\
            .select_from(Subjects).join(Evaluations).group_by(Subjects.id).all()
    print(q)

def select_9():
    q = session.query(Subjects.subject_id.label("teacher"), Evaluations.student, Subjects.subject)\
            .select_from(Subjects).join(Evaluations).where(Evaluations.student.like('Raymond French')).group_by(Subjects.id).all()
    print(q)

if __name__ == '__main__':
    
    select_9()