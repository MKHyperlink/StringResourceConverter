# StringResourceConverter
Generating Android/iOS string resource from CSV file.

When do you need it: You can create a Google Drive file for translation and export it as CSV file to local (You can use my another project GoogleDriveAccess to do it automatically). And then you can use this tool to generate Android or iOS string resources.

#### Introduce:
This tools is default executed by Jython. If you have Python in your platform, you can execute it with Python directly.

##### Add／Modify／delete supported languages:
	•	Open script/stringsFormat.py 
	•	Modify list content to what you need: LANGUAGE_ARY = ['variable', 'eng', 'cht', 'chs', 'jpn']
		Define alias for every languages in order in CSV file.
		ex: LANGUAGE_ARY = ['variable', 'kor', 'vnm', 'tha'] or ['variable', 'en', 'cht', 'chs', 'jp', 'kr', 'vn']
	•	If you want to change index of 'variable', the value of KEY_IDX should be change at the same time.
		ex: ['eng', 'cht', 'chs', 'jpn', 'variable']
		KEY_IDX = 4
	•	supportedLanguagesDisplay(): Define the display name for every languages on Android Operation UI.

##### Use python to execute Android string resource translation.
	python stringsFormat.py -csvtoxml [eng|cht|chs|jpn](self-defined alias)
	python stringsFormat.py -xmltocsv [eng|cht|chs|jpn](self-defined alias)


#### For Android:  
	•	Execute start.bat/sh: Launch the operation UI
![ScreenShot](/doc/screenshot/ScreenShot.png)

	XML to CSV function:
	•	Copy the language folder with strings.xml in Android project to "file" folder.
		Change the country code in folder name to self-defined alias.
		ex: [values-zh-rTW]->[values-cht]
			[values-ja]->[values-jpn]
	•	Press "start".
	•	It'll create language.csv file.

	CSV to XML function:
	•	Create strings.xml for target language, according to string in language.csv.

#### For iOS:
	•	There are no UI for operate. You can only use command line.
	•	Create string file "inforPlist.strings.[self-defined alias]" from language.csv.

	Steps:	
	•	If your language.csv file can't be import to execute, please execute "formatCsv.bat/sh" format language.csv.
		ex.
		from
		[variable]	[alias_1]	[alias_2]	[alias_3]
		to
		"variable","Eng","Cht","Chs","Jpn"    <= For reference, print self-defined alias. First line is useless
		"[variable]","[alias_1]","[alias_2]","[alias_3]"
	•	Execute iosCreateStringTable.sh/bat and create iOS string files.
	•	iOS can not export single language form CSV file. It should export all languages at the same time.
	•	iOS can not convert iOS string files to CSV file.


#### Folders:  
	files： contains every localization language files, CSV file
	libs：jython libs  
	script：python scripts
