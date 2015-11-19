# coding=utf-8
from os.path import basename, isdir
from os import listdir
import re,os
import os

def traverse(path, depth=0):
    #print depth* '| ' + '|_', basename(path)
    filename=os.path.abspath(path)
    ret=re.search("\.txt",filename)
    if ret:

        os.remove(os.path.abspath(filename))

    if(isdir(path)):
        for item in listdir(path):
            traverse(path+'/'+item, depth+1)

if __name__ == '__main__':
    traverse('./')