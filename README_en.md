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
	•	Copy the language folder with strings.xml in android project to "file" folder
	•	Press "start"
	•	It'll createed language.csv file.

	CSV to XML function:
	•	Create strings.xml for target language, according to string in language.csv

####For iOS:
	•	There haven't UI to operate.
	•	根據	language.csv 轉換成 iOS 字串表「inforPlist.strings.[語系]」

	Steps:	
	•	如果language.csv非正規CSV檔，執行 formatCsv.bat/sh 格式化 language.csv 為可處理格式
		ex.
		from
		[變數名稱]	[語系1]	[語系2]	[語系3]
		to
		"Parameter","Eng","Cht","Chs","Jpn"    <<= 參考用，第一行無作用
		"[變數名稱]","[語系1]","[語系2]","[語系3]"
	•	執行 androidToIOS_string.sh 產生 iOS plist檔


####Folders:  
	files： 語系檔  
	libs：jython libs  
	script：python scripts
