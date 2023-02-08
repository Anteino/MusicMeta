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
    root = ""
    musicData = []

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainView = MainView(self.openFolderClicked, self.beatportButtonClicked, self.checkAllClicked, self.lineCheckBoxClicked, self.beatportComboBoxChanged, self.saveButtonClicked)
    
    def show(self):
        self.mainView.selectAllCheckBox.setChecked(False)
        self.mainView.setPathLabel(self.root)
        if(self.root != ""):
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
        try:
            self.loop = asyncio.get_event_loop()
            self.loop.run_until_complete(self.collectBeatportData())
        except:
            pass
    
    async def collectBeatportData(self):
        tasks = []

        for index in range(len(self.musicData)):
            item = self.musicData[index]
            tasks.append(self.loop.create_task(search(item.name, index, self.setBeatportData)))
        
        await asyncio.wait(tasks)

        self.updateBeatportDataToView()
    
    def setBeatportData(self, index, data):
        self.musicData[index].beatportData = data
    
    def updateBeatportDataToView(self):
        self.mainView.updateBeatportData(self.musicData)

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
    
    def beatportComboBoxChanged(self, musicIndex, comboBoxIndex):
        track = self.musicData[musicIndex].beatportData["tracks"][comboBoxIndex]

        title = track["name"] +  " (" + track["mix_name"] + ")"

        artists = track["artists"][0]["name"]
        for j in range(1, len(track["artists"])):
            artist = track["artists"][j]
            artists += "/" + artist["name"]

        newFilename = title + " - "  + artists
        ext = self.musicData[musicIndex].extension
        album = track["release"]["name"]
        year = track["new_release_date"].split("-")[0]
        genre = track["genre"]["name"]
        publisher = track["release"]["label"]["name"]
        key = str(track["key"]["camelot_number"]) + track["key"]["camelot_letter"]
        bpm = str(track["bpm"])

        self.musicData[musicIndex].newFilename = newFilename + "." + ext
        self.musicData[musicIndex].title = title
        self.musicData[musicIndex].artist = artists
        self.musicData[musicIndex].album = album
        self.musicData[musicIndex].year = year
        self.musicData[musicIndex].genre = genre
        self.musicData[musicIndex].publisher = publisher
        self.musicData[musicIndex].key = key
        self.musicData[musicIndex].bpm = bpm

        self.mainView.updateMusicLine(musicIndex, self.musicData[musicIndex])
        self.mainView.musicLines[musicIndex].checkBox.setChecked(True)
        self.lineCheckBoxClicked(musicIndex)
    
    def saveButtonClicked(self):
        for index in range(len(self.mainView.musicLines)):
            musicLine = self.mainView.musicLines[index]

            if(musicLine.checkBox.isChecked()):
                tmp = musicLine.newFilenameLineEdit.text()
                ext = self.musicData[index].extension
                if(tmp.find(ext) == -1):
                    tmp = tmp + "." + ext
                self.musicData[index].newFilename = tmp
                self.musicData[index].title = musicLine.titleLineEdit.text()
                self.musicData[index].artist = musicLine.artistLineEdit.text()
                self.musicData[index].album = musicLine.albumLineEdit.text()
                self.musicData[index].year = musicLine.yearLineEdit.text()
                self.musicData[index].genre = musicLine.genreLineEdit.text()
                self.musicData[index].publisher = musicLine.publisherLineEdit.text()
                self.musicData[index].key = musicLine.keyLineEdit.text()
                self.musicData[index].bpm = musicLine.bpmLineEdit.text()

                self.musicData[index].saveTags()