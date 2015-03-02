import sys
import os
sys.path.append(r'./lib/miglayout-4.0-swing.jar')

import stringsFormat
from net.miginfocom.swing import MigLayout #@UnresolvedImport
from javax.swing.border import TitledBorder
from javax.swing import (JFrame, JLabel, JPanel, JRadioButton, JButton,
	JCheckBox, JList, JScrollPane, JTextField, JTextArea, SwingUtilities,
	JOptionPane, ButtonGroup)	
from java.lang import Runnable, Thread, Runtime


WIDTH=280
HEIGHT=30

language = ['English', 'Chinese traditional', 'Chinese simple', 'Japanese', 'All']
languageDic = {language[0]:'eng', language[1]:'cht', language[2]:'chs', language[3]:'jpn'}
function = ['xml to csv', 'csv to xml'] 
functionDic = {function[0]:'-xmltocsv', function[1]:'-csvtoxml'}


class RadioAction():
	def __init__(self, type):
		if(type == 'lang'):
			self.selected = language[0]
		elif(type == 'func'):
			self.selected = function[0]
	def select(self, event):
		self.selected =  event.getActionCommand()
	def getSelected(self):
		return self.selected

langRdoAct = RadioAction('lang')
funcRdoAct = RadioAction('func')


class ButtonAction():	
	def quit(self, event):
		sys.exit()	
	def start(self, event):
		if(langRdoAct.getSelected().lower() == 'all'):
			for lang in languageDic.keys():
				stringsFormat.start(functionDic[funcRdoAct.getSelected()], languageDic[lang])
		else:
			stringsFormat.start(functionDic[funcRdoAct.getSelected()], languageDic[langRdoAct.getSelected()])

btnAct = ButtonAction()

def langPanelInit(langPnl):
	langPnl.setBorder(TitledBorder('Language:'))
	engRdoBtn = JRadioButton(language[0], actionPerformed = langRdoAct.select)
	chtRdoBtn = JRadioButton(language[1], actionPerformed = langRdoAct.select)
	chsRdoBtn = JRadioButton(language[2], actionPerformed = langRdoAct.select)
	jpnRdoBtn = JRadioButton(language[3], actionPerformed = langRdoAct.select)
	allRdoBtn = JRadioButton(language[4], actionPerformed = langRdoAct.select)
	engRdoBtn.setSelected(True)
	langRdoBtnGrp = ButtonGroup()
	langRdoBtnGrp.add(engRdoBtn)
	langRdoBtnGrp.add(chtRdoBtn)
	langRdoBtnGrp.add(chsRdoBtn)
	langRdoBtnGrp.add(jpnRdoBtn)
	langRdoBtnGrp.add(allRdoBtn)
	langPnl.add(engRdoBtn, 'wrap')
	langPnl.add(chtRdoBtn, 'wrap')
	langPnl.add(chsRdoBtn, 'wrap')
	langPnl.add(jpnRdoBtn, 'wrap')
	langPnl.add(allRdoBtn, 'wrap')
	

def funcPanelInit(funcPnl):
	funcPnl.setBorder(TitledBorder('Function:'))
	x2vRdoBtn = JRadioButton(function[0], actionPerformed = funcRdoAct.select)
	c2xRdoBtn = JRadioButton(function[1], actionPerformed = funcRdoAct.select)
	x2vRdoBtn.setSelected(True)
	funcRdoBtnGrp = ButtonGroup()
	funcRdoBtnGrp.add(x2vRdoBtn)
	funcRdoBtnGrp.add(c2xRdoBtn)
	funcPnl.add(x2vRdoBtn, 'wrap')
	funcPnl.add(c2xRdoBtn, 'wrap')

def actionPanelInit(actionPnl):
	startBtn = JButton('Start', actionPerformed = btnAct.start)
	exitBtn = JButton('Exit', actionPerformed = btnAct.quit)
	pnl = JPanel()
	actionPnl.add(pnl, 'w %s'%(WIDTH/4))
	actionPnl.add(startBtn)
	actionPnl.add(exitBtn, 'right')

class ConfigEditor(Runnable):
	def __init__(self):
		self.mainFrame = JFrame('Main Form')
		self.mainFrame.setSize(300, 400)
		self.mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		
		self.basePnl = JPanel(MigLayout())
		self.langPnl = JPanel(MigLayout())
		self.funcPnl = JPanel(MigLayout())
		self.actionPnl = JPanel(MigLayout('fillx, insets 10 0 10 0'))
		
		langPanelInit(self.langPnl)
		funcPanelInit(self.funcPnl)
		actionPanelInit(self.actionPnl)
		
		self.basePnl.add(self.langPnl, 'wrap, w %s'%(WIDTH))
		self.basePnl.add(self.funcPnl, 'wrap, w %s'%(WIDTH))
		self.basePnl.add(self.actionPnl, 'wrap, w %s'%(WIDTH))
		
		self.mainFrame.add(self.basePnl)
		
	def run(self):
		self.mainFrame.setVisible(True)

if ( __name__ == '__main__' ) or ( __name__ == 'main' ) :
	#--------------------------------------------------
	# Schedule a job for the event-dispatching thread:
	# creating and showing this application's GUI.
	#--------------------------------------------------
	SwingUtilities.invokeLater( ConfigEditor() )
	raw_input()
	sys.exit()
else :
	print 'Error - script must be executed, not imported.\n'
	print 'Usage: jython %s.py\n' % __name__
	print '   or: wsadmin -conntype none -f %s.py' % __name__

