# StringTableConverter
Convert to Android/iOS string table format from CSV file.

####Introduce:
This tools is default executed by Jython. If you have Python in your platform, you can execute it with Python directly.

#####If you execute this tool with Python, you need use command line to operate it.
	python stringsFormat.py -csvtoxml [eng|cht|chs|jpn]  
	python stringsFormat.py -xmltocsv [eng|cht|chs|jpn]  


####For Android:  
	•	Execute start.bat/sh: Launch the operation UI

	XML to CSV function:
	•	Copy the language folder with strings.xml in android project to "file" folder.
	•	Press "start".
	•	It'll createed language.csv file.

	CSV to XML function:
	•	Create strings.xml for target language, according to string in language.csv.

####For iOS:
	•	There haven't UI to operate.
	•	Create string file "inforPlist.strings.[language]" for iOS to use, according to string in language.csv.

	Steps:	
	•	If your language.csv file can't be import to execute, please formate language.csv file with scripte "formateCsv.bat/sh".
		ex.
		from
		[string_var]	[lang_1]	[lang_2]	[lang_3]
		to
		"Parameter","Eng","Cht","Chs","Jpn"    <<= For reference, first line is useless
		"[string_var]","[lang_1]","[lang_2]","[lang_3]"
	•	Execute androidToIOS_string.sh and create iOS plist file.


####Folders:  
	files： contains localization language files.  
	libs：jython libs  
	script：python scripts
