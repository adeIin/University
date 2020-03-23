import unittest
from Repository import StudentRepository

class TestRepo(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(StudentRepository.addTwoNumbers(self,4,7), 11)