import re
from random import randint
from databases import *

'''
Created on Apr 7, 2010

@author: emil
'''
class SQLConnectException(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)


class DatabaseConnectionFactory(object):
    
    @staticmethod
    def _loadModule(schema, string):
        if schema.lower() == "mysql":
            return mysql.MySQL(string)
        elif schema.lower() == "sqlite":
            return sqlite.SQLite(string)
        else:
            raise SQLConnectException("%s is not a valid schema" % schema)
                
    @staticmethod        
    def DatabaseConnection(string):
        schemaPattern = re.compile("^([^\:]+):\/\/(.*)$")
        match = schemaPattern.search(string)
        if match:
            return DatabaseConnectionFactory._loadModule(match.group(1), match.group(2))
            
        
class DatabaseManager:
    """ A python singleton """
    class __Databaseimpl:
        """ Implementation of the singleton interface """
        
        databases = {}
        
        def addConnection(self, connectionString, name=None):
            if name is None:
                name = randint(0, 100)
                
            self.databases[name] = connectionString
            
            return name
        
        def _getConnectionString(self, name=None):
            if len(self.databases) is 0:
                raise SQLConnectException('Please add a connection before trying to get a connection')
            
            if name is not None:
                if name in self.databases.keys():
                    return self.databases[name]
                else:
                    raise SQLConnectException("%s is not added as a connection name" % name) 
            elif name is None and len(self.databases) == 1:
                return self.databases[self.databases.keys()[0]]
            else:
                raise SQLConnectException('Please provide the name for the connection since you have more then one connectionstring')
            
            raise SQLConnectException('This shouldnt happen')

        def getConnection(self, name=None):
            connectionString = self._getConnectionString(name)
            return DatabaseConnectionFactory.DatabaseConnection(connectionString)
        
        def execute(self, sql, name=None):
            conn = self.getConnection(name).connect()
            cur = conn.cursor()
            try:

                cur.execute(sql)
                conn.commit()
            finally:
                cur.close()
                conn.close()
            return cur
        
        def fetchList(self, sql, name=None):
            conn = self.getConnection(name).connect()
            cur = conn.cursor()
            cur.execute(sql)
            rows = []
            while (1):
                row = cur.fetchone()
                if row == None:
                    break #pragma: no cover
                rows.append(row)
                
            cur.close()
            conn.close()
            return rows
        
        def fetchDict(self, sql, name=None):
            
            conn = self.getConnection(name).connect()
            cur = conn.cursor()
            cur.execute(sql)
            
            rows = []
            cols = [ d[0] for d in cur.description ]
            
            while (1):
                row = cur.fetchone()
                if row == None:
                    break #pragma: no cover
                rows.append(dict(zip(cols, row)))
                
            cur.close()
            conn.close()
            return rows
            
            
             

    # storage for the instance reference
    __instance = None

    def __init__(self, connectionString=None):
        """ Create singleton instance """
        # Check whether we already have an instance
        if DatabaseManager.__instance is None:
            # Create and remember instance
            DatabaseManager.__instance = DatabaseManager.__Databaseimpl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = DatabaseManager.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
        
        
