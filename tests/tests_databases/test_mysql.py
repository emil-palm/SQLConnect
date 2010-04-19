'''
Created on Apr 7, 2010

@author: emil
'''
import unittest2 as unittest
from ...SQLConnect import DatabaseConnectionFactory

def checkMysql():
    try:
        import MySQLdb as db
        return True
    except ImportError:
        return False
 
#@unittest.skipIf(checkMysql(), "Cannot find MySQL skipping connection testing")
class Test_MySQL(unittest.TestCase):

    def test_validDSNWithoutPort(self):
        """ Try setting up mysql object with a valid DSN without port """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost/database")
        self.assertNotEqual(database, None)
    
    def test_validDSNWithPort(self):
        """ Try setting up mysql object with a valid DSN with port """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost:3306/database")
        self.assertNotEqual(database, None)
        
    def test_invalidDSN(self):
        """ Try setting up mysql object with a invalid dsn """
        self.assertRaises(ValueError, DatabaseConnectionFactory.DatabaseConnection, ("mysql://root::root@localhost:3306/database"))
    
    def test_mysqWithPassword(self):
        """ Try setting up mysql object with dsn containing password """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root:root@localhost/database")
        self.assertNotEqual(database, None)
        
    def test_mysqWithPort(self):
        """ Try setting up mysql object with dsn containing port """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost:3306/database")
        self.assertNotEqual(database, None)
        
    def test_mysqlWithPasswordAndPort(self):
        """ Try setting up mysql object with dsn containing password and port """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root:root@localhost:3306/database")
        self.assertNotEqual(database, None)
    
    def test_connect(self):
        try:
            import MySQLdb
        except ImportError:
            self.skip()
        
        """ Try connecting """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost:3306/mysql")
        try:
            conn = database.connect()
            self.assertNotEqual(conn, None)
        except MySQLdb.OperationalError:
            self.skipTest("Validate your mysql install")
        
        
    
        
