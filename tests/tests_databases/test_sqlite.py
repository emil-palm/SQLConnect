'''
Created on Apr 8, 2010

@author: emil
'''
import unittest,tempfile
from random import randint
from Database import DatabaseConnectionFactory



class Test_SQLite(unittest.TestCase):


    def test_validMemoryDsn(self):
        """ Try valid SQLite memory DSN """
        database = DatabaseConnectionFactory.DatabaseConnection("sqlite://:memory:")
        self.assertNotEqual(database,None)
        
    def test_invalidMemoryDsn(self):
        """ Try invalid SQLite memory DSN """
        self.assertRaises(ValueError,DatabaseConnectionFactory.DatabaseConnection,("sqlite://:::test"))
        
    def test_ValidFileDsn(self):
        """ Try valid SQLite file DSN """ 
        
        database = DatabaseConnectionFactory.DatabaseConnection("sqlite://%s/SQLow.tmp" % tempfile.gettempdir())
        self.assertNotEqual(database,None)        
    
    def test_InvalidFileDsn(self):
        """ Try invalid SQLite file DSN """
        arg = ("sqlite:///%i/%i/%i/%i" % (randint(0,100),randint(0,100),randint(0,100),randint(0,100)))
        self.assertRaises(ValueError,DatabaseConnectionFactory.DatabaseConnection,arg)
        


if __name__ == "__main__":
    import sys;sys.argv = ['', '-v']
    unittest.main()