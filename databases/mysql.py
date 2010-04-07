'''
Created on Apr 7, 2010

@author: emil
'''

import MySQLdb as db
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
    
    connectionStringPattern = re.compile("([^\:]+):([^@]+)@([^\/]+)\/(\w+)")

    def __init__(self,string):
        '''
        Constructor
        '''
        match = self.connectionStringPattern.match(string)
        if match:
            (self.username,self.password,hostname,self.database) = match.groups()
            splits = hostname.split(":",1)
            if len(splits) > 1:
                (self.hostname,self.hostport) = splits
            else:
                self.hostname = hostname
                 
            if self.hostport is None:
                self.hostport = 3306
        else:
            raise Exception(string," is not a valid mysql dsn. mysql://username:password@hostname[:port]/database")
        
    def connect(self):
        return db.connect (host = self.hostname,
                           port = self.hostport,
                           user = self.username,
                           passwd = self.password,
                           db = self.database)
        