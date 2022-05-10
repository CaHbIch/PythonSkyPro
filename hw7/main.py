from function import *

pk = int(input('Введите номер студента\n'))

print(get_student_by_pk(pk))
for students in load_students():
    if students['pk'] == pk:
        print(f'Выберите специальность для оценки студента {students["full_name"]}\n')

profession = str(input())

print(check_fitness(pk, profession))
