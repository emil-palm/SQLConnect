'''
Created on Apr 7, 2010

@author: emil
'''

try:
    import sqlite3 as db
except ImportError as e:
    import sqlite2 as db


class SQLite(object):
    '''
    classdocs
    '''
    database = None

    def __init__(self,string):
        self.database = string

    def connect(self):
        return db.connect (self.database)
        