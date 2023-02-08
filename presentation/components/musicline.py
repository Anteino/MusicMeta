from PyQt5 import QtCore, QtWidgets

class MusicLine:
    def __init__(self, super, data, index, lineCheckBoxClicked, beatportComboBoxChanged):
        self.index = index
        self.lineCheckBoxClicked = lineCheckBoxClicked
        self.beatportComboBoxChanged = beatportComboBoxChanged

        self.frame = QtWidgets.QFrame(super.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(0, self.index  * 40 + 10, 1701, 21))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.checkBox = self.addWidget(QtWidgets.QCheckBox(self.frame), [10, 0, 17, 20], "", "checkBox")
        self.checkBox.clicked.connect(self.checkBoxClicked)
        
        self.currentFilenameLabel = self.addWidget(QtWidgets.QLabel(self.frame), [40, 0, 201, 20], data.filename, "currentFilenameLabel")
        self.newFilenameLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [250, 0, 151, 20], data.newFilename, "newFilenameLineEdit")
        self.titleLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [420, 0, 151, 20], data.title, "titleLineEdit")
        self.artistLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [590, 0, 151, 20], data.artist, "artistLineEdit")
        self.albumLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [760, 0, 101, 20], data.album, "albumLineEdit")
        self.yearLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [880, 0, 51, 20], data.year, "yearLineEdit")
        self.genreLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [950, 0, 101, 20], data.genre, "genreLineEdit")
        self.publisherLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [1070, 0, 101, 20], data.publisher, "publisherLineEdit")
        self.keyLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [1190, 0, 31, 20], data.key, "keyLineEdit")
        self.bpmLineEdit = self.addWidget(QtWidgets.QLineEdit(self.frame), [1240, 0, 31, 20], data.bpm, "bpmLineEdit")

        self.beatportComboBox = QtWidgets.QComboBox(self.frame)
        self.beatportComboBox.setGeometry(QtCore.QRect(1290, 0, 401, 20))
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