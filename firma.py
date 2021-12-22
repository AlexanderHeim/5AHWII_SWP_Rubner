#!/usr/bin/env python3
from enum import Enum
class Gender(Enum):
    MALE = 1
    FEMALE = 2

    def __str__(self):
        if self == Gender.MALE:
            return "male"
        else:
            return "female"

class Person:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def __str__(self):
        return "Person: " + self.first_name + " " + self.last_name + " " + str(self.gender)

class Employee(Person):
    def __str__(self):
        return "Employee: " + self.first_name + " " + self.last_name + " " + str(self.gender)


class Groupleader(Employee):
    def __str__(self):
        return "Groupleader: " + self.first_name + " " + self.last_name + " " + str(self.gender)


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    
    def add_employee(employee):
        self.employees.append(employee)

    def __len__(self):
        return len(self.employees)

    def __str__(self):
        return "Department: " + self.name + "\n----" + "\n----".join(str(x) for x in self.employees)

class Company:
    def __init__(self, departments):
        self.departments = departments
    
    def __str__(self):
        return "Company:\n--" + "\n--".join(str(x) for x in self.departments)

    def count_members(self):
        count = 0
        for department in self.departments:
            count += len(department.employees)
        return count
    
    def count_groupleaders(self):
        count = 0
        for department in self.departments:
            group_leaders = [leader for leader in department.employees if type(leader) is Groupleader]
            count += len(group_leaders)
        return count
    
    def male_female_ratio(self):
        count_males = 0
        count_females = 0
        for department in self.departments:
            males = [male for male in department.employees if male.gender == Gender.MALE]
            females = [female for female in department.employees if female.gender == Gender.FEMALE]
            count_males += len(males)
            count_females += len(females)
        return count_males/count_females*100

    def largest_department(self):
        return max(self.departments, key=len)

x = Groupleader("Test", "Test", Gender.MALE)
y = Groupleader("Test2", "Test2", Gender.FEMALE)
c = Groupleader("Test2", "Test2", Gender.FEMALE)
z = Department("test", [x, y, c])
a = Company([z])
print(x)
print(y)
print(a.largest_department())
