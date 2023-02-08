from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

sys.path.append('../MusicMeta')
from utils.constants import *
from presentation.components.musicline import MusicLine

class MainView(QMainWindow):
    musicLines = []

    def __init__(self, openFolderClicked, beatportButtonClicked, checkAllClicked, lineCheckBoxClicked, beatportComboBoxChanged, saveButtonClicked):
        super(MainView, self).__init__()
        self.openFolderClicked = openFolderClicked
        self.beatportButtonClicked = beatportButtonClicked
        self.checkAllClicked = checkAllClicked
        self.lineCheckBoxClicked = lineCheckBoxClicked
        self.beatportComboBoxChanged = beatportComboBoxChanged
        self.saveButtonClicked = saveButtonClicked
        self.initUI()
        self.retranslateUi()
    
    def initUI(self):
        self.setObjectName("MainView")
        self.setGeometry(WINDOW_POSITION[0], WINDOW_POSITION[1], WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.setMinimumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.setMaximumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.setAnimated(True)
        
        self.openFolderButton = QtWidgets.QPushButton(self)
        self.openFolderButton.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.openFolderButton.setCheckable(False)
        self.openFolderButton.setObjectName("openFolderButton")
        self.openFolderButton.clicked.connect(self.openFolderClicked)
        
        self.pathLabel = QtWidgets.QLabel(self)
        self.pathLabel.setGeometry(QtCore.QRect(106, 12, 401, 31))
        self.pathLabel.setText("")
        self.pathLabel.setObjectName("pathLabel")
        
        self.beatportButton = QtWidgets.QPushButton(self)
        self.beatportButton.setGeometry(QtCore.QRect(760, 10, 151, 31))
        self.beatportButton.setCheckable(False)
        self.beatportButton.setObjectName("beatportButton")
        self.beatportButton.clicked.connect(self.beatportButtonClicked)
        
        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setGeometry(QtCore.QRect(931, 10, 201, 31))
        self.saveButton.setCheckable(False)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveButtonClicked)

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(0, 50, WINDOW_SIZE[0], 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.selectAllCheckBox = QtWidgets.QCheckBox(self)
        self.selectAllCheckBox.setGeometry(QtCore.QRect(10, 60, 17, 17))
        self.selectAllCheckBox.setText("")
        self.selectAllCheckBox.setObjectName("selectAllCheckBox")
        self.selectAllCheckBox.clicked.connect(self.checkAllClicked)
        
        self.currentFilenameLabelHeader = QtWidgets.QLabel(self)
        self.currentFilenameLabelHeader.setGeometry(QtCore.QRect(40, 60, 201, 16))
        self.currentFilenameLabelHeader.setObjectName("currentFilenameLabelHeader")

        self.newFilenameLabelHeader = QtWidgets.QLabel(self)
        self.newFilenameLabelHeader.setGeometry(QtCore.QRect(250, 60, 151, 16))
        self.newFilenameLabelHeader.setObjectName("newFilenameLabelHeader")

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(QtCore.QRect(420, 60, 151, 16))
        self.titleLabel.setObjectName("titleLabel")

        self.artistLabel = QtWidgets.QLabel(self)
        self.artistLabel.setGeometry(QtCore.QRect(590, 60, 151, 16))
        self.artistLabel.setObjectName("artistLabel")

        self.albumLabel = QtWidgets.QLabel(self)
        self.albumLabel.setGeometry(QtCore.QRect(760, 60, 101, 16))
        self.albumLabel.setObjectName("albumLabel")

        self.yearLabel = QtWidgets.QLabel(self)
        self.yearLabel.setGeometry(QtCore.QRect(880, 60, 51, 16))
        self.yearLabel.setObjectName("yearLabel")

        self.genreLabel = QtWidgets.QLabel(self)
        self.genreLabel.setGeometry(QtCore.QRect(950, 60, 101, 16))
        self.genreLabel.setObjectName("genreLabel")

        self.publisherLabel = QtWidgets.QLabel(self)
        self.publisherLabel.setGeometry(QtCore.QRect(1070, 60, 101, 16))
        self.publisherLabel.setObjectName("publisherLabel")

        self.keyLabel = QtWidgets.QLabel(self)
        self.keyLabel.setGeometry(QtCore.QRect(1190, 60, 31, 16))
        self.keyLabel.setObjectName("keyLabel")

        self.bpmLabel = QtWidgets.QLabel(self)
        self.bpmLabel.setGeometry(QtCore.QRect(1240, 60, 31, 16))
        self.bpmLabel.setObjectName("bpmLabel")

        self.beatportLabel = QtWidgets.QLabel(self)
        self.beatportLabel.setGeometry(QtCore.QRect(1290, 60, 201, 16))
        self.beatportLabel.setObjectName("beatportLabel")
        
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(0, 80, WINDOW_SIZE[0], WINDOW_SIZE[1] - 80))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(WINDOW_TITLE)
        self.openFolderButton.setText(_translate("MainWindow", OPEN_FOLDER))
        self.beatportButton.setText(_translate("MainWindow", IMPORT_BEATPORT))
        self.saveButton.setText(_translate("MainWindow", SAVE))
        self.currentFilenameLabelHeader.setText(_translate("MainWindow", CURRENT_FILENAME))
        self.newFilenameLabelHeader.setText(_translate("MainWindow", NEW_FILENAME))
        self.titleLabel.setText(_translate("MainWindow", TITLE))
        self.artistLabel.setText(_translate("MainWindow", ARTIST))
        self.albumLabel.setText(_translate("MainWindow", ALBUM))
        self.yearLabel.setText(_translate("MainWindow", YEAR))
        self.genreLabel.setText(_translate("MainWindow", GENRE))
        self.publisherLabel.setText(_translate("MainWindow", PUBLISHER))
        self.keyLabel.setText(_translate("MainWindow", KEY))
        self.bpmLabel.setText(_translate("MainWindow", BPM))
        self.beatportLabel.setText(_translate("MainWindow", SELECT_BEATPORT_DATA))
    
    def setPathLabel(self, path):
        self.pathLabel.setText(path)
    
    def repopulateMusicData(self, data):
        self.musicLines = []
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setFixedWidth(1701)
        self.scrollAreaWidgetContents.setMinimumHeight(max(len(data) * 40 + 10, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        for item in data:
            self.addMusicDataFrame(item)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    
    def updateMusicLine(self, index, data):
        self.musicLines[index].newFilenameLineEdit.setText(data.newFilename)
        self.musicLines[index].titleLineEdit.setText(data.title)
        self.musicLines[index].artistLineEdit.setText(data.artist)
        self.musicLines[index].albumLineEdit.setText(data.album)
        self.musicLines[index].yearLineEdit.setText(data.year)
        self.musicLines[index].genreLineEdit.setText(data.genre)
        self.musicLines[index].publisherLineEdit.setText(data.publisher)
        self.musicLines[index].keyLineEdit.setText(data.key)
        self.musicLines[index].bpmLineEdit.setText(data.bpm)
    
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
                    line += " (publ: " + track["release"]["label"]["name"] + ")"
                    self.musicLines[i].beatportComboBox.addItem(line)
    
    def addMusicDataFrame(self, data):
        self.musicLines.append(MusicLine(self, data, len(self.musicLines), self.lineCheckBoxClicked, self.beatportComboBoxChanged))