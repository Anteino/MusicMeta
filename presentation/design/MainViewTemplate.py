# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1501, 582)
        MainWindow.setMinimumSize(QtCore.QSize(1501, 582))
        MainWindow.setMaximumSize(QtCore.QSize(1501, 582))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openFolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFolderButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.openFolderButton.setCheckable(False)
        self.openFolderButton.setObjectName("openFolderButton")
        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(106, 12, 631, 31))
        self.pathLabel.setObjectName("pathLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1501, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 80, 1501, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1499, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, 10, 1501, 21))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(10, 0, 17, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.currentFilenameLabel = QtWidgets.QLabel(self.frame)
        self.currentFilenameLabel.setGeometry(QtCore.QRect(40, 0, 201, 20))
        self.currentFilenameLabel.setObjectName("currentFilenameLabel")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(110, -10, 31, 31))
        self.commandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../../assets/icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(18, 20))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.selectAllCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.selectAllCheckBox.setGeometry(QtCore.QRect(10, 60, 17, 17))
        self.selectAllCheckBox.setText("")
        self.selectAllCheckBox.setObjectName("selectAllCheckBox")
        self.currentFilenameLabelHeader = QtWidgets.QLabel(self.centralwidget)
        self.currentFilenameLabelHeader.setGeometry(QtCore.QRect(40, 60, 201, 16))
        self.currentFilenameLabelHeader.setObjectName("currentFilenameLabelHeader")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(140, 60, 151, 16))
        self.titleLabel.setObjectName("titleLabel")
        self.artistLabel = QtWidgets.QLabel(self.centralwidget)
        self.artistLabel.setGeometry(QtCore.QRect(310, 60, 151, 16))
        self.artistLabel.setObjectName("artistLabel")
        self.albumLabel = QtWidgets.QLabel(self.centralwidget)
        self.albumLabel.setGeometry(QtCore.QRect(480, 60, 101, 16))
        self.albumLabel.setObjectName("albumLabel")
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(600, 60, 51, 16))
        self.yearLabel.setObjectName("yearLabel")
        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        self.genreLabel.setGeometry(QtCore.QRect(670, 60, 101, 16))
        self.genreLabel.setObjectName("genreLabel")
        self.publisherLabel = QtWidgets.QLabel(self.centralwidget)
        self.publisherLabel.setGeometry(QtCore.QRect(790, 60, 101, 16))
        self.publisherLabel.setObjectName("publisherLabel")
        self.keyLabel = QtWidgets.QLabel(self.centralwidget)
        self.keyLabel.setGeometry(QtCore.QRect(910, 60, 31, 16))
        self.keyLabel.setObjectName("keyLabel")
        self.bpmLabel = QtWidgets.QLabel(self.centralwidget)
        self.bpmLabel.setGeometry(QtCore.QRect(960, 60, 31, 16))
        self.bpmLabel.setObjectName("bpmLabel")
        self.beatportLabel = QtWidgets.QLabel(self.centralwidget)
        self.beatportLabel.setGeometry(QtCore.QRect(1010, 60, 441, 16))
        self.beatportLabel.setObjectName("beatportLabel")
        self.beatportButton = QtWidgets.QPushButton(self.centralwidget)
        self.beatportButton.setGeometry(QtCore.QRect(760, 10, 201, 31))
        self.beatportButton.setCheckable(False)
        self.beatportButton.setObjectName("beatportButton")
        self.titleLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleLineEdit.setGeometry(QtCore.QRect(141, 91, 151, 20))
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.publisherLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.publisherLineEdit.setGeometry(QtCore.QRect(791, 91, 101, 20))
        self.publisherLineEdit.setObjectName("publisherLineEdit")
        self.albumLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.albumLineEdit.setGeometry(QtCore.QRect(481, 91, 101, 20))
        self.albumLineEdit.setObjectName("albumLineEdit")
        self.genreLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreLineEdit.setGeometry(QtCore.QRect(671, 91, 101, 20))
        self.genreLineEdit.setObjectName("genreLineEdit")
        self.yearLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yearLineEdit.setGeometry(QtCore.QRect(601, 91, 51, 20))
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.artistLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.artistLineEdit.setGeometry(QtCore.QRect(311, 91, 151, 20))
        self.artistLineEdit.setObjectName("artistLineEdit")
        self.keyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.keyLineEdit.setGeometry(QtCore.QRect(911, 91, 31, 20))
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.bpmLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.bpmLineEdit.setGeometry(QtCore.QRect(961, 91, 31, 20))
        self.bpmLineEdit.setObjectName("bpmLineEdit")
        self.beatportComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.beatportComboBox.setGeometry(QtCore.QRect(1011, 91, 441, 20))
        self.beatportComboBox.setCurrentText("")
        self.beatportComboBox.setObjectName("beatportComboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1501, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MusicMeta"))
        self.openFolderButton.setText(_translate("MainWindow", "Open folder"))
        self.pathLabel.setText(_translate("MainWindow", "This is a text"))
        self.currentFilenameLabel.setText(_translate("MainWindow", "filename.mp3"))
        self.currentFilenameLabelHeader.setText(_translate("MainWindow", "Current filename"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.artistLabel.setText(_translate("MainWindow", "Artist(s)"))
        self.albumLabel.setText(_translate("MainWindow", "Album"))
        self.yearLabel.setText(_translate("MainWindow", "Year"))
        self.genreLabel.setText(_translate("MainWindow", "Genre"))
        self.publisherLabel.setText(_translate("MainWindow", "Publisher"))
        self.keyLabel.setText(_translate("MainWindow", "Key"))
        self.bpmLabel.setText(_translate("MainWindow", "BPM"))
        self.beatportLabel.setText(_translate("MainWindow", "Select beatport data"))
        self.beatportButton.setText(_translate("MainWindow", "Import from beatport for selected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
