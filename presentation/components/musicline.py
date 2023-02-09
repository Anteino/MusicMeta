from PyQt5 import QtCore, QtWidgets, QtGui
import sys

sys.path.append('../../MusicMeta')

class MusicLine:
    def __init__(self, super, data, index, lineCheckBoxClicked, beatportComboBoxChanged, resetTags):
        self.index = index
        self.lineCheckBoxClicked = lineCheckBoxClicked
        self.beatportComboBoxChanged = beatportComboBoxChanged
        self.resetTags = resetTags

        self.frame = QtWidgets.QFrame(super.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, self.index  * 40 + 10, 1701, 21))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.checkBox = self.addWidget(QtWidgets.QCheckBox(self.frame), [10, 0, 17, 20], "", "checkBox")
        self.checkBox.clicked.connect(self.checkBoxClicked)
        self.currentFilenameLabel = self.addWidget(QtWidgets.QLabel(self.frame), [40, 0, 201, 20], data.filename, "currentFilenameLabel")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(245, -7, 31, 31))
        self.commandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icons/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(18, 20))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.resetTagsClicked)

        self.titleLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [290, 0, 151, 20], data.title, "titleLineEdit")
        self.artistLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [460, 0, 151, 20], data.artist, "artistLineEdit")
        self.albumLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [630, 0, 101, 20], data.album, "albumLineEdit")
        self.yearLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [750, 0, 51, 20], data.year, "yearLineEdit")
        self.genreLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [820, 0, 101, 20], data.genre, "genreLineEdit")
        self.publisherLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [940, 0, 101, 20], data.publisher, "publisherLineEdit")
        self.keyLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [1060, 0, 31, 20], data.key, "keyLineEdit")
        self.bpmLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [1110, 0, 31, 20], data.bpm, "bpmLineEdit")

        self.beatportComboBox = QtWidgets.QComboBox(self.frame)
        self.beatportComboBox.setGeometry(QtCore.QRect(1160, 0, 531, 20))
        self.beatportComboBox.setCurrentText("")
        self.beatportComboBox.setObjectName("beatportComboBox")
        self.beatportComboBox.activated[int].connect(self.onComboBoxChanged)
    
    def onComboBoxChanged(self, comboBoxIndex):
        self.beatportComboBoxChanged(self.index, comboBoxIndex)
    
    def addWidget(self, widgetType, geometry, text, name):
        widget = widgetType
        widget.setGeometry(QtCore.QRect(geometry[0], geometry[1], geometry[2], geometry[3]))
        widget.setText(text)
        widget.setObjectName(name)
        return widget
    
    def checkBoxClicked(self):
        self.lineCheckBoxClicked(self.index)
    
    def resetTagsClicked(self):
        self.resetTags(self.index)