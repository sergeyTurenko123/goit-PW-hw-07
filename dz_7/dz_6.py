from datetime import datetime
import faker
from random import randint, choice
import sqlite3

STUDENTS = 50
GROUPS = 3
TEACHERS = 3
SUBJECTS = 5
EVALUATIONS = 12


def generate_fake_data(students, groups, teachers, subjects, evaluations): #-> tuple():
    subjects = ("mathematics", "physics", "chemistry", "geography", "metallurgy")
    fake_students = []
    fake_groups = []
    fake_teachers = []
    fake_subjects = []
    fake_evaluations = []

    fake_data = faker.Faker()

    for _ in range(students):
        fake_students.append(fake_data.name())
    for i in range(1, groups+1):
        fake_groups.append(i)
    for _ in range(teachers):
        fake_teachers.append(fake_data.name())
    for i in subjects:
        fake_subjects.append(i)
    for i in range(1, evaluations+1):
        fake_evaluations.append(i)

    return fake_students, fake_groups, fake_teachers, fake_subjects, fake_evaluations

def prepare_data(students, groups, teachers, subjects, evaluations): #-> tuple():
    
    for_students = []  
    for student in students:
        for_students.append((student, randint(1, GROUPS)))

    for_groups = []
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher, ))
    
    for_subjects = []
    for subject in subjects:
        for_subjects.append((subject, choice(teachers)))
    
    for_evaluations = []
    for student in students:
        for list in range(1, 21):
            #for evaluation in evaluations:
            for_evaluations.append((student, choice(subjects), randint(1, EVALUATIONS), datetime(2021, randint(1, 12), randint(1, 25)).date().strftime("%d-%m-%Y")))

    return for_students, for_groups, for_teachers, for_subjects, for_evaluations

def insert_data_to_db(students, groups, teachers, subjects, evaluations) -> None:
    
    with sqlite3.connect('./salary.db') as con:

        cur = con.cursor()

        sql_to_students = """INSERT INTO students(student, student_id) VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)
        
        sql_to_groups = """INSERT INTO groups(group_number) VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(teacher)
                              VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject, subject_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_evaluations = """INSERT INTO evaluations(student, subject, evaluation, created_at) VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_evaluations, evaluations)

        con.commit()


if __name__ == "__main__":
    students, groups, teachers, subjects, evaluations = prepare_data(*generate_fake_data(STUDENTS, GROUPS, TEACHERS, SUBJECTS, EVALUATIONS))
    insert_data_to_db(students, groups, teachers, subjects, evaluations)
    #print (evaluations)