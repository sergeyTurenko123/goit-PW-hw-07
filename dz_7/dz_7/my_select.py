from sqlalchemy import select, func, desc
from connect_db import session
from models import m2m, Groups, Students, Subjects, Teachers, Evaluations

# def select_1():
    


if __name__ == '__main__':
    
    q = session.query(Students.student,
    func.round(func.avg(Evaluations.evaluation), 2).label('avg_grade'))\
    .select_from(Evaluations).join(Students).group_by(Students.id).order_by(desc('avg_grade')).limit(5).all()
    print(q)
