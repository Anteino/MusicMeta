import asyncio
import aiohttp
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
import sys

sys.path.append('../MusicMeta')
from utils.constants import *
from utils.musicReader import musicReader as reader
from model.beatportSearch import beatportSearch as search

from presentation.mainview import MainView

class MainViewController():
    root = "C:\\Users\\admin\\Music\\SoundCloud\\Flauwe shit"
    musicData = []

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainView = MainView(self.openFolderClicked, self.beatportButtonClicked, self.checkAllClicked, self.lineCheckBoxClicked)
    
    def show(self):
        self.mainView.selectAllCheckBox.setChecked(False)
        self.mainView.setPathLabel(self.root)
        self.musicData = reader(self.root)
        self.mainView.repopulateMusicData(self.musicData)

        self.mainView.show()
        sys.exit(self.app.exec_())
    
    def openFolderClicked(self):
        self.root = QtWidgets.QFileDialog.getExistingDirectory(self.mainView, OPEN_FOLDER)
        if(self.root == ''):
            return
        self.mainView.selectAllCheckBox.setChecked(False)
        self.mainView.setPathLabel(self.root)
        self.musicData = reader(self.root)
        self.mainView.repopulateMusicData(self.musicData)
    
    def beatportButtonClicked(self):
        pass

    def checkAllClicked(self, state):
        for item in self.mainView.musicLines:
            item.checkBox.setChecked(state)
    
    def lineCheckBoxClicked(self, index):
        if(self.mainView.musicLines[index].checkBox.isChecked() == False):
            self.mainView.selectAllCheckBox.setChecked(False)
        elif(len(self.mainView.musicLines) > 0):
            tmp = self.mainView.musicLines[0].checkBox.isChecked()
            for i in range(len(self.mainView.musicLines)):
                if(self.mainView.musicLines[i].checkBox.isChecked() != tmp): return
            self.mainView.selectAllCheckBox.setChecked(tmp)