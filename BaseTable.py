'''
Created on Apr 7, 2010

@author: emil
'''
from Database import Database 

class BaseTable(object):
    __cols__ = ['']

    def __validateConnection(self):
        Database().hasConnection()
        Database().hasCursor()
        
    def executeSql(self,sql):
        
        print sql
        