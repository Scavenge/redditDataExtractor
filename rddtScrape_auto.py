# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redditScraper.ui'
#
# Created: Mon May 26 01:14:22 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RddtScrapeMainWindow(object):
    def setupUi(self, RddtScrapeMainWindow):
        RddtScrapeMainWindow.setObjectName(_fromUtf8("RddtScrapeMainWindow"))
        RddtScrapeMainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(RddtScrapeMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.subredditList = QtGui.QListView(self.centralwidget)
        self.subredditList.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.subredditList.setObjectName(_fromUtf8("subredditList"))
        self.gridLayout.addWidget(self.subredditList, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addUserBtn = QtGui.QToolButton(self.centralwidget)
        self.addUserBtn.setObjectName(_fromUtf8("addUserBtn"))
        self.horizontalLayout.addWidget(self.addUserBtn)
        self.deleteUserBtn = QtGui.QToolButton(self.centralwidget)
        self.deleteUserBtn.setObjectName(_fromUtf8("deleteUserBtn"))
        self.horizontalLayout.addWidget(self.deleteUserBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.userList = QtGui.QListView(self.centralwidget)
        self.userList.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.userList.setObjectName(_fromUtf8("userList"))
        self.gridLayout.addWidget(self.userList, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.subredditLabel = QtGui.QLabel(self.centralwidget)
        self.subredditLabel.setObjectName(_fromUtf8("subredditLabel"))
        self.horizontalLayout_3.addWidget(self.subredditLabel)
        self.subredditListChooser = QtGui.QComboBox(self.centralwidget)
        self.subredditListChooser.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.subredditListChooser.setObjectName(_fromUtf8("subredditListChooser"))
        self.horizontalLayout_3.addWidget(self.subredditListChooser)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.addSubredditBtn = QtGui.QToolButton(self.centralwidget)
        self.addSubredditBtn.setObjectName(_fromUtf8("addSubredditBtn"))
        self.horizontalLayout_2.addWidget(self.addSubredditBtn)
        self.deleteSubredditBtn = QtGui.QToolButton(self.centralwidget)
        self.deleteSubredditBtn.setObjectName(_fromUtf8("deleteSubredditBtn"))
        self.horizontalLayout_2.addWidget(self.deleteSubredditBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.directoryBox = QtGui.QLineEdit(self.centralwidget)
        self.directoryBox.setObjectName(_fromUtf8("directoryBox"))
        self.gridLayout.addWidget(self.directoryBox, 4, 0, 1, 1)
        self.directorySelectBtn = QtGui.QPushButton(self.centralwidget)
        self.directorySelectBtn.setObjectName(_fromUtf8("directorySelectBtn"))
        self.gridLayout.addWidget(self.directorySelectBtn, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.userLabel = QtGui.QLabel(self.centralwidget)
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.horizontalLayout_4.addWidget(self.userLabel)
        self.userListChooser = QtGui.QComboBox(self.centralwidget)
        self.userListChooser.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.userListChooser.setAcceptDrops(False)
        self.userListChooser.setEditable(False)
        self.userListChooser.setObjectName(_fromUtf8("userListChooser"))
        self.horizontalLayout_4.addWidget(self.userListChooser)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.downloadBtn = QtGui.QPushButton(self.centralwidget)
        self.downloadBtn.setObjectName(_fromUtf8("downloadBtn"))
        self.gridLayout.addWidget(self.downloadBtn, 10, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.userSubBtn = QtGui.QRadioButton(self.centralwidget)
        self.userSubBtn.setChecked(True)
        self.userSubBtn.setObjectName(_fromUtf8("userSubBtn"))
        self.horizontalLayout_5.addWidget(self.userSubBtn)
        self.allUserBtn = QtGui.QRadioButton(self.centralwidget)
        self.allUserBtn.setChecked(False)
        self.allUserBtn.setObjectName(_fromUtf8("allUserBtn"))
        self.horizontalLayout_5.addWidget(self.allUserBtn)
        self.allSubBtn = QtGui.QRadioButton(self.centralwidget)
        self.allSubBtn.setObjectName(_fromUtf8("allSubBtn"))
        self.horizontalLayout_5.addWidget(self.allSubBtn)
        self.gridLayout.addLayout(self.horizontalLayout_5, 8, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        RddtScrapeMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RddtScrapeMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuType = QtGui.QMenu(self.menubar)
        self.menuType.setObjectName(_fromUtf8("menuType"))
        self.menuNew = QtGui.QMenu(self.menuType)
        self.menuNew.setObjectName(_fromUtf8("menuNew"))
        self.menuRemove = QtGui.QMenu(self.menuType)
        self.menuRemove.setObjectName(_fromUtf8("menuRemove"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        RddtScrapeMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RddtScrapeMainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RddtScrapeMainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(RddtScrapeMainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionCreate_New_Subreddit_List = QtGui.QAction(RddtScrapeMainWindow)
        self.actionCreate_New_Subreddit_List.setObjectName(_fromUtf8("actionCreate_New_Subreddit_List"))
        self.actionSubreddit_List = QtGui.QAction(RddtScrapeMainWindow)
        self.actionSubreddit_List.setObjectName(_fromUtf8("actionSubreddit_List"))
        self.actionUser_List = QtGui.QAction(RddtScrapeMainWindow)
        self.actionUser_List.setObjectName(_fromUtf8("actionUser_List"))
        self.actionSettings_2 = QtGui.QAction(RddtScrapeMainWindow)
        self.actionSettings_2.setObjectName(_fromUtf8("actionSettings_2"))
        self.actionSave = QtGui.QAction(RddtScrapeMainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionDownloaded_Reddit_User_Posts = QtGui.QAction(RddtScrapeMainWindow)
        self.actionDownloaded_Reddit_User_Posts.setObjectName(_fromUtf8("actionDownloaded_Reddit_User_Posts"))
        self.actionRemove_Subreddit_List = QtGui.QAction(RddtScrapeMainWindow)
        self.actionRemove_Subreddit_List.setObjectName(_fromUtf8("actionRemove_Subreddit_List"))
        self.actionRemove_User_List = QtGui.QAction(RddtScrapeMainWindow)
        self.actionRemove_User_List.setObjectName(_fromUtf8("actionRemove_User_List"))
        self.menuNew.addAction(self.actionSubreddit_List)
        self.menuNew.addAction(self.actionUser_List)
        self.menuRemove.addAction(self.actionRemove_Subreddit_List)
        self.menuRemove.addAction(self.actionRemove_User_List)
        self.menuType.addAction(self.menuNew.menuAction())
        self.menuType.addAction(self.menuRemove.menuAction())
        self.menuType.addAction(self.actionSave)
        self.menuType.addAction(self.actionSettings_2)
        self.menuType.addSeparator()
        self.menuType.addAction(self.actionExit)
        self.menuView.addAction(self.actionDownloaded_Reddit_User_Posts)
        self.menubar.addAction(self.menuType.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(RddtScrapeMainWindow)
        QtCore.QMetaObject.connectSlotsByName(RddtScrapeMainWindow)

    def retranslateUi(self, RddtScrapeMainWindow):
        RddtScrapeMainWindow.setWindowTitle(_translate("RddtScrapeMainWindow", "Reddit Scraper", None))
        self.addUserBtn.setText(_translate("RddtScrapeMainWindow", "+", None))
        self.deleteUserBtn.setText(_translate("RddtScrapeMainWindow", "-", None))
        self.subredditLabel.setText(_translate("RddtScrapeMainWindow", "Subreddits To Download From", None))
        self.addSubredditBtn.setText(_translate("RddtScrapeMainWindow", "+", None))
        self.deleteSubredditBtn.setText(_translate("RddtScrapeMainWindow", "-", None))
        self.directorySelectBtn.setText(_translate("RddtScrapeMainWindow", "Set directory to save to", None))
        self.userLabel.setText(_translate("RddtScrapeMainWindow", "Users to Download From", None))
        self.downloadBtn.setText(_translate("RddtScrapeMainWindow", "Download!", None))
        self.userSubBtn.setText(_translate("RddtScrapeMainWindow", "Constrain Selected Users To Selected Subreddits", None))
        self.allUserBtn.setText(_translate("RddtScrapeMainWindow", "Selected Users\' Content in All Subreddits", None))
        self.allSubBtn.setText(_translate("RddtScrapeMainWindow", "Selected Subreddits\' Frontpage Content", None))
        self.menuType.setTitle(_translate("RddtScrapeMainWindow", "&File", None))
        self.menuNew.setTitle(_translate("RddtScrapeMainWindow", "&New", None))
        self.menuRemove.setTitle(_translate("RddtScrapeMainWindow", "Remove", None))
        self.menuView.setTitle(_translate("RddtScrapeMainWindow", "&View", None))
        self.actionExit.setText(_translate("RddtScrapeMainWindow", "E&xit", None))
        self.actionCreate_New_Subreddit_List.setText(_translate("RddtScrapeMainWindow", "Create New Subreddit List", None))
        self.actionSubreddit_List.setText(_translate("RddtScrapeMainWindow", "New Subreddit List", None))
        self.actionSubreddit_List.setShortcut(_translate("RddtScrapeMainWindow", "Ctrl+1", None))
        self.actionUser_List.setText(_translate("RddtScrapeMainWindow", "New User List", None))
        self.actionUser_List.setShortcut(_translate("RddtScrapeMainWindow", "Ctrl+2", None))
        self.actionSettings_2.setText(_translate("RddtScrapeMainWindow", "&Settings", None))
        self.actionSave.setText(_translate("RddtScrapeMainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("RddtScrapeMainWindow", "Ctrl+S", None))
        self.actionDownloaded_Reddit_User_Posts.setText(_translate("RddtScrapeMainWindow", "&Downloaded Reddit User Posts", None))
        self.actionRemove_Subreddit_List.setText(_translate("RddtScrapeMainWindow", "Remove Selected Subreddit List", None))
        self.actionRemove_User_List.setText(_translate("RddtScrapeMainWindow", "Remove Selected User List", None))

