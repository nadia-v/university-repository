"""
Nadia Vedeneyeva
Homework 08 (part 2)
Field separated file reader
"""


import os
import sys
import unittest

file_name = '/Users/nadik/Desktop/540/python/try.txt'
num_fields = 3


def file_reader(file_name, num_fields, sep=',', header=False):
    """A generator opens a file, checks for header, ignores it if there is one,
    checks for the number of elements in a line, 
    if number of elements matches the number of fields it returns a tuple of the elements"""
    
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(file_name, 'does not exist')  #File does not exist exception
    
    size = os.path.getsize(file_name)
    if size == 0:
        print(file_name, 'is an empty file')    #Instance of an empty file
        sys.exit()

    else:
        with file:
            for line_num, line in enumerate(file, 1): 
                if header is True and line_num == 1:   #Checking for header                              
                    continue
            
                line = line.rstrip().split(sep)     #Split the line on separators
                if len(line) == num_fields: 
                                            
                    yield tuple(line)

                else:
                    raise ValueError(f"Number of elements doesn't match number of fields on line {line_num}")



class Test_File_Reader(unittest.TestCase):
    """Class unittest"""

    def test_file_reader(self):
        """Testing function file_reader"""

        file_name = '/Users/nadik/Desktop/540/python/part2test.txt'
        expect = [('one', 'two', 'three'), ('three', 'two', 'one')]
        self.assertTrue(list(file_reader(file_name, num_fields=3, sep=',', header=False)), expect)


                    
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
                    

    for line in file_reader(file_name, num_fields, sep=',', header=True):
        print(line)


