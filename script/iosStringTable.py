import stringsFormat
from unicodeCsv import UnicodeWriter, UnicodeReader

filePath = './file/infoPlist.strings'

def writeFile(desFile, lang, content, keyIdx):
    for row in content:        
        langIdx = langAry.index(lang)
        line = "\"%s\"=\"%s\";\n"%(row[keyIdx], row[langIdx])
        desFile.write(line.encode('utf8'))

def createLanguageFile(lang, content, keyIdx):
    langFilePath = '%s.%s' %(filePath, lang)
    langFile = open(langFilePath,'w+')
    writeFile(langFile, lang, content, keyIdx)

    if(langFile):
        langFile.close()

if ( __name__ == '__main__' ) or ( __name__ == 'main' ) :
    content = stringsFormat.readOriginalCsvData()
    keyIdx, langAry = stringsFormat.supportedLanguages()

    for idx, lang in enumerate(langAry):
        if idx == keyIdx:
            continue
        createLanguageFile(lang, content, keyIdx)    

