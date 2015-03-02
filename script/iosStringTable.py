import stringsFormat
from unicodeCsv import UnicodeWriter, UnicodeReader

jpnFilePath = './file/infoPlist.strings.jpn'
chtFilePath = './file/infoPlist.strings.cht'
chsFilePath = './file/infoPlist.strings.chs'
engFilePath = './file/infoPlist.strings.eng'

PARA_IDX = 0
ENG_IDX = 1
CHT_IDX = 2
CHS_IDX = 3
JPN_IDX = 4

def writeFile(desFile, lang, content):
    for row in content:
        if lang.lower() == 'eng':
            line = "\"%s\"=\"%s\";\n"%(row[PARA_IDX], row[ENG_IDX])
            desFile.write(line.encode('utf8'))
        elif lang.lower() == 'cht':
            line = "\"%s\"=\"%s\";\n"%(row[PARA_IDX], row[CHT_IDX])
            desFile.write(line.encode('utf8'))
        elif lang.lower() == 'chs':
            line = "\"%s\"=\"%s\";\n"%(row[PARA_IDX], row[CHS_IDX])
            desFile.write(line.encode('utf8'))
        elif lang.lower() == 'jpn':
            line = "\"%s\"=\"%s\";\n"%(row[PARA_IDX], row[JPN_IDX])
            desFile.write(line.encode('utf8'))

def createLanguageFile(lang):
    langFile = None

    if lang.lower() == 'eng':
        langFile = open(engFilePath,'w+')
    elif lang.lower() == 'cht':
        langFile = open(chtFilePath,'w+')
    elif lang.lower() == 'chs':
        langFile = open(chsFilePath,'w+')
    elif lang.lower() == 'jpn':
        langFile = open(jpnFilePath,'w+')

    writeFile(langFile, lang, content)

    if(langFile):
        langFile.close()

if ( __name__ == '__main__' ) or ( __name__ == 'main' ) :
    content = stringsFormat.readOriginalCsvData()
    createLanguageFile('eng')
    createLanguageFile('cht')
    createLanguageFile('chs')
    createLanguageFile('jpn')

