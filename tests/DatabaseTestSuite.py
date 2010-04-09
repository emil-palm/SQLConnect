'''
Created on Apr 8, 2010

@author: emil
'''
import unittest2 as unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    test = loader.discover(".")
    unittest.TextTestRunner(verbosity=2).run(test)