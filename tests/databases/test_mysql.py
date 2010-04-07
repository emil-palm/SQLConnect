'''
Created on Apr 7, 2010

@author: emil
'''
import unittest
from Database import DatabaseConnectionFactory

class Test(unittest.TestCase):

    def test_validDSNWithoutPort(self):
        """ Try setting up mysql object with a valid DSN without port """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost/database")
        self.assertNotEqual(database,None)
    
    def test_validDSNWithPort(self):
        """ Try setting up mysql object with a valid DSN with port """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost:3306/database")
        self.assertNotEqual(database,None)
        
    def test_invalidDSN(self):
        """ Try setting up mysql object with a invalid dsn """
        self.assertRaises(Exception,DatabaseConnectionFactory.DatabaseConnection("mysql://foo::bar@localhost:3306/database"))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    print "foobar"