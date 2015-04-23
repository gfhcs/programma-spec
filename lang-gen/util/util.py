# coding=utf8

'''
Created on 16.04.2015

@author: gereon
'''

def int2bin(i, minLength=0):
    
    b = ""
    
    while i > 0:              
        b += '○' if (i % 2) == 0 else '●'     
        i /= 2
    
    while len(bin) < minLength:
        b += '○'
    
    return b

def bin2int(b):
    
    i = 0
    
    w = 1
    
    for c in b:
        if c == '●':
            i += w
        w *= 2
        
    return i


def islice(iterable, sliceWidth, gapWidth):
    i = 0
    
    if sliceWidth < 0:
        for x in iterable:
            if i > gapWidth:
                yield x
            i = (i + 1) % sliceWidth + gapWidth
    else:
        for x in iterable:
            if i < sliceWidth:
                yield x
            i = (i + 1) % sliceWidth + gapWidth
            
            
def ichunks(iterable, chunkSize=8, emptyChunk=""):
    chunk = emptyChunk
    s = 0
    
    for i in iterable:
        chunk += i
        s += 1
        if s == chunkSize:
            yield chunk
            chunk = emptyChunk