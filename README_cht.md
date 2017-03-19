# StringResourceConverter
依據 CSV 檔轉換出 android 用 XML 字串檔，及 iOS 用的字串檔。

使用場景：在 Google Drive 創建公開的語系表供翻譯，再輸出 CSV 檔至本地端（可搭配另一專案 GoogleDriveAccess 一併使用），使用本工具轉換成 android/iOS 平台使用的語系檔。

#### 介紹：  
此程式預設使用 jython 來執行，只要有安裝 Java Runtime 即可直接執行，若是平台己有安裝 python 也可直接使用 python 執行。  

##### 新增／修改／刪減支援語系：
	• 開啟 script/stringsFormat.py 
	• 修改 List 內容成需要的語系：LANGUAGE_ARY = ['variable', 'eng', 'cht', 'chs', 'jpn']
	  依照順序為 CSV 檔中的各語系定義代號
	  ex: LANGUAGE_ARY = ['variable', 'kor', 'vnm', 'tha'] 或 ['variable', 'en', 'cht', 'chs', 'jp', 'kr', 'vn']
	• 如果要改變「變數」的位序，需一併更改 KEY_IDX
	  ex: ['eng', 'cht', 'chs', 'jpn', 'variable']
	  KEY_IDX = 4
	• supportedLanguagesDisplay() 目前儘有 android 使用，定義各語系在 UI 顯示時的名字，請自行依需求更改

##### 使用 python 執行 Android 語系檔轉換:  
	python stringsFormat.py -csvtoxml [eng|cht|chs|jpn](自定義的支援語系)  
	python stringsFormat.py -xmltocsv [eng|cht|chs|jpn](自定義的支援語系)

#### For Android:  
	• 執行start.bat/sh: 啟動UI
![ScreenShot](/doc/screenshot/ScreenShot.png)

	XML to CSV function:
	• 將 Android 語系資料夾，連同 strings.xml 一起複製到「file」資料夾，再將資料夾後方的「語系」更改成自定義的代號。
	  ex: [values-zh-rTW]->[values-cht]
	      [values-ja]->[values-jpn]
	• 按下「start」
	• 產生 language.csv 檔

	CSV to XML function:
	• 依照 language.csv 檔格式把值填入，結果會在各語系資料夾中產生 strings.xml

#### For iOS:
	• 無 UI，需使用 command line。
	• 根據 language.csv 轉換成 iOS 字串表「inforPlist.strings.[自定義的支援語系]」

	Steps:	
	• 如果 language.csv 非正規 CSV 檔，執行 formatCsv.sh/bat 格式化 language.csv 成可處理格式
	  ex：
	  from
	  [變數名稱]	[語系代號1]	[語系代號2]	[語系代號3]
	  to
	  "variable","Eng","Cht","Chs","Jpn"    <= 印出定義的支援語系。參考用，第一行無作用。
	  "[變數名稱]","[語系代號1]","[語系代號2]","[語系代號3]"
	• 執行 iosCreateStringTable.sh/bat 產生 iOS 字串檔
	• iOS 不支援單一語系轉換，需一次全部轉出
	• iOS 不支援反向轉出 CSV 檔


#### Folders:  
	files： CSV 檔放置處、各語系檔產出處
	libs：jython libs  
	script：python scripts
