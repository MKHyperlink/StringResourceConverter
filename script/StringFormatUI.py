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


WINDOW_WIDTH=300
WINDOW_HEIGHT=400

language = ['All']
languageDic = stringsFormat.supportedLanguagesDisplay()
for key in languageDic:
	language.insert(0, key)

function = ['xml to csv', 'csv to xml'] 
functionDic = {function[0]:'-xmltocsv', function[1]:'-csvtoxml'}


class RadioAction():
	def __init__(self, type):
		if(type == 'lang'):
			self.selected = language[-1]
		elif(type == 'func'):
			self.selected = function[-1]
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
			for lang in languageDic:
				stringsFormat.start(functionDic[funcRdoAct.getSelected()], languageDic[lang])
		else:
			stringsFormat.start(functionDic[funcRdoAct.getSelected()], languageDic[langRdoAct.getSelected()])

btnAct = ButtonAction()

def langPanelInit(langPnl):
	langPnl.setBorder(TitledBorder('Language:'))
	langRdoBtnGrp = ButtonGroup()

	for idx, lang in enumerate(language):
		rdoBtn = JRadioButton(lang, actionPerformed = langRdoAct.select)	
		if idx == len(language)-1:
			rdoBtn.setSelected(True)
		langRdoBtnGrp.add(rdoBtn)
		langPnl.add(rdoBtn, 'wrap')

def funcPanelInit(funcPnl):
	funcPnl.setBorder(TitledBorder('Function:'))
	funcRdoBtnGrp = ButtonGroup()

	for idx, func in enumerate(function):
		rdoBtn = JRadioButton(func, actionPerformed = funcRdoAct.select)
		if idx == len(function)-1:
			rdoBtn.setSelected(True)
		funcRdoBtnGrp.add(rdoBtn)
		funcPnl.add(rdoBtn, 'wrap')

def actionPanelInit(actionPnl):
	startBtn = JButton('Start', actionPerformed = btnAct.start)
	exitBtn = JButton('Exit', actionPerformed = btnAct.quit)
	pnl = JPanel()
	actionPnl.add(pnl, 'w %s'%(WINDOW_WIDTH/4))
	actionPnl.add(startBtn)
	actionPnl.add(exitBtn, 'right')

class ConfigEditor(Runnable):
	def __init__(self):
		self.mainFrame = JFrame('Main Form')
		self.mainFrame.setSize(WINDOW_WIDTH, WINDOW_HEIGHT)
		self.mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
		
		self.basePnl = JPanel(MigLayout())
		self.langPnl = JPanel(MigLayout())
		self.funcPnl = JPanel(MigLayout())
		self.actionPnl = JPanel(MigLayout('fillx, insets 10 0 10 0'))
		
		langPanelInit(self.langPnl)
		funcPanelInit(self.funcPnl)
		actionPanelInit(self.actionPnl)
		
		self.basePnl.add(self.langPnl, 'wrap, w %s'%(WINDOW_WIDTH))
		self.basePnl.add(self.funcPnl, 'wrap, w %s'%(WINDOW_WIDTH))
		self.basePnl.add(self.actionPnl, 'wrap, w %s'%(WINDOW_WIDTH))
		
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

