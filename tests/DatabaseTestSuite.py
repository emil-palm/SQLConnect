'''
Created on Apr 8, 2010

@author: emil
'''

import unittest,sys
import tests_databases

if __name__ == "__main__":
        
    loader = unittest.TestLoader()
    testSuit = unittest.TestSuite()
    sys.path.append("tests_databases")
    for testModule in tests_databases.__all__:
        mod = __import__(testModule)
        for suit in loader.loadTestsFromModule(mod):
            for x in suit:
                testSuit.addTest(x)
                
    unittest.TextTestRunner(verbosity=2).run(testSuit)
    