#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *

qss = '''
*{
	font-size:12px;
	font-family: "Microsoft YaHei";
}
ElegantMainWindow{
	background:#fff;
}
QToolBar{
	background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #f2f2f2);
	min-height:37px;
	max-height:37px;
	border-bottom:1px solid #a6a6a6;
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
	padding:2px;
}
ElegantLibrary::item::text{}
SearchInput{
	border:1px solid #a9a9a9;
	padding:0px 3px 0px 18px;
	border-radius: 2px;
	min-width:300px;
	max-width:300px;
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
		self.setWindowTitle('Elegantr')
		self.setWindowIcon(QIcon("img/logo.png"))
		
		#create status bar
		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Hello')

		#create menu bar
		self.menubar = self.menuBar()

		#create tool bar
		self.toolbar = self.addToolBar('')
		self.toolbar.setMovable(False)

		#create search input
		self.toolbarSearchInput = SearchInput(self)


		#split main window
		splitter = ElegantMainSplitter(self)
		self.setCentralWidget(splitter)
		
		#create library list
		self.libraryList = ElegantLibrary()
		ltest = QListWidget()

		#create document view
		self.documentView = QTreeWidget()

		splitter.addWidget(self.libraryList)
		splitter.addWidget(self.documentView)
		splitter.addWidget(ltest)
		splitter.setScales(0, 1, 0)

		self.setStyleSheet(qss)
		self.show()
		self.createActions()
		self.createMenus()
		self.createTools()
		
	def createActions(self):
		self.addFileAct = QAction(QIcon("img/addfile.png"), self.tr("Add files"), self,
			shortcut = QKeySequence.Open,
			toolTip = self.tr("Add files"),
			triggered = self.addFiles
		)
		self.addFolderAct = QAction(QIcon("img/addfolder.png"), self.tr("Add folder"), self,
			shortcut = QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_O),
			toolTip = self.tr("Add files in a folder"),
			triggered = self.addFolder
		)
		self.removeDocAct = QAction(self.tr("Remove from Collection"), self,
			statusTip = self.tr("Remove document from collection"),
			triggered = self.removeFile
		)
		self.delDocAct = QAction(self.tr("Delete Document"), self,
			statusTip = self.tr("Delete Document from elegantr"),
			triggered = self.delFile
		)

		self.selectAllAct = QAction(self.tr("Select All"), self,
			shortcut = QKeySequence.SelectAll,
			statusTip = self.tr("Select All Documents"),
			triggered = self.selectAll
		)
		self.newCollectionAct = QAction(self.tr("New Collection"), self,
			shortcut = QKeySequence.New,
			toolTip = self.tr("Create a new collection"),
			triggered = self.newCollection
		)
		self.removeCollectionAct = QAction(self.tr("Remove Collection"), self,
			toolTip = self.tr("Remove the collection"),
			triggered = self.removeCollection
		)
		self.renameCollectionAct = QAction(self.tr("Rename Collection"), self, 
			toolTip = self.tr("Rename the collection"),
			triggered = self.renameCollection
		)

	def createMenus(self):
		self.fileMenu = self.menubar.addMenu(self.tr("&File"))
		self.fileMenu.addAction(self.addFileAct)
		self.fileMenu.addAction(self.addFolderAct)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.removeDocAct)
		self.fileMenu.addAction(self.delDocAct)
		self.editMenu = self.menubar.addMenu(self.tr("&Edit"))
		self.editMenu.addAction(self.selectAllAct)
		self.editMenu.addSeparator()
		self.editMenu.addAction(self.newCollectionAct)
		self.editMenu.addAction(self.removeCollectionAct)
		self.editMenu.addAction(self.renameCollectionAct)
		self.viewMenu = self.menubar.addMenu(self.tr("&View"))
		self.toolMenu = self.menubar.addMenu(self.tr("&Tool"))
		self.helpMenu = self.menubar.addMenu(self.tr("&Help"))

	def createTools(self):
		self.toolbar.addAction(self.addFileAct)
		spacer = QWidget()
		spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.toolbar.addWidget(spacer)
		self.toolbar.addWidget(self.toolbarSearchInput)

	def addFiles(self):
		print "yes"
	def addFolder(self):
		pass
	def removeFile(self):
		pass
	def delFile(self):
		pass

	def selectAll(self):
		pass
	
	def newCollection(self):
		collection = self.libraryList.addLibrary("New")
		self.libraryList.setCurrentItem(collection)
		self.libraryList.setFocus()
		self.libraryList.editItem(collection)


	def removeCollection(self):
		self.libraryList.removeCurrentItem()

	def renameCollection(self):
		self.libraryList.editCurrentItem()

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

	def _addHeaderItem(self, item):
		header = QListWidgetItem(item)
		icon = QPixmap(QSize(1, 1))
		icon.fill(Qt.transparent)
		header.setIcon(icon)
		#header.setForeground(QBrush(QColor("#8fb504")))
		font = QFont()
		font.setWeight(60)
		font.setPixelSize(13)
		header.setFont(font)
		self.addItem(header)

	def _addDefaultItems(self):
		self._addHeaderItem(self.tr('General Collections'))
		QListWidgetItem(QIcon("img/documents.png"), self.tr('All Documents'), self)
		QListWidgetItem(QIcon("img/recent.png"), self.tr('Recently Added'), self)
		QListWidgetItem(QIcon("img/started.png"), self.tr('Started'), self)
		QListWidgetItem(QIcon("img/uncategorized.png"), self.tr('Uncategorized'), self)
		QListWidgetItem(QIcon("img/owen.png"), self.tr('My Publications'), self)
		self._addHeaderItem(self.tr('My Collections'))
		self._addHeaderItem(self.tr('Recycle Bin'))
		QListWidgetItem(QIcon("img/bin.png"), self.tr('Deleted Documents'), self)

	def addLibrary(self, library):
		row = self.count() - 2
		item = QListWidgetItem(QIcon("img/folder.png"), library)
		item.setFlags(item.flags() | Qt.ItemIsEditable)
		self.insertItem(row, item)
		return item

	def removeCurrentItem(self):
		item = self.takeItem(self.currentRow())
		del item

	def editCurrentItem(self):
		self.editItem(self.currentItem())


def main():
	app = QApplication(sys.argv)
	elegantr = ElegantMainWindow()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()