介紹： 
	此程式預設使用 jython 來執行，若平台己有安裝 python 可直接使用 python 執行。
使用 python 直接執行會無 UI 使用需使用 Command line:
	python stringsFormat.py -csvtoxml [eng|cht|chs|jpn]
	python stringsFormat.py -xmltocsv [eng|cht|chs|jpn]


For Android:
	•	執行start.bat/sh: 啟動UI

	UI功能：
	•	Xml to csv function:
	•	按android預設語系資料夾名稱，連同strings.xml一起複製到「file」資料夾
	•	按下「start」
	•	結果會產生language.csv檔

	•	Csv to xml function:
	•	依照language.csv檔格式把值填入，結果會在各語系資料夾中產生strings.xml

For iOS:
	•	無UI
	•	根據	language.csv 轉換成 iOS 字串表「inforPlist.strings.[語系]」

	Steps:	
	•	執行 formatCsv.bat/sh: 格式化 language.csv 為可處理格式
		ex.
		from
		[變數名稱]	[語系1]	[語系2]	[語系3]
		to
		"[變數名稱]","[語系1]","[語系2]","[語系3]"
	•	執行 androidToIOS_string.sh 產生 iOS plist檔


Folders:
	files： 語系檔
	libs：jython libs
	script：python scripts



