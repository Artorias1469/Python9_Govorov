#!/usr/bin/env python3
# -*- coding: utf-8 -*-

school = {}

while True:
    class_name = input("Введите название класса (или 'exit' для завершения): ")

    if class_name.lower() == 'exit':
        break

    students_count = int(input("Введите количество учащихся в классе {}: ".format(class_name)))

    school[class_name] = students_count

print("Исходный словарь с данными по школе:", school)

class_to_change = input("Введите название класса, в котором изменилось количество учащихся: ")
new_student_count = int(input("Введите новое количество учащихся в классе {}: ".format(class_to_change)))
school[class_to_change] = new_student_count

new_class = input("Введите название нового класса: ")
new_class_count = int(input("Введите количество учащихся в новом классе {}: ".format(new_class)))
school[new_class] = new_class_count

class_to_remove = input("Введите название класса, который был расформирован: ")
del school[class_to_remove]

total_students = sum(school.values())

print("Измененный словарь с данными по школе:", school)
print("Общее количество учащихся в школе:", total_students)
