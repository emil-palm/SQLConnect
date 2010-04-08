'''
Created on Apr 7, 2010

@author: emil
'''

import inspect

def validateMethod(method,object):
        item = getattr(object, method)
        if item is not None:
            if inspect.ismethod(item):
                return
            else:
                raise AttributeError(method,' is not a method')
        else:
            raise AttributeError(method,'is not defined')
        
def validatePEP249Connection(connection):
    for method in ['close','commit','rollback','cursor']:
        validateMethod(method,connection)
        
def validatePEP249Cursor(cursor):
    for method in ['description','rowcount','close','execute','executemany','fetchone','fetchmany','fetchall','arraysize','setinputsizes','setoutputsize']:
        validateMethod(method,cursor)
        
def unittest2():
    import unittest
    try:
        unittest.skip
    except AttributeError:
        import unittest2 as ut2
        unittest = ut2