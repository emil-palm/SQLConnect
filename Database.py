import re
from random import randint
from databases import *

'''
Created on Apr 7, 2010

@author: emil
'''
class SQLowException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class DatabaseConnectionFactory(object):
    
    
    @staticmethod
    def loadModule(schema,string):
        if schema.lower() == "mysql":
            return mysql.MySQL(string) 
                
    @staticmethod        
    def DatabaseConnection(string):
        schemaPattern = re.compile("^([^\:]+):\/\/(.*)$")
        match = schemaPattern.search(string)
        if match:
            return DatabaseConnectionFactory.loadModule(match.group(1),match.group(2))
            
        
class DatabaseManager:
    """ A python singleton """
    class __Databaseimpl:
        """ Implementation of the singleton interface """
        
        databases = {}
        
        def addConnection(self,connectionString,name=None):
            if name is None:
                name = randint()
                
            self.databases[name] = connectionString
            
            return name
        
        def _getConnectionString(self,name=None):
            if len(self.databases) is 0:
                raise SQLowException('Please add a connection before trying to get a connection')
            
            if name is None and len(self.databases) == 1:
                return self.databases[self.databses.keys()[0]]
            else:
                raise SQLowException('Please provide the name for the connection since you have more then one connectionstring')
            
            if name:
                return self.database[name]
            
            raise SQLowException('This shouldnt happen')
        
        def getConnection(self,name=None):
            sqlConnection = ""

                
            
             

    # storage for the instance reference
    __instance = None

    def __init__(self,connectionString=None):
        """ Create singleton instance """
        # Check whether we already have an instance
        if DatabaseManager.__instance is None:
            
            if connectionString is None:
                raise SQLowException('Cannot instansiate SQLow.database without sqlConnection argument')
            
            # Create and remember instance
            DatabaseManager.__instance = DatabaseManager.__Databaseimpl(connectionString)

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = DatabaseManager.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)


if __name__ == '__main__':
    apa = DatabaseConnectionFactory("mysql://ASDF:password@dev.miniclip.com/Database")
        
        