#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mike_Chen
#
# Created:     20/04/2012
# Copyright:   (c) Mike_Chen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import csv, sys
import os.path
import re
import codecs
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom

csvFilePath = './file/language.csv'
xmlToCsvFilePath = './file/language_fromXML.csv'
folderPath = './file/values'
xmlFilePath = '/strings.xml'

KEY_IDX = 0
LANGUAGE_ARY = ['variable', 'eng', 'cht', 'chs', 'jpn']

def supportedLanguagesDisplay():
    langDisplayDic = {}
    langDisplayDic['English'] = 'eng'
    langDisplayDic['Chinese traditional'] = 'cht'
    langDisplayDic['Chinese simple'] = 'chs'
    langDisplayDic['Japanese'] = 'jpn'
    return langDisplayDic

def supportedLanguages():
    return (KEY_IDX, LANGUAGE_ARY)

def xmlToCsv(srcFile, desFile, lang, content):
    tree = ElementTree.parse(srcFile)

    desFile.writerow(LANGUAGE_ARY)

    contentDic = {}
    for langAry in content:
        key = langAry[KEY_IDX]
        contentDic[key] = langAry

    #for node in tree.iter('string'): #new feature from python v2.7
    for node in tree.findall('string'):
        name = node.attrib.get('name')
        value = node.text
        if not value:
            value = ''

        langAry = contentDic[name]
        if not langAry:
            langAry = [''] * len(LANGUAGE_ARY)
            langAry[KEY_IDX] = name
        if len(langAry) < len(LANGUAGE_ARY):
            diffAry = [''] * (len(LANGUAGE_ARY)-len(langAry))
            langAry.extend(diffAry)
        langAry[LANGUAGE_ARY.index(lang)] = value
        desFile.writerow(langAry)

def csvToXml(srcFile, desFile, lang):
    top = Element('resources')

    #comment = Comment('Generated for PyMOTW')
    #top.append(comment)

    for idx, row in enumerate(srcFile):
        if idx == KEY_IDX:
            continue

        child = SubElement(top, 'string')
        child.set('name', row[KEY_IDX])
        child.text = row[LANGUAGE_ARY.index(lang)]          

    # Return a pretty-printed XML string for the Element.
    rough_string = ElementTree.tostring(top, 'utf-8')
    reparsed = minidom.parseString(rough_string)

    # print each item in one line
    reparsed = re.sub('\"\>\\n','\">',reparsed.toprettyxml(indent='', encoding='utf-8'))
    reparsed = re.sub('\\n\</string','</string', reparsed)
    reparsed = re.sub('\<string','\t<string', reparsed)

    desFile.write(reparsed)

def readOriginalCsvData():
    content = []
    oriData = open(csvFilePath,'r+')
    oriDataReader = csv.reader(oriData)

    for idx, row in enumerate(oriDataReader):
        if idx == KEY_IDX:
            continue
        print(repr(row))
        content.append(row)
    oriData.close()
    return content

def getXmlFileFullPath(lang, xmlPath):
    langFilePath = '%s-%s' %(folderPath, lang)
    if not os.path.exists(langFilePath):
        os.makedirs(langFilePath)
    return langFilePath+xmlPath

def start(function, lang, isCreateNewCSV=False):
    '''
    isCreateNewCSV:
        True: Create new CSV file after convert XML file to CSV file.
        False: Modify original CSV file.
    '''
    # print '%s, %s' %(function, lang)
    # return

    if function.lower()=="-csvtoxml":
        fullXmlFilePath = getXmlFileFullPath(lang, xmlFilePath)
        csvFile = open(csvFilePath,'r')
        xmlFile = open(fullXmlFilePath,'w+')
        csvreader = csv.reader(csvFile)

        csvToXml(csvreader, xmlFile, lang)
        csvFile.close()
        xmlFile.close()
    elif function.lower()=="-xmltocsv":
        fullXmlFilePath = getXmlFileFullPath(lang, xmlFilePath)
        xmlFile = open(fullXmlFilePath,'r')
        if os.path.exists(csvFilePath):
            content = readOriginalCsvData()
        else:
            content = []
        targetCsvFilePath = csvFilePath
        if isCreateNewCSV:
            targetCsvFilePath = xmlToCsvFilePath
        csvFile = open(targetCsvFilePath,'w+')

        csvwriter = csv.writer(csvFile)

        xmlToCsv(xmlFile, csvwriter, lang, content)
        csvFile.close()
        xmlFile.close()
    print('%s Done' %(lang))

if __name__ == "__main__":
   if len(sys.argv) != 3:
      print("Need more paramters: [-csvtoxml|-xmltocsv] [eng|cht|chs|jpn]")
   else:
      start(sys.argv[1], sys.argv[2], False)



