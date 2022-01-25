#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mike
#
# Created:     28/08/2011
# Copyright:   (c) Mike 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import re
import urllib
import stringsFormat

def main():
    file=open('./file/language.csv',"r+")
    count = 0
    list = []
    for strLine in file.readlines():
        strLine = re.sub('^','"', strLine)
        strLine = re.sub(r'($(\r\n|\n)?)','"\n', strLine)
        strLine = re.sub(r'\t','","', strLine)
        list.append(strLine)
    file.seek(0)
    title = ''
    keyIdx, supportedLangs = stringsFormat.supportedLanguages()
    print(supportedLangs)
    for idx, lang in enumerate(supportedLangs):
        title.join('"%s"' %(lang))
        print(title)
        if idx != len(supportedLangs)-1:
            title.join(',')
        else:
            title.join('\n')
    print(title)
    file.write(title)
    file.writelines(list)
    file.truncate()
    file.close()

if __name__ == '__main__':
    main()
