"""
Nadia Vedeneyeva
Repository tests
"""

import unittest
from HW10_Nadia_Vedeneyeva import Repository



class Repository_Test(unittest.TestCase):
    """Class unittest"""

    def test_student(self):
        """Testing Student class"""
       
        stevens = Repository('/Users/nadik/Desktop/801/homework/repository')
        student_details = [s.pt_row() for s in stevens.students.values()]
        student_expect = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], None],
                 ['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], None], 
                 ['10172','Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545']], 
                 ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545']], 
                 ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']], 
                 ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], None], 
                 ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810']], 
                 ['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']], 
                 ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']], 
                 ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], None]]

        self.assertEqual(student_details, student_expect)


    def test_instructor(self):
        """Testing Instructor class"""

        stevens = Repository('/Users/nadik/Desktop/801/homework/repository')       
        instructor_details = [row for i in stevens.instructors.values() for row in i.pt_row()]
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

        self.assertEqual(instructor_details, instructor_expect)


    def test_major(self):
        """Testing Major class"""

        stevens = Repository('/Users/nadik/Desktop/801/homework/repository')
        major_details = [s.pt_row() for s in stevens.majors.values()]
        major_expect = [['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]

        self.assertEqual(major_details, major_expect)
            

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=1)