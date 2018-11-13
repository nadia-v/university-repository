"""
Nadia Vedeneyeva
Homework 10
Majors
""" 

import sys
import os
from prettytable import PrettyTable
from collections import defaultdict
from HW08_part2_Nadia_Vedeneyeva import file_reader
import unittest 


class Student():
    """Class Student"""

    #Lables for student table
    pt_lables = ['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Courses', 'Remainin Electives']    

    def __init__(self, s_cwid, name, dept, major):
    
        self.s_cwid = s_cwid
        self.name = name 
        self.dept = dept 
        self.major = major      
        self.courses = dict()   #courses[course] = grades
        

    def add_courses(self, course, grade):
        """Function adds an element to student courses dictionary
        with key=course and volue=grade"""
        self.courses[course] = grade


    def pt_row(self):
        """Function adds a row to student PrettyTable"""
        completed_courses, remaining_req, remaining_elect = self.major.grade_check(self.courses)

        completed_courses = None if completed_courses == None else sorted(completed_courses)
        remaining_req = None if remaining_req == None else sorted(remaining_req)
        remaining_elect = None if remaining_elect == None else sorted(remaining_elect)

        return [self.s_cwid, self.name, self.dept, completed_courses, remaining_req, remaining_elect]

   
class Instructor():
    """Class Instructor"""

    #Lables for instructor table
    pt_lables = ['CWID', 'Name', 'Department', 'Courses', 'Students']   

    def __init__(self, i_cwid, name, dept):
    
        self.i_cwid = i_cwid
        self.name = name 
        self.dept = dept
        self.courses = defaultdict(int)     #courses[course] = number of students


    def add_courses(self, course):
        """Function adds elements to instructor courses default dictionary
        with key=course and count=number of students in the class"""
        self.courses[course] += 1

    def pt_row(self):
        """Function creates a row for instructor table"""
        for course, students in self.courses.items():
            yield [self.i_cwid, self.name, self.dept, course, students]
    

class Major():
    """Class Major"""

    #Lables for major table
    pt_lables = ['Department', 'Required', 'Electives']

    def __init__(self, dept):
        self.dept = dept  
        self.req = set()
        self.elect = set()
        self.passing_grades = {'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C'}

    def add_course(self, flag, courses):
        """Function separates required courses from elective courses depending on the flag"""
        if flag == 'E':
            self.elect.add(courses)
        elif flag == 'R':
            self.req.add(courses)
        else:
            raise ValueError(f'An unexpected flag {flag} was found in majors.txt')


    def grade_check(self, courses):
        """Function returns completed courses, remaining required courses and remaining elective
        courses from dict[course] = grade for a single student"""

        completed_courses = {course for course, grade in courses.items() if grade in self.passing_grades}
        remaining_req = self.req - completed_courses
        if self.elect.intersection(completed_courses):
            remaining_elect = None
        else:
            remaining_elect = self.elect

        return completed_courses, remaining_req, remaining_elect

    def pt_row(self):
        """Function creates a row for major table"""
        return [self.dept, sorted(self.req), sorted(self.elect)]


class Repository():
    """Class University repository"""

    def __init__(self, directory):
       
        self.directory = directory
        self.students = dict()   #student[cwid] = instance of class student
        self.instructors = dict()    #instructor[cwid] = instance of class instructor
        self.grades = list()  #a list of all grades
        self.majors = dict()  #major[dept] = instance of class major
            
        self.read_majors_file(os.path.join(directory, 'majors.txt'))   
        self.read_student_file(os.path.join(directory, 'students.txt'))             
        self.read_instructors_file(os.path.join(directory, 'instructors.txt'))
        self.read_grades_file(os.path.join(directory, 'grades.txt'))   


     
    def read_student_file(self, path):
        """Function reads student file"""
        try:
            for s_cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
                if s_cwid in self.students:
                    print(f'CWID {s_cwid} alerady exist')
                else:
                    self.students[s_cwid] = Student(s_cwid, name, dept, self.majors[dept])
        except ValueError as e: 
            print(e)   


    def read_instructors_file(self, path):
        """Function reads instructor"""
        try:
            for i_cwid, name, dept in file_reader(path, 3, sep='\t', header=False):
                if i_cwid in self.instructors:
                    print(f'CWID {i_cwid} already exist')
                else:
                    self.instructors[i_cwid] = Instructor(i_cwid, name, dept)
        except ValueError as e:
            print(e)   


    def read_grades_file(self, path):
        """Function reads grades file"""
        try:
            for s_cwid, course, grade, i_cwid in file_reader(path, 4, sep='\t', header=False):
                if s_cwid in self.students:
                    self.students[s_cwid].add_courses(course, grade)
                else:
                    print(f'Student cwid {s_cwid} is not in database')
                if i_cwid in self.instructors:
                    self.instructors[i_cwid].add_courses(course)
                else:
                    print(f'Instructor cwid {i_cwid} is not in database')
        except ValueError as e:
            print(e)


    def read_majors_file(self, path):
        """FUnction reads majors file"""

        try:
            for dept, flag, courses in file_reader(path, 3, sep='\t', header=False): 
                if dept not in self.majors:
                    self.majors[dept] = Major(dept)
                self.majors[dept].add_course(flag, courses)
        except ValueError as e:
            print(e)
                    
         

    def student_prettytable(self):
        """Function prints students table"""
        pt = PrettyTable(field_names=Student.pt_lables)
        for student in self.students.values():
            pt.add_row(student.pt_row())
        print(pt)

    def instructor_prettytable(self):
        """Function prints instructors table"""
        pt = PrettyTable(field_names=Instructor.pt_lables)
        for instructor in self.instructors.values():
            for row in instructor.pt_row():
                pt.add_row(row)
                
        print(pt) 

    def major_prettytable(self):
        """Function prints majors table"""
        pt = PrettyTable(field_names=Major.pt_lables)
        for dept in self.majors.values():
            pt.add_row(dept.pt_row())
        print(pt)
     
  
def main():
    """Main function"""

    directory = '/Users/nadik/Desktop/801/homework/repository'
    
    repo = Repository(directory)
    repo.major_prettytable()
    repo.student_prettytable()
    repo.instructor_prettytable()


if __name__ == "__main__":
    main()


