'''
Created on Apr 7, 2010

@author: emil
'''

import inspect

def validateMethod(method, object):
        item = getattr(object, method)
        if item is not None:
            if inspect.ismethod(item):
                return
            else:
                raise AttributeError(method, ' is not a method')
        else:
            raise AttributeError(method, 'is not defined')
        
def validatePEP249Connection(connection):
    for method in ['close', 'commit', 'rollback', 'cursor']:
        validateMethod(method, connection)
        
def validatePEP249Cursor(cursor):
    for method in ['description', 'rowcount', 'close', 'execute', 'executemany', 'fetchone', 'fetchmany', 'fetchall', 'arraysize', 'setinputsizes', 'setoutputsize']:
        validateMethod(method, cursor)
        
def typeTransformer(value):
    if value is None:
        return "NULL"    
    elif isinstance(value, int):
        return value
    elif isinstance(value, float):
        return int(value)
    elif isinstance(value, str):
        return '"%s"' % value
    else:
        return '"%s"' % value.__str__() 

def sqlformat (values):
    valueString = ""
    if isinstance(values, list):
        valueString = ", ".join(str(typeTransformer(value)) for value in values)
#            
    elif isinstance(values, dict):
        valueString = ", ".join("%s=%s" % (value, typeTransformer(values[value])) for value in values)
        
    return valueString
            
            
