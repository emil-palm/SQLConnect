'''
Created on Apr 7, 2010

@author: emil
'''
from Database import DatabaseManager
from Database import SQLowException 

class BaseTable(object):
    __cols__ = ['']
    __conname__ = None
    
    def executeSql(self,sql,close=True):
        """
        Execute a given SQL
        """
        connection = DatabaseManger().getConnection(self.__conname__)
        
    def getConnection(self):
        return DatabaseManager().getConnection(self.__conname__)
        

class Foobar(BaseTable):
    
    def __init__(self):
        self.__conname__ = "test"
        self.connection = self.getConnection().connect()
        self.cursor = self.connection.cursor();
        
    def _setup(self):
        self.cursor.execute("DROP TABLE IF EXISTS `test`")
        self.cursor.execute("create table t1 (t1key INTEGER PRIMARY KEY,data TEXT,num double,timeEnter DATE);")
        
        
    def test(self):
        return self.getConnection()


if __name__ == '__main__':
    DatabaseManager().addConnection("sqlite://foobar.sqlite","test")
    foo = Foobar()
    foo._setup()
    print foo.test()
    
        
        