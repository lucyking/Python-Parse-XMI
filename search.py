# coding=utf-8
import re
import codecs
import os

# global tag_packagedElement
# global tag_ownedAttribute_print_print,tag_ownedAttribute_xpath
separator1 = "    "
separator2 = "        "
separator3 = "            "
tag_packagedElement = 0
tag_ownedOperation_print=0
tag_ownedAttribute_print = 0
tag_ownedAttribute_xpath = 0

resault = "Init String"

file_object = codecs.open('yixinapp.xmi', 'rb')
try:
    unicode_file = codecs.open('KeywordList.txt', 'w')
    for each_text in file_object:
        ret1_1 = re.search("<packagedElement", each_text)  # pattern1 for Mode1
        if ret1_1:
            tag_packagedElement = 1
            tag_ownedAttribute_print = 1
            tag_ownedOperation_print = 1
            ret2 = re.search(r"(name=\")(\S+)(\".+)", each_text)  # pattern1 for Mode1
            if ret2:
                print  ret2.group(2)
                # print tag_packagedElement

        ret1_2 = re.search(r"</packagedElement>", each_text)
        if (ret1_2 != None):
            tag_packagedElement = 0

        if (tag_packagedElement == 1):
            ret3 = re.search("<ownedAttribute", each_text)
            if ret3:
                if (tag_ownedAttribute_print == 1):
                    print  separator1+"ownedAttribute:"
                    tag_ownedAttribute_print = 0

                ret4 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                if ret4:
                    ret4_1 =re.search("/>",each_text)
                    ret4_2 =re.search(">",each_text)
                    if ret4_1:
                        tag_ownedAttribute_xpath = 0
                        resault = separator2+ ret2.group(2) + "_" + ret4.group(2)
                        print resault
                    else:
                        if ret4_2:
                            tag_ownedAttribute_xpath = 1
                            resault = separator2+ ret2.group(2) + "_" + ret4.group(2)
                        else:
                            # if  the XMI syntax is wrong , report it
                            print "ownedAttribute ending with  illegal syntax, not with \" /> or > \"  "
                            break


            if(tag_ownedAttribute_xpath==1):
                # if xpath  exist , get it
                ret5 = re.search(r"(value=\")(xpath=\S+)(\".+)", each_text)
                if ret5:
                    resault = resault+separator1+ret5.group(2)
                    print resault
                    tag_ownedAttribute_xpath = 0

            ret6 = re.search("<ownedOperation", each_text)
            if ret6:
                if(tag_ownedOperation_print==1):
                    print separator1+"ownedOperation:"
                    tag_ownedOperation_print = 0
                ret6_1 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                if ret6_1:
                    print separator2+ret2.group(2)+"_"+ret6_1.group(2)


















finally:
    file_object.close()
"""
if( len(re.findall(pattern4,each_text)) > 0 ):
    tag_packagedElement = 0
"""

"""
        if  tag_packagedElement > 0 :
            ret2 = re.findall(pattern3,each_text)
            if len(ret2) > 0:
                print "    "+page+"_"+ret2[0][3]
                unicode_file.write("    "+page+"_"+ret2[0][3]+"\n")


        ret = re.findall(pattern2, each_text)  #pattern2 for Class1
        if len(ret) > 0:
            print ret[0][3]
            unicode_file.write(ret[0][3]+'\n')
"""
