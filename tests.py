import os
import nose
import unittest

APPLICATION_DIR = 'application.py'

class TestApplication(unittest.TestCase):


    def test_lint(self):
        resultado = os.system('pylint' + " " +APPLICATION_DIR)
        return resultado

if __name__ == '__main__':
    unittest.main()

