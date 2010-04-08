'''
Created on Apr 7, 2010

@author: emil
'''
try:
    import MySQLdb as db
except ImportError:
    pass

import re

class MySQL(object):
    '''
    classdocs
    '''
    hostname = None
    hostport = None
    username = None
    password = None
    database = None
    
    connectionStringPattern = re.compile("(\w+)(\:\w+)?@(\w+)(\:\d+)?\/(\w+)")

    def __init__(self, string):
        '''
        Constructor
        '''
        match = self.connectionStringPattern.match(string)
        if match:
            (self.username, self.password, self.hostname, self.hostport, self.database) = match.groups()
            
            if self.password is not None:
                self.password.lstrip(":")
            
            if self.hostport is not None:
                self.hostport.lstrip(":")
            else:
                self.hostport = 3306
            
        else:
            raise ValueError("mysql://%s is not a valid mysql dsn. mysql://username[:password]@hostname[:port]/database" % string)
        
    def connect(self):
        return db.connect (host=self.hostname,
                           port=self.hostport,
                           user=self.username,
                           passwd=self.password,
                           db=self.database)
        
