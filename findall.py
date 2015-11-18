# coding=utf-8
import re
import codecs
import os
global flag
#global page

flag = 0
pattern1 = re.compile(r"(<packagedElement)(\s+\S+\s)(name=\")(\S+)(\".+)")
pattern2 =  re.compile(r"(<packagedElement)(\s\S+\s\S+\s)(name=\")(\S+)(\".+)")
pattern3 = re.compile(r"(<ownedAttribute)(\s\S+\s)(name=\")(\S+)(\".+)")
pattern4 = re.compile(r"</packagedElement>")

file_object = codecs.open('yixinapp.xmi', 'rb')
try:
    unicode_file = codecs.open('KeywordList.txt', 'w')
    for each_text in file_object:
        ret = re.findall(pattern1, each_text)    # pattern1 for Mode1
        if len(ret) > 0:
            print ret[0][3]
            page = ret[0][3]
            unicode_file.write(ret[0][3]+'\n')
            flag = 1

        if( len(re.findall(pattern4,each_text)) > 0 ):
            flag = 0


        if  flag > 0 :
            ret2 = re.findall(pattern3,each_text)
            if len(ret2) > 0:
                print "    "+page+"_"+ret2[0][3]
                unicode_file.write("    "+page+"_"+ret2[0][3]+"\n")


        ret = re.findall(pattern2, each_text)  #pattern2 for Class1
        if len(ret) > 0:
            print ret[0][3]
            unicode_file.write(ret[0][3]+'\n')
finally:
    file_object.close()


