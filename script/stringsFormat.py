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
from unicodeCsv import UnicodeWriter, UnicodeReader

PARA_IDX = 0
ENG_IDX = 1
CHT_IDX = 2
CHS_IDX = 3
JPN_IDX = 4

csvFilePath = './file/language.csv'

engFolder = './file/values'
chtFolder = './file/values-zh-rTW'
chsFolder = './file/values-zh-rCN'
jpnFolder = './file/values-ja'
xmlFilePath = '/strings.xml'

def xmlToCsv(srcFile, desFile, lang, content):
    tree = ElementTree.parse(srcFile)

    desFile.writerow(['Parameter', 'eng', 'cht', 'chs', 'jpn'])

    index = 0
    #for node in tree.iter('string'): #new feature from python v2.7
    for node in tree.findall('string'):
        name = node.attrib.get('name')
        value = node.text

        if len(content)>index:
            langValue = content[index]
        else:
            langValue = ['','','','','']

        if name:
            if lang.lower() == 'eng':
                desFile.writerow([name, value, langValue[CHT_IDX], langValue[CHS_IDX], langValue[JPN_IDX]])
            elif lang.lower() == 'cht':
                desFile.writerow([name, langValue[ENG_IDX], value, langValue[CHS_IDX], langValue[JPN_IDX]])
            elif lang.lower() == 'chs':
                desFile.writerow([name, langValue[ENG_IDX], langValue[CHT_IDX], value, langValue[JPN_IDX]])
            elif lang.lower() == 'jpn':
                desFile.writerow([name, langValue[ENG_IDX], langValue[CHT_IDX], langValue[CHS_IDX], value])
            index+=1

def csvToXml(srcFile, desFile, lang):
    top = Element('resources')

    #comment = Comment('Generated for PyMOTW')
    #top.append(comment)

    isCrossRow = True
    for row in srcFile:
        if isCrossRow:
            isCrossRow = False
            continue
        parameter, english, chineseT, chineseS, japanese = readFixedColumn(row)

        child = SubElement(top, 'string')
        child.set('name',parameter)
        if lang.lower() == 'eng':
            child.text = english
        elif lang.lower() == 'cht':
            child.text = chineseT
        elif lang.lower() == 'chs':
            child.text = chineseS
        elif lang.lower() == 'jpn':
            child.text = japanese

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
    oriDataReader = UnicodeReader(oriData)
    isCrossRow = True
    for row in oriDataReader:
        if isCrossRow:
            isCrossRow = False
            continue
        parameter, english, chineseT, chineseS, japanese = readFixedColumn(row)
        content.append([parameter, english, chineseT, chineseS, japanese])
    oriData.close()
    return content

def readFixedColumn(row):
    print row
    if len(row) !=0:
        parameter = row[PARA_IDX]
        english = row[ENG_IDX]
        chineseT = row[CHT_IDX]
        chineseS = row[CHS_IDX]
        japanese = row[JPN_IDX]
    else:
        parameter = ''
        english = ''
        chineseT = ''
        chineseS = ''
        japanese = ''
    return (parameter, english, chineseT, chineseS, japanese)

def checkFolderExists(lang):
    global xmlFilePath
    xmlFilePath = '/strings.xml'
    if lang.lower() == 'eng':
        if not os.path.exists(engFolder):
            os.makedirs(engFolder)
        xmlFilePath = engFolder+xmlFilePath
    elif lang.lower() == 'cht':
        if not os.path.exists(chtFolder):
            os.makedirs(chtFolder)
        xmlFilePath = chtFolder+xmlFilePath
    elif lang.lower() == 'chs':
        if not os.path.exists(chsFolder):
            os.makedirs(chsFolder)
        xmlFilePath = chsFolder+xmlFilePath
    elif lang.lower() == 'jpn':
        if not os.path.exists(jpnFolder):
            os.makedirs(jpnFolder)
        xmlFilePath = jpnFolder+xmlFilePath
    else:
        if not os.path.exists(engFolder):
            os.makedirs(engFolder)
        xmlFilePath = engFolder+xmlFilePath

def start(function, lang):
    checkFolderExists(lang)
    if function.lower()=="-csvtoxml":
        csvFile = open(csvFilePath,'r')
        xmlFile = open(xmlFilePath,'w+')
        #csvreader = csv.reader(csvFile)
        csvreader = UnicodeReader(csvFile)
        csvToXml(csvreader, xmlFile, lang)
        csvFile.close()
        xmlFile.close()
    elif function.lower()=="-xmltocsv":
        xmlFile = open(xmlFilePath,'r')
        if os.path.exists(csvFilePath):
            content = readOriginalCsvData()
            csvFile = open(csvFilePath,'w+')
        else:
            csvFile = open(csvFilePath,'w+')
            content = []

        #csvwriter = csv.writer(csvFile)
        csvwriter = UnicodeWriter(csvFile, lineterminator='\n')
        xmlToCsv(xmlFile, csvwriter, lang, content)
        csvFile.close()
        xmlFile.close()




