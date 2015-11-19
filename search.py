# coding=utf-8
import re
import codecs
import os
import sys
import view

separator1 = "    "
separator2 = "    "
separator3 = "            "
tag_packagedElement = 0
tag_ownedOperation_print=0
tag_ownedAttribute_print = 0
tag_ownedAttribute_xpath = 0

resault = "Init String"

file_object = codecs.open('WEB.xmi', 'rb')

try:

    Business_file = codecs.open('Business.txt','w')
    UIElement_file = codecs.open('UIElement.txt','w')
    KeywordMap_file = codecs.open('KeywordMap.txt', 'w')

    for each_text in file_object:
        ret1_1 = re.search("<packagedElement", each_text)  # <packagedElement  Begin
        if ret1_1:
            tag_packagedElement = 1
            tag_ownedAttribute_print = 1
            tag_ownedOperation_print = 1
            ret2 = re.search(r"(name=\")(\S+)(\".+)", each_text)
            if ret2:
                resault = ret2.group(2)
                print  resault
                KeywordMap_file.write(resault+"\n")
                # print tag_packagedElement

        ret1_2 = re.search(r"</packagedElement>", each_text)
        if (ret1_2 != None):
            tag_packagedElement = 0

        if (tag_packagedElement == 1):
            ret3 = re.search("<ownedAttribute", each_text)
            if ret3:
                if (tag_ownedAttribute_print == 1):
                    resault =  separator1+"ownedAttribute:"
                    print resault
                    KeywordMap_file.write(resault+"\n")
                    tag_ownedAttribute_print = 0

                ret4 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                if ret4:
                    ret4_1 =re.search("/>",each_text)
                    ret4_2 =re.search(">",each_text)
                    if ret4_1:
                        tag_ownedAttribute_xpath = 0
                        resault = separator2+ ret2.group(2) + "_" + ret4.group(2)
                        print resault
                        KeywordMap_file.write(resault+"\n")
                        UIElement_file.write(resault+"\n")
                    else:
                        if ret4_2:
                            tag_ownedAttribute_xpath = 1
                            resault = separator2+ ret2.group(2) + "_" + ret4.group(2)
                        else:
                            # if  the XMI syntax is wrong , report it
                            print "ownedAttribute ending " \
                                  "with illegal syntax, not with \" /> or > \"  "
                            break


            if(tag_ownedAttribute_xpath==1):
                # if xpath  exist , get it
                ret5 = re.search(r"(value=\")(xpath=\S+)(\".+)", each_text)
                if ret5:
                    resault = resault+separator1+ret5.group(2)
                    print resault
                    KeywordMap_file.write(resault+"\n")
                    UIElement_file.write(resault+"\n")
                    tag_ownedAttribute_xpath = 0

            ret6 = re.search("<ownedOperation", each_text)
            if ret6:
                if(tag_ownedOperation_print==1):
                    resault = separator1+"ownedOperation:"
                    print resault
                    KeywordMap_file.write(resault+"\n")
                    tag_ownedOperation_print = 0
                ret6_1 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                if ret6_1:
                    resault = separator2+ret2.group(2)+"_"+ret6_1.group(2)
                    print resault
                    KeywordMap_file.write(resault+"\n")
                    Business_file.write(resault+"\n")

    Business_file.close()
    UIElement_file.close()
    KeywordMap_file.close()


finally:
    file_object.close()


