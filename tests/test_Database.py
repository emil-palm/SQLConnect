'''
Created on Apr 8, 2010

@author: emil
'''
import unittest
from Database import DatabaseManager, SQLowException, DatabaseConnectionFactory

class Test_DatabaseConnectionFactory(unittest.TestCase):
    def test_creatingMysql(self):
        """ Try to retrive a MySQL Database object """
        database = DatabaseConnectionFactory.DatabaseConnection("mysql://root@localhost/mysql")
        self.assertNotEqual(database,None)
        
    def test_creatingSQLite(self):
        """ Try to retrive a SQLite Database object """
        database = DatabaseConnectionFactory.DatabaseConnection("sqlite://:memory:")
        self.assertNotEqual(database,None)
    
        

class Test_DatabaseManager(unittest.TestCase):
    databaseManager = None
    def setUp(self):
        self.databaseManager = DatabaseManager()
    
    def tearDown(self):
        self.databaseManager.databases = {}

    def test_databaseManager(self):
        """ Try to get the databaseManager object """
        self.assertNotEqual(self.databaseManager,None)

    def test_addSQLConnectionWithoutName(self):
        """ Try adding a connection without name"""
        self.databaseManager.addConnection("sqlite://:memory:")
        
    def test_getSQLConnectionWithoutName(self):
        """ Try adding and retreving a connection without a name """
        self.databaseManager.addConnection("sqlite://:memory:")
        self.assertNotEqual(self.databaseManager.getConnection(),None)

    def test_addSQLConnectionWithName(self):
        """ Try adding a connection with a name """
        self.databaseManager.addConnection("sqlite://:memory:","sqlite")
    
    def test_getSQLConnectionWithName(self):
        """ Try adding and retreving a connection with a name """
        self.databaseManager.addConnection("sqlite://:memory:","sqlite")
        self.assertNotEqual(self.databaseManager.getConnection("sqlite"),None)
        
    def test_getSQLConnectionWithoutAdding(self):
        """ Try retriving a database object before adding a object """
        self.assertRaises(SQLowException,self.databaseManager.getConnection)
        self.assertRaises(SQLowException,self.databaseManager.getConnection,("sqlite"))
    
    def test_getAndConnect(self):
        """ Try adding a database and then retrive and connect """
        self.databaseManager.addConnection("sqlite://:memory:")
        sqlite = self.databaseManager.getConnection()
        self.assertNotEqual(sqlite.connect(),None)
        

if __name__ == "__main__":
    import sys;sys.argv = ['', '-v']
    unittest.main()