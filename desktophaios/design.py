# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 300, 91))
        self.label.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 160, 220, 120))
        self.frame.setMaximumSize(QtCore.QSize(220, 120))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.file = QtGui.QTextEdit(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(100, 310, 450, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file.sizePolicy().hasHeightForWidth())
        self.file.setSizePolicy(sizePolicy)
        self.file.setMaximumSize(QtCore.QSize(450, 30))
        self.file.setReadOnly(False)
        self.file.setObjectName(_fromUtf8("file"))
        self.upload = QtGui.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(70, 310, 30, 30))
        self.upload.setMaximumSize(QtCore.QSize(30, 30))
        self.upload.setObjectName(_fromUtf8("upload"))
        self.search = QtGui.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(260, 350, 100, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setMaximumSize(QtCore.QSize(100, 30))
        self.search.setObjectName(_fromUtf8("search"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HAIOS Image Search", None))
        self.label.setText(_translate("MainWindow", "HAIOS", None))
        self.upload.setText(_translate("MainWindow", "...", None))
        self.search.setText(_translate("MainWindow", "Search Image", None))

