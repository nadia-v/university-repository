"""
Nadia Vedeneyeva
Homework 09
Repository
""" 

import sys
import os
from prettytable import PrettyTable
from collections import defaultdict
from HW08_part2_Nadia_Vedeneyeva import file_reader
import unittest 


class Student():
    """Class Student"""

    pt_lables = ['CWID', 'Name', 'Major', 'Courses']    #Header for studend PrettyTable

    def __init__(self, s_cwid, name, major):
    
        self.s_cwid = s_cwid
        self.name = name 
        self.major = major       
        self.courses = dict()   #courses[course] = grades
      

    def add_courses(self, course, grade):
        """Function adds an element to student courses dictionary
        with key=course and volue=grade"""
        self.courses[course] = grade


    def pt_row(self):
        """Function adds a row to student PrettyTable"""
        return [self.s_cwid, self.name, self.major, sorted(self.courses.keys())]

   
class Instructor():
    """Class Instructor"""

    pt_lables = ['CWID', 'Name', 'Department', 'Courses', 'Students']   #Header fo instructor PrettyTable

    def __init__(self, i_cwid, name, dept):
    
        self.i_cwid = i_cwid
        self.name = name 
        self.dept = dept
        self.courses = defaultdict(int)     #cources[course] = number of students


    def add_courses(self, course):
        """Function adds elements to instructor courses default dictionary
        with key=course and count=number of students in the class"""
        self.courses[course] += 1

    def pt_row(self):
        """Function creates a row for instructor table"""
        for course, students in self.courses.items():
            yield [self.i_cwid, self.name, self.dept, course, students]
    


class Repository():

    def __init__(self, directory):
       
        self.directory = directory
        self.students = dict()   #student[cwid] = instance of class student
        self.instructors = dict()    #instructor[cwid] = instance of class instructor
        self.grades = list()    #a list of all grades
            
        self.read_student_file(os.path.join(directory, 'students.txt'))             
        self.read_instructors_file(os.path.join(directory, 'instructors.txt'))
        self.read_grades_file(os.path.join(directory, 'grades.txt'))      


     
    def read_student_file(self, path):
        """Function reads student file"""
        try:
            for s_cwid, name, major in file_reader(path, 3, sep='\t', header=False):
                if s_cwid in self.students:
                    print(f'CWID {s_cwid} alerady exist')
                else:
                    self.students[s_cwid] = Student(s_cwid, name, major)
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
     
  
def main():
    """Main function"""

    directory = '/Users/nadik/Desktop/801/homework/repository'
    

    repo = Repository(directory)
    repo.student_prettytable()
    repo.instructor_prettytable()

main()


class Repository_Test(unittest.TestCase):
    """Class unittest"""

    def test_repository(self):
        """Testing reository class"""
       
        stevens = Repository('/Users/nadik/Desktop/801/homework/repository')
        student_details = [s.pt_row() for s in stevens.students.values()]
        instructor_details = [row for i in stevens.instructors.values() for row in i.pt_row()]
        student_expect = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
                 ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']], 
                 ['10172','Forbes, I', 'SFEN', ['SSW 555', 'SSW 567']], 
                 ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687']], 
                 ['10183', 'Chapman, O', 'SFEN', ['SSW 689']], 
                 ['11399', 'Cordova, I', 'SYEN', ['SSW 540']], 
                 ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800']], 
                 ['11658', 'Kelly, P', 'SYEN', ['SSW 540']], 
                 ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645']], 
                 ['11788', 'Fuller, E', 'SYEN', ['SSW 540']]]
        instructor_expect = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], 
                ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3],
                ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], 
                ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], 
                ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], 
                ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], 
                ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], 
                ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], 
                ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], 
                ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], 
                ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], 
                ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        self.assertEqual(student_details, student_expect)
        self.assertEqual(instructor_details, instructor_expect)
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)