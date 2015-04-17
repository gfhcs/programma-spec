# coding=utf8

'''
Created on 16.04.2015

@author: gereon
'''

def int2bin(i, minLength=0):
    
    b = ""
    
    while i > 0:              
        b = ('○' if (i % 2) == 0 else '●') + b            
        i /= 2
    
    while len(bin) < minLength:
        b = '○' + b
    
    return b
