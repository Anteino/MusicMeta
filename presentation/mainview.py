# from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QRect, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFrame, QCheckBox, QScrollArea, QWidget

import sys

sys.path.append('../MusicMeta')
from utils.constants import *
from presentation.components.musicline import MusicLine

class MainView(QMainWindow):
    musicLines = []

    def __init__(self, openFolderClicked, beatportButtonClicked, checkAllClicked, lineCheckBoxClicked, beatportComboBoxChanged, saveButtonClicked, resetTags, openWikiPopup, openDiscogsPopup, rekordboxButtonClicked):
        super(MainView, self).__init__()
        self.openFolderClicked = openFolderClicked
        self.beatportButtonClicked = beatportButtonClicked
        self.checkAllClicked = checkAllClicked
        self.lineCheckBoxClicked = lineCheckBoxClicked
        self.beatportComboBoxChanged = beatportComboBoxChanged
        self.saveButtonClicked = saveButtonClicked
        self.resetTags = resetTags
        self.openWikiPopup = openWikiPopup
        self.openDiscogsPopup = openDiscogsPopup
        self.rekordboxButtonClicked = rekordboxButtonClicked
        self.initUI()
        self.retranslateUi()
    
    def initUI(self):
        self.setObjectName("MainView")
        self.setGeometry(WINDOW_POSITION[0], WINDOW_POSITION[1], WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.setMaximumSize(QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.setAnimated(True)
        
        self.openFolderButton = QPushButton(self)
        self.openFolderButton.setGeometry(QRect(10, 10, 81, 31))
        self.openFolderButton.setCheckable(False)
        self.openFolderButton.setObjectName("openFolderButton")
        self.openFolderButton.clicked.connect(self.openFolderClicked)
        
        self.pathLabel = QLabel(self)
        self.pathLabel.setGeometry(QRect(106, 12, 401, 31))
        self.pathLabel.setText("")
        self.pathLabel.setObjectName("pathLabel")
        
        self.rekordboxButton = QPushButton(self)
        self.rekordboxButton.setGeometry(QRect(760, 10, 161, 31))
        self.rekordboxButton.setCheckable(False)
        self.rekordboxButton.setObjectName("rekordboxButton")
        self.rekordboxButton.clicked.connect(self.rekordboxButtonClicked)
        
        self.beatportButton = QPushButton(self)
        self.beatportButton.setGeometry(QRect(940, 10, 151, 31))
        self.beatportButton.setCheckable(False)
        self.beatportButton.setObjectName("beatportButton")
        self.beatportButton.clicked.connect(self.beatportButtonClicked)
        
        self.saveButton = QPushButton(self)
        self.saveButton.setGeometry(QRect(1111, 10, 201, 31))
        self.saveButton.setCheckable(False)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveButtonClicked)

        self.line = QFrame(self)
        self.line.setGeometry(QRect(0, 50, WINDOW_SIZE[0], 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")

        self.selectAllCheckBox = QCheckBox(self)
        self.selectAllCheckBox.setGeometry(QRect(10, 60, 17, 17))
        self.selectAllCheckBox.setText("")
        self.selectAllCheckBox.setObjectName("selectAllCheckBox")
        self.selectAllCheckBox.clicked.connect(self.checkAllClicked)
        
        self.currentFilenameLabelHeader = QLabel(self)
        self.currentFilenameLabelHeader.setGeometry(QRect(40, 60, 201, 16))
        self.currentFilenameLabelHeader.setObjectName("currentFilenameLabelHeader")

        self.titleLabel = QLabel(self)
        self.titleLabel.setGeometry(QRect(290, 60, 151, 16))
        self.titleLabel.setObjectName("titleLabel")

        self.artistLabel = QLabel(self)
        self.artistLabel.setGeometry(QRect(460, 60, 151, 16))
        self.artistLabel.setObjectName("artistLabel")

        self.albumLabel = QLabel(self)
        self.albumLabel.setGeometry(QRect(630, 60, 101, 16))
        self.albumLabel.setObjectName("albumLabel")

        self.yearLabel = QLabel(self)
        self.yearLabel.setGeometry(QRect(750, 60, 51, 16))
        self.yearLabel.setObjectName("yearLabel")

        self.genreLabel = QLabel(self)
        self.genreLabel.setGeometry(QRect(820, 60, 101, 16))
        self.genreLabel.setObjectName("genreLabel")

        self.publisherLabel = QLabel(self)
        self.publisherLabel.setGeometry(QRect(940, 60, 101, 16))
        self.publisherLabel.setObjectName("publisherLabel")

        self.keyLabel = QLabel(self)
        self.keyLabel.setGeometry(QRect(1060, 60, 31, 16))
        self.keyLabel.setObjectName("keyLabel")

        self.bpmLabel = QLabel(self)
        self.bpmLabel.setGeometry(QRect(1110, 60, 31, 16))
        self.bpmLabel.setObjectName("bpmLabel")

        self.beatportLabel = QLabel(self)
        self.beatportLabel.setGeometry(QRect(1170, 60, 531, 16))
        self.beatportLabel.setObjectName("beatportLabel")
        
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QRect(0, 80, WINDOW_SIZE[0], WINDOW_SIZE[1] - 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(WINDOW_TITLE)
        self.openFolderButton.setText(_translate("MainWindow", OPEN_FOLDER))
        self.rekordboxButton.setText(_translate("MainWindow", IMPORT_REKORDBOX_DB))
        self.beatportButton.setText(_translate("MainWindow", IMPORT_BEATPORT))
        self.saveButton.setText(_translate("MainWindow", SAVE))
        self.currentFilenameLabelHeader.setText(_translate("MainWindow", CURRENT_FILENAME))
        self.titleLabel.setText(_translate("MainWindow", TITLE))
        self.artistLabel.setText(_translate("MainWindow", ARTIST))
        self.albumLabel.setText(_translate("MainWindow", ALBUM))
        self.yearLabel.setText(_translate("MainWindow", YEAR))
        self.genreLabel.setText(_translate("MainWindow", GENRE))
        self.publisherLabel.setText(_translate("MainWindow", PUBLISHER))
        self.keyLabel.setText(_translate("MainWindow", KEY))
        self.bpmLabel.setText(_translate("MainWindow", BPM))
        self.beatportLabel.setText(_translate("MainWindow", SELECT_DATA))
    
    def setPathLabel(self, path):
        self.pathLabel.setText(path)
    
    def repopulateMusicData(self, data):
        self.musicLines = []
        
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setFixedWidth(1701)
        self.scrollAreaWidgetContents.setMinimumHeight(max(len(data) * 80 + 10, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        for item in data:
            self.addMusicDataFrame(item)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    
    def updateBeatportData(self, musicData):
        for i in range(len(musicData)):
            data = musicData[i].beatportData
            if(len(data["tracks"]) != 0):
                self.musicLines[i].beatportComboBox.clear()
                for track in data["tracks"]:
                    line = track["name"] +  " (" + track["mix_name"] + ") - " + track["artists"][0]["name"]
                    for j in range(1, len(track["artists"])):
                        artist = track["artists"][j]
                        line += ", " + artist["name"]
                    self.musicLines[i].beatportComboBox.addItem(line)
    
    def addMusicDataFrame(self, data):
        self.musicLines.append( MusicLine(
                                            self,
                                            data,
                                            len(self.musicLines),
                                            self.lineCheckBoxClicked,
                                            self.beatportComboBoxChanged,
                                            self.resetTags,
                                            self.openWikiPopup,
                                            self.openDiscogsPopup
                                        ))