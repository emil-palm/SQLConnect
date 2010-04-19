'''
Created on Apr 8, 2010

@author: emil
'''
import unittest2 as unittest
from random import randint
from ..SQLConnect import DatabaseManager, SQLConnectException, DatabaseConnectionFactory

class Test_DatabaseConnectionFactory(unittest.TestCase):
    def test_creatingMysql(self):
        # Try to retrive a MySQL Database object
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost/mysql")
        self.assertNotEqual(database, None)
        
    def test_creatingSQLite(self):
        """ Try to retrive a SQLite Database object """
        database = DatabaseConnectionFactory.DatabaseConnection("sqlite://:memory:")
        self.assertNotEqual(database, None)
    
    def test_creatingFake(self):
        """ Try creating a non working object by using a invalid schema """
        self.assertRaises(SQLConnectException, DatabaseConnectionFactory.DatabaseConnection, ("random://randomInvalidString"))
        

class Test_DatabaseManager(unittest.TestCase):
    databaseManager = None
    def setUp(self):
        self.databaseManager = DatabaseManager()
    
    def tearDown(self):
        self.databaseManager.databases = {}

    def test_databaseManager(self):
        """ Try to get the databaseManager object """
        self.assertNotEqual(self.databaseManager, None)

    def test_addSQLConnectionWithoutName(self):
        """ Try adding a connection without name"""
        self.databaseManager.addConnection("sqlite://:memory:")
        
    def test_getSQLConnectionWithoutName(self):
        """ Try adding and retreving a connection without a name """
        self.databaseManager.addConnection("sqlite://:memory:")
        self.assertNotEqual(self.databaseManager.getConnection(), None)

    def test_addSQLConnectionWithName(self):
        """ Try adding a connection with a name """
        self.databaseManager.addConnection("sqlite://:memory:", "sqlite")
    
    def test_getSQLConnectionWithName(self):
        """ Try adding and retreving a connection with a name """
        self.databaseManager.addConnection("sqlite://:memory:", "sqlite")
        self.assertNotEqual(self.databaseManager.getConnection("sqlite"), None)
        
    def test_getSQLConnectionWithoutAdding(self):
        """ Try retriving a database object before adding a object """
        self.assertRaises(SQLConnectException, self.databaseManager.getConnection)
        self.assertRaises(SQLConnectException, self.databaseManager.getConnection, ("sqlite"))
    
    def test_getAndConnect(self):
        """ Try adding a database and then retrive and connect """
        self.databaseManager.addConnection("sqlite://:memory:")
        sqlite = self.databaseManager.getConnection()
        self.assertNotEqual(sqlite.connect(), None)
        
    def test_getRandomKey(self):
        """ Try getting a non added connection """
        self.databaseManager.addConnection("sqlite://:memory:")
        self.assertRaises(SQLConnectException, self.databaseManager.getConnection, ("%i%i" % (randint(0, 1000), randint(0, 1000))))
        
    def test_getConnectionStringWithoutName(self):
        """ Try adding and retreving a connection string without a name """
        self.databaseManager.addConnection("sqlite://:memory:")
        self.assertNotEqual(self.databaseManager._getConnectionString(), None)
        
    def test_getConnectionStringWithName(self):
        """ Try adding and retreving a connection string with a name """
        self.databaseManager.addConnection("sqlite://:memory:", "sqlite")
        self.assertNotEqual(self.databaseManager._getConnectionString("sqlite"), None)
        
    def test_getConnectionStringWithoutAdding(self):
        """ Try retreving a connectionString without adding one prior """
        self.assertRaises(SQLConnectException, self.databaseManager._getConnectionString)
                          
if __name__ == "__main__":
    import sys;sys.argv = ['', '-v']
    unittest.main()
