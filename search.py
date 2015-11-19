# coding=utf-8
import os
import re
import codecs
from os import listdir
from os.path import basename, isdir


def trans(fullname):
    prefix = ""
    separator1 = "    "
    separator2 = "    "
    separator3 = "            "

    connector1 = "-"
    # kkk.xmi -->  kkk-UIElement.txt | kkk-Business.txt
    #                 ^                   ^

    connector2 = "_"
    # UIElement_Business
    #          ^

    resault = "Init String"
    tag_packagedElement = 0
    tag_ownedOperation_print = 0
    tag_ownedAttribute_print = 0
    tag_ownedAttribute_xpath = 0
    filename = os.path.basename(fullname)
    dirname = os.path.dirname(fullname)
    file_object = codecs.open(fullname, 'rb')

    try:
        ret = re.search("\.xmi", filename)
        if ret:
            # os.chdir(os.path.dirname(abspath)+"\\..")
            ret = re.search(r"(\w+)(\.xmi)", filename)
            if ret:
                file = ret.group(1)
                prefix = dirname + "\\" + file + connector1
                #print ">>>" + prefix

            # init output files
            Business_file = codecs.open(prefix + 'Business.txt', 'w')
            UIElement_file = codecs.open(prefix + 'UIElement.txt', 'w')
            KeywordMap_file = codecs.open(prefix + 'KeywordMap.txt', 'w')

            for each_text in file_object:
                # <packagedElement start
                ret1_1 = re.search("<packagedElement", each_text)
                if ret1_1:
                    tag_packagedElement = 1
                    tag_ownedAttribute_print = 1
                    tag_ownedOperation_print = 1
                    ret2 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                    if ret2:
                        resault = ret2.group(2)
                        print  resault
                        KeywordMap_file.write(resault + "\n")

                # print tag_packagedElement
                ret1_2 = re.search(r"</packagedElement>", each_text)
                if (ret1_2 != None):
                    tag_packagedElement = 0

                if (tag_packagedElement == 1):
                    # <ownedAttribute start
                    ret3 = re.search("<ownedAttribute", each_text)
                    if ret3:
                        if (tag_ownedAttribute_print == 1):
                            resault = separator1 + "ownedAttribute:"
                            print resault
                            KeywordMap_file.write(resault + "\n")
                            tag_ownedAttribute_print = 0

                        ret4 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                        if ret4:
                            # <ownedAttribute  ended with no XPATH
                            ret4_1 = re.search("/>", each_text)
                            # <ownedAttribute  ended with XPATH
                            ret4_2 = re.search(">", each_text)
                            if ret4_1:
                                # no xpath,output
                                tag_ownedAttribute_xpath = 0
                                resault = separator2 + ret2.group(2) + connector2 + ret4.group(2)
                                print resault
                                KeywordMap_file.write(resault + "\n")
                                UIElement_file.write(resault + "\n")
                            else:
                                # xpath exist
                                if ret4_2:
                                    tag_ownedAttribute_xpath = 1
                                    resault = separator2 + ret2.group(2) + connector2 + ret4.group(2)
                                else:
                                    # if  the XMI syntax is wrong , report it
                                    print "ownedAttribute ending with illegal syntax, not with \" /> or > \"  "
                                    break

                    if (tag_ownedAttribute_xpath == 1):
                        # if xpath  exist , get it
                        ret5 = re.search(r"(value=\")(xpath=\S+)(\".+)", each_text)
                        if ret5:
                            resault = resault + separator1 + ret5.group(2)
                            print resault
                            KeywordMap_file.write(resault + "\n")
                            UIElement_file.write(resault + "\n")
                            tag_ownedAttribute_xpath = 0
                    # <ownedOperation start
                    ret6 = re.search("<ownedOperation", each_text)
                    if ret6:
                        if (tag_ownedOperation_print == 1):
                            resault = separator1 + "ownedOperation:"
                            print resault
                            KeywordMap_file.write(resault + "\n")
                            tag_ownedOperation_print = 0
                        ret6_1 = re.search(r"(name=\")(\S+)(\".+)", each_text)
                        if ret6_1:
                            resault = separator2 + ret2.group(2) + connector2 + ret6_1.group(2)
                            print resault
                            KeywordMap_file.write(resault + "\n")
                            Business_file.write(resault + "\n")

            Business_file.close()
            UIElement_file.close()
            KeywordMap_file.close()

    finally:
        file_object.close()


def traverse(path, depth=0):
    fullname = os.path.abspath(path)

    ret = re.search("\.xmi", fullname)
    if ret:
        print fullname,
        print os.path.basename(fullname),
        print os.path.dirname(fullname)
        trans(fullname)

    if (isdir(path)):
        for item in listdir(path):
            traverse(path + '/' + item, depth + 1)


if __name__ == '__main__':
    traverse('./')
