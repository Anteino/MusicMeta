# from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QFrame, QCheckBox, QLabel, QLineEdit, QPushButton, QComboBox, QCommandLinkButton
from time import time
from sys import path

path.append('../../MusicMeta')
from utils.constants import *
from utils.resourcepath import resourcePath

class MusicLine:
    def __init__(self, super, data, index, lineCheckBoxClicked, beatportComboBoxChanged, resetTags, openWikiPopup, openDiscogsPopup):
        self.time = 0

        self.index = index
        self.lineCheckBoxClicked = lineCheckBoxClicked
        self.beatportComboBoxChanged = beatportComboBoxChanged
        self.resetTags = resetTags
        self.openWikiPopUp = openWikiPopup
        self.openDiscogsPopup = openDiscogsPopup

        self.frame = QFrame(super.scrollAreaWidgetContents)
        self.frame.setGeometry(QRect(0, self.index  * 80 + 10, 1711, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")

        self.checkBox = self.addWidget(QCheckBox(self.frame), [10, 0, 17, 20], "", "checkBox")
        self.checkBox.clicked.connect(self.checkBoxClicked)
        self.currentFilenameLabel = self.addWidget(QLabel(self.frame), [40, 0, 201, 20], data.filename, "currentFilenameLabel")

        self.resetButton = self.addButton([245, -7, 31, 31], "undo.png", self.resetTagsClicked)
        self.copyTagsButton = self.addButton([245, 23, 31, 31], "arrow_up.png", self.copyAllTags)

        self.titleLineEdit = self.addWidget(QLineEdit(self.frame), [290, 0, 151, 20], data.title, "titleLineEdit")
        self.artistLineEdit = self.addWidget(QLineEdit(self.frame), [460, 0, 151, 20], data.artist, "artistLineEdit")
        self.albumLineEdit = self.addWidget(QLineEdit(self.frame), [630, 0, 101, 20], data.album, "albumLineEdit")
        self.yearLineEdit = self.addWidget(QLineEdit(self.frame), [750, 0, 51, 20], data.year, "yearLineEdit")
        self.genreLineEdit = self.addWidget(QLineEdit(self.frame), [820, 0, 101, 20], data.genre, "genreLineEdit")
        self.publisherLineEdit = self.addWidget(QLineEdit(self.frame), [940, 0, 101, 20], data.publisher, "publisherLineEdit")
        self.keyLineEdit = self.addWidget(QLineEdit(self.frame), [1060, 0, 31, 20], data.key, "keyLineEdit")
        self.bpmLineEdit = self.addWidget(QLineEdit(self.frame), [1110, 0, 41, 20], data.bpm, "bpmLineEdit")
        
        self.titleButton = self.addWidget(QPushButton(self.frame), [290, 30, 151, 20], data.title, "titleButton")
        self.artistButton = self.addWidget(QPushButton(self.frame), [460, 30, 151, 20], data.artist, "artistButton")
        self.albumButton = self.addWidget(QPushButton(self.frame), [630, 30, 101, 20], data.album, "albumButton")
        self.yearButton = self.addWidget(QPushButton(self.frame), [750, 30, 51, 20], data.year, "yearButton")
        self.genreButton = self.addWidget(QPushButton(self.frame), [820, 30, 101, 20], data.genre, "genreButton")
        self.publisherButton = self.addWidget(QPushButton(self.frame), [940, 30, 101, 20], data.publisher, "publisherButton")
        self.keyButton = self.addWidget(QPushButton(self.frame), [1060, 30, 31, 20], data.key, "keyButton")
        self.bpmButton = self.addWidget(QPushButton(self.frame), [1110, 30, 41, 20], data.bpm, "bpmButton")

        self.beatportComboBox = QComboBox(self.frame)
        self.beatportComboBox.setGeometry(QRect(1170, 0, 531, 20))
        self.beatportComboBox.setCurrentText("")
        self.beatportComboBox.setObjectName("beatportComboBox")
        self.beatportComboBox.activated[int].connect(self.onComboBoxChanged)

        self.wikiButton = self.addWidget(QPushButton(self.frame), [1170, 30, 71, 20], OPEN_WIKI_PAGE, "wikiButton")
        self.discogsButton = self.addWidget(QPushButton(self.frame), [1260, 30, 91, 20], OPEN_DISCOGS_PAGE, "discogsButton")
    
    def onComboBoxChanged(self, comboBoxIndex):
        self.beatportComboBoxChanged(self.index, comboBoxIndex)
    
    def wikiButtonClicked(self):
        self.openWikiPopUp(self.index)
    
    def discogsButtonClicked(self):
        self.openDiscogsPopup(self.index)
    
    def addWidget(self, widgetType, geometry, text, name):
        widget = widgetType
        if("wiki" in name):
            widget.clicked.connect(self.wikiButtonClicked)
        elif("discogs" in name):
            widget.clicked.connect(self.discogsButtonClicked)
        elif("Button" in name):
            widget.setStyleSheet("QPushButton { text-align: left; }")
            lineEdit = self.frame.findChild(QLineEdit, name.replace("Button", "LineEdit"))
            widget.clicked.connect(lambda: self.checkDoubleClick(lambda: lineEdit.setText(widget.text())))
            
        widget.setGeometry(QRect(geometry[0], geometry[1], geometry[2], geometry[3]))
        widget.setText(text)
        widget.setObjectName(name)

        return widget

    def checkDoubleClick(self, function):
        if time() - self.time < 0.25:
            function()
        else:
            self.time = time()
    
    def addButton(self, geometry, iconName, function):
        self.commandLinkButton = QCommandLinkButton(self.frame)
        self.commandLinkButton.setGeometry(QRect(geometry[0], geometry[1], geometry[2], geometry[3]))
        self.commandLinkButton.setLayoutDirection(Qt.LeftToRight)
        self.commandLinkButton.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(resourcePath("assets/icons/" + iconName)), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QSize(18, 20))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(function)
    
    def checkBoxClicked(self):
        self.lineCheckBoxClicked(self.index)
    
    def resetTagsClicked(self):
        self.resetTags(self.index)
    
    def copyAllTags(self):
        self.titleLineEdit.setText(self.titleButton.text())
        self.artistLineEdit.setText(self.artistButton.text())
        self.albumLineEdit.setText(self.albumButton.text())
        self.yearLineEdit.setText(self.yearButton.text())
        self.genreLineEdit.setText(self.genreButton.text())
        self.publisherLineEdit.setText(self.publisherButton.text())
        self.keyLineEdit.setText(self.keyButton.text())
        self.bpmLineEdit.setText(self.bpmButton.text())