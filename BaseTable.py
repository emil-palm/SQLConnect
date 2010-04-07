'''
Created on Apr 7, 2010

@author: emil
'''
from Database import DatabaseManager
from Database import SQLowException 

class BaseTable(object):
    __cols__ = ['']
    __database__ = None

    def validate(self):
        if len(self.__cols__) == 0:
            raise SQLowException('You cannot have a table with a colum count of 0')
            
    
    def executeSql(self,sql,close=True):
        """
        Execute a given SQL
        """
        DatabaseManger().getConnection(self.__name__)
        
        
    
        
        