#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *

qss = '''
*{
	/*font-size:12px;*/
}
ElegantMainWindow{
	background:#fff;
}
QToolBar{
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #f2f2f2);
	min-height:32px;
	max-height:32px;
	border-bottom:1px solid #a6a6a6;
	spacing: 3px;
}
QStatusBar{
	background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ededed);
	border-top:1px solid #ccc;
	font-size:12px;
}
ElegantMainSplitter::handle{
	background: #fff;
}
ElegantMainSplitter:handle:horizontal{
	width:1px;
}
ElegantMainSplitter::handle:vertical{
     height:1px;
}
QTreeWidget{
	border:1px solid #ddd;
	border-top:0;
	border-bottom:0;
}
QListWidget{
	border:0;
	show-decoration-selected: 1;
}
ElegantLibrary{
	border:0;
	show-decoration-selected: 1;
}
ElegantLibrary::item{
	padding:1px;
}
ElegantLibrary::item::text{}
SearchInput{
	border:1px solid #a9a9a9;
	padding:2px 3px 2px 18px;
	border-radius: 2px;
	min-width:280px;
	max-width:280px;
	margin-right:10px;
	background: #fff url(img/search.png);
	background-position: left center;
	background-repeat: none;
}
'''

class ElegantMainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(ElegantMainWindow, self).__init__()

		#self.setWindowFlags(Qt.CustomizeWindowHint)
		self.resize(1000, 600)

		#set window title
		self.setWindowTitle('Elegant Research')
		self.setWindowIcon(QIcon("img/logo.png"))
		
		#create status bar
		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Hello')

		#create menu bar
		self.menubar = self.menuBar()

		#create tool bar
		self.toolbar = self.addToolBar('')
		self.toolbar.setMovable(False)
		self.toolbar.setIconSize(QSize(20, 20))

		#create search input
		self.toolbarSearchInput = SearchInput(self)


		#split main window
		self.splitter = ElegantMainSplitter(self)
		self.setCentralWidget(self.splitter)
		
		#create library list
		self.libraryList = ElegantLibrary()
		ltest = QListWidget()

		#create document view
		self.documentView = QTreeWidget()

		self.splitter.addWidget(self.libraryList)
		self.splitter.addWidget(self.documentView)
		self.splitter.addWidget(ltest)
		self.splitter.setScales(0, 1, 0)

		self.setStyleSheet(qss)
		self.show()
		self.createActions()
		self.createMenus()
		self.createTools()
		
	def createActions(self):
		self.addFileAct = QAction(QIcon("img/blog--plus.png"), self.tr("Add files"), self,
			shortcut = QKeySequence.Open,
			toolTip = self.tr("Add files"),
			triggered = self.addFiles
		)
		self.removeDocAct = QAction(QIcon("img/blog--arrow.png"), self.tr("Remove from folder"), self,
			statusTip = self.tr("Remove document from folder"),
			triggered = self.removeFile
		)
		self.delDocAct = QAction(QIcon("img/blog--minus.png"), self.tr("Delete Document"), self,
			shortcut = QKeySequence.Quit,
			statusTip = self.tr("Delete Document from elegantr"),
			triggered = self.delFile
		)
		self.quitAct = QAction(self.tr("Quit"), self,
			statusTip = self.tr("Quit"),
			triggered = self.doQuit
		)

		self.copyAct = QAction(self.tr("Copy"), self,
			shortcut = QKeySequence.Copy,
			toolTip = self.tr("Copy"),
			triggered = self.doCopy
		)
		self.cutAct = QAction(self.tr("Cut"), self,
			shortcut = QKeySequence.Cut,
			toolTip = self.tr("Cut"),
			triggered = self.doCut
		)
		self.pasteAct = QAction(self.tr("Paste"), self,
			shortcut = QKeySequence.Paste,
			toolTip = self.tr("Paste"),
			triggered = self.doPaste
		)
		self.selectAllAct = QAction(self.tr("Select All"), self,
			shortcut = QKeySequence.SelectAll,
			statusTip = self.tr("Select All Documents"),
			triggered = self.selectAll
		)
		self.newFolderAct = QAction(QIcon("img/folder--plus.png"), self.tr("New Folder"), self,
			shortcut = QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_N),
			toolTip = self.tr("Create a new folder"),
			triggered = self.newFolder
		)
		self.removeFolderAct = QAction(QIcon("img/folder--minus.png"), self.tr("Remove Folder"), self,
			toolTip = self.tr("Remove the folder"),
			triggered = self.removeFolder
		)
		self.renameFolderAct = QAction(QIcon("img/folder-rename.png"), self.tr("Rename Folder"), self, 
			toolTip = self.tr("Rename the folder"),
			triggered = self.renameFolder
		)

		self.sidebarAct = QAction(QIcon("img/layout-2.png"), self.tr("Show sidebar"), self,
			toolTip = self.tr("Show sidebar"),
			triggered = self.showSidebar
		)

	def createMenus(self):
		self.fileMenu = self.menubar.addMenu(self.tr("&File"))
		self.fileMenu.addAction(self.addFileAct)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.removeDocAct)
		self.fileMenu.addAction(self.delDocAct)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.quitAct)

		self.editMenu = self.menubar.addMenu(self.tr("&Edit"))
		self.editMenu.addAction(self.copyAct)
		self.editMenu.addAction(self.cutAct)
		self.editMenu.addAction(self.pasteAct)
		self.editMenu.addSeparator()
		self.editMenu.addAction(self.selectAllAct)
		self.editMenu.addSeparator()
		self.editMenu.addAction(self.newFolderAct)
		self.editMenu.addAction(self.renameFolderAct)
		self.editMenu.addAction(self.removeFolderAct)
		
		self.viewMenu = self.menubar.addMenu(self.tr("&View"))
		self.toolMenu = self.menubar.addMenu(self.tr("&Tool"))
		self.helpMenu = self.menubar.addMenu(self.tr("&Help"))

	def createTools(self):
		self.toolbar.addAction(self.addFileAct)
		self.toolbar.addAction(self.removeDocAct)
		self.toolbar.addAction(self.delDocAct)
		self.toolbar.addSeparator()
		self.toolbar.addAction(self.newFolderAct)
		self.toolbar.addAction(self.renameFolderAct)
		self.toolbar.addAction(self.removeFolderAct)

		spacer = QWidget()
		spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.toolbar.addWidget(spacer)
		self.toolbar.addWidget(self.toolbarSearchInput)
		self.toolbar.addAction(self.sidebarAct)

	def addFiles(self):
		print "yes"
	def addFolder(self):
		pass
	def removeFile(self):
		pass
	def delFile(self):
		pass
	def doQuit(self):
		self.close()

	def doCopy(self):
		focus = QApplication.focusWidget()
		if focus is 0: return
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyPress, Qt.Key_C, Qt.ControlModifier))
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyRelease, Qt.Key_C, Qt.ControlModifier))

	def doCut(self):
		focus = QApplication.focusWidget()
		if focus is 0: return
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyPress, Qt.Key_X, Qt.ControlModifier))
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyRelease, Qt.Key_X, Qt.ControlModifier))
	
	def doPaste(self):
		focus = QApplication.focusWidget()
		if focus is 0: return
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyPress, Qt.Key_V, Qt.ControlModifier))
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyRelease, Qt.Key_V, Qt.ControlModifier))
	
	def selectAll(self):
		focus = QApplication.focusWidget()
		if focus is 0: return
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyPress, Qt.Key_A, Qt.ControlModifier))
		QApplication.postEvent(focus, QKeyEvent(QEvent.KeyRelease, Qt.Key_A, Qt.ControlModifier))
	
	def newFolder(self):
		self.libraryList.createNewFolder()

	def removeFolder(self):
		self.libraryList.removeCurrentItem()

	def renameFolder(self):
		self.libraryList.editCurrentItem()

	def showSidebar(self):
		print self.splitter.sizes()
		self.splitter.setSizes((256,486,0))

	

class SearchInput(QLineEdit):
	def __init__(self, parent=None):
		super(SearchInput, self).__init__(parent)

class ElegantMainSplitter(QSplitter):
	def __init__(self, parent=None):
		super(ElegantMainSplitter, self).__init__(Qt.Horizontal, parent)

	def setScales(self, *scales):
		for i, j in enumerate(scales):
			self.setStretchFactor(i, j)


class ElegantLibrary(QListWidget):
	def __init__(self):
		super(ElegantLibrary, self).__init__()
		self.setIconSize(QSize(36, 16))
		self._addDefaultItems()
		self.itemChanged.connect(self.itemTextChanged)
		self.itemClicked.connect(self.itemClick)
		self. itemDoubleClicked.connect(self.itemTwoClick)

	def _addHeaderItem(self, text):
		item = QListWidgetItem(text)
		icon = QPixmap(QSize(1, 1))
		icon.fill(Qt.transparent)
		item.setIcon(icon)
		item.setForeground(QBrush(QColor("#000")))
		font = QFont()
		font.setWeight(62)
		font.setPixelSize(13)
		item.setFont(font)
		item.setFlags(Qt.ItemIsSelectable)
		self.addItem(item)

	def _addSpaceItem(self):
		item = QListWidgetItem()
		item.setSizeHint(QSize(-1, 12))
		item.setFlags(Qt.ItemIsSelectable)
		self.addItem(item)

	def _addDefaultItems(self):
		self._addHeaderItem(self.tr('General Collections'))
		QListWidgetItem(QIcon("img/documents.png"), self.tr('All Documents'), self)
		QListWidgetItem(QIcon("img/recent.png"), self.tr('Recently Added'), self)
		QListWidgetItem(QIcon("img/started.png"), self.tr('Started'), self)
		QListWidgetItem(QIcon("img/uncategorized.png"), self.tr('Uncategorized'), self)
		QListWidgetItem(QIcon("img/owen.png"), self.tr('My Publications'), self)
		self._addSpaceItem()
		self._addHeaderItem(self.tr('My Folders'))
		icon = QPixmap(QSize(36, 16))
		icon.fill(Qt.transparent)
		self.newItemBtn = QListWidgetItem(QIcon(icon), self.tr('New Folder...'), self)
		self.newItemBtn.setFlags(self.newItemBtn.flags() | Qt.ItemIsEditable)
		self._addSpaceItem()
		self._addHeaderItem(self.tr('Recycle Bin'))
		QListWidgetItem(QIcon("img/bin.png"), self.tr('Deleted Documents'), self)

	def createNewFolder(self):
		self.editItem(self.newItemBtn)
		self.setCurrentItem(self.newItemBtn)

	def removeCurrentItem(self):
		row = self.currentRow()
		msgBox = QMessageBox.warning(self,
			self.tr("Remove Folder"),
			self.tr('Remove folder') + ' <font color="red">%s</font> ? ' % self.item(row).text()
			  + self.tr('This action can not be reversed.'),
			QMessageBox.Yes | QMessageBox.No,
		)
		if msgBox == QMessageBox.Yes:
			item = self.takeItem(row)
			del item

	def editCurrentItem(self):
		self.editItem(self.currentItem())

	def itemTextChanged(self, item):
		if item is self.newItemBtn:
			if item.text() == self.tr('New Folder...'):
				pass
			elif item.text() == "":
				item.setText(self.tr('New Folder...'))
			else:
				items = self.findItems(item.text(), Qt.MatchExactly)
				text = item.text()
				if len(items) > 1:
					while 1:
						text, ok = QInputDialog.getText(self, "Elegant Research",
							self.tr("The folder already exists. Enter a unique name for new folder:"),
							QLineEdit.Normal,
							text
						)
						if not ok or not text:
							item.setText(self.tr('New Folder...'))
							return
						if text != item.text():
							break
				newItem = QListWidgetItem(QIcon("img/folder.png"), text)
				newItem.setFlags(newItem.flags() | Qt.ItemIsEditable)
				self.insertItem(self.row(item), newItem)
				self.setCurrentItem(newItem)
				item.setText(self.tr('New Folder...'))
		else:
			if item.text() == "":
				item.setText(self.prevText)


	def itemClick(self, item):
		if item is self.newItemBtn:
			self.editItem(item)

	def itemTwoClick(self, item):
		self.prevText = item.text()

class PDF:
	def __init__(self, pdf):
		self.pdf = pdf

	def execute(self, program, args):
		process = QProcess()
		process.start(program, args)
		if process.waitForFinished():
			return process.readAll()

	def getTotalPages(self):	
		info = str(self.execute("pdfinfo", [self.pdf]))
		for line in info.split("\n"):
			if line.startswith("Pages:"):
				return line.strip().split()[1]

	def getFirstPage(self):
		return self.execute("pdftotext", ["-l", "1", self.pdf, "-"])

	def getLastPage(self):
		pages = self.getTotalPages()
		return self.execute("pdftotext", ["-f", pages, self.pdf, "-"])

	def getContents(self):
		return self.execute("pdftotext", [self.pdf])

	def getDoi(self):
		doiPattern = re.compile(r'(?:doi[:/]?)?(10.\d{4,}(?:.\d+)?/[^\s"<>]+)')
		content = self.getFirstPage()
		m = doiPattern.search(content)
		if m:
			return m.group(1)
		content = self.getLastPage()
		m = doiPattern.findall(content)
		if m:
			return m[-1]
		return None


def main():
	app = QApplication(sys.argv)
	elegantr = ElegantMainWindow()
	print PDF('test.pdf').getDoi()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()