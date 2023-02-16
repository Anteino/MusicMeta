from asyncio import get_event_loop, wait
from PyQt5.QtWidgets import QDialog, QFileDialog, QApplication
from urllib.parse import unquote
from sys import path, argv, exit

path.append('../MusicMeta')
from utils.constants import *
from utils.musicReader import musicReader as reader
from utils.importRbCollection import importRbCollection as collect
from model.beatportSearch import beatportSearch as search
from model.wikiSearch import wikiSearch

from presentation.mainview import MainView
from presentation.components.wikidialog import WikiDialog

class MainViewController():
    root = ""
    musicData = []
    rbDB = []

    def __init__(self):
        self.app = QApplication(argv)
        self.mainView = MainView(self.openFolderClicked, self.beatportButtonClicked, self.checkAllClicked, self.lineCheckBoxClicked, self.beatportComboBoxChanged, self.saveButtonClicked, self.resetTags, self.openWikiPopup, self.rekordboxButtonClicked)
    
    def show(self):
        self.mainView.selectAllCheckBox.setChecked(False)
        self.mainView.setPathLabel(self.root)
        if(self.root != ""):
            self.musicData = reader(self.root)
            self.mainView.repopulateMusicData(self.musicData)

        self.mainView.show()
        exit(self.app.exec_())
    
    def openFolderClicked(self):
        self.root = QFileDialog.getExistingDirectory(self.mainView, OPEN_FOLDER)
        if(self.root != ''):
            self.mainView.selectAllCheckBox.setChecked(False)
            self.mainView.setPathLabel(self.root)
            self.musicData = reader(self.root)
            self.mainView.repopulateMusicData(self.musicData)
            self.overWriteRekordboxData()
    
    def rekordboxButtonClicked(self):
        path = QFileDialog.getOpenFileName(self.mainView, IMPORT_REKORDBOX_DB, "", "XML files (*.xml)")[0]
        if(path == ''):
            return
        self.rbDB = collect(path)
        self.overWriteRekordboxData()
    
    def overWriteRekordboxData(self):
        tempDB = self.rbDB
        for track in tempDB:
            for index in range(len(self.musicData)):
                musicLine = self.mainView.musicLines[index]
                try:
                    filename = self.musicData[index].filename
                    location = unquote(track["@Location"].replace("\\", "/").split("/")[-1])
                    if(location == filename):
                        changed = False
                        if(musicLine.keyButton.text() == ""):
                            changed = True
                            key = track["@Tonality"]
                            musicLine.keyButton.setText(key)
                            musicLine.keyLineEdit.setText(key)
                            self.musicData[index].key = key
                        if(musicLine.bpmButton.text() == ""):
                            changed = True
                            bpm = track["@AverageBpm"]
                            musicLine.bpmButton.setText(bpm)
                            musicLine.bpmLineEdit.setText(bpm)
                            self.musicData[index].bpm = bpm
                        if(changed):
                            self.mainView.musicLines[index].checkBox.setChecked(True)
                            self.lineCheckBoxClicked(index)
                        break
                except:
                    pass
    
    def openWikiPopup(self, index):
        try:
            html = wikiSearch(self.musicData[index].name)
            self.Dialog = QDialog()
            self.ui = WikiDialog()
            self.ui.setupUi(self.Dialog, html, self.musicData[index].name)
            self.Dialog.show()
        except Exception as e:
            print("An exception occuring during handling of wikipedia request: ", end="")
            print(e)
    
    def beatportButtonClicked(self):
        try:
            self.loop = get_event_loop()
            self.loop.run_until_complete(self.collectBeatportData())
        except:
            pass
    
    async def collectBeatportData(self):
        tasks = []

        for index in range(len(self.musicData)):
            item = self.musicData[index]
            tasks.append(self.loop.create_task(search(item.name, index, self.setBeatportData)))
        
        await wait(tasks)

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
    
    def resetTags(self, index):
        musicLine = self.mainView.musicLines[index]
        musicData = self.musicData[index]
        musicData.beatportId = musicData.oldBeatportId

        musicLine.titleLineEdit.setText(musicData.title)
        musicLine.artistLineEdit.setText(musicData.artist)
        musicLine.albumLineEdit.setText(musicData.album)
        musicLine.yearLineEdit.setText(musicData.year)
        musicLine.genreLineEdit.setText(musicData.genre)
        musicLine.publisherLineEdit.setText(musicData.publisher)
        musicLine.keyLineEdit.setText(musicData.key)
        musicLine.bpmLineEdit.setText(musicData.bpm)

        musicLine.titleButton.setText(musicData.title)
        musicLine.artistButton.setText(musicData.artist)
        musicLine.albumButton.setText(musicData.album)
        musicLine.yearButton.setText(musicData.year)
        musicLine.genreButton.setText(musicData.genre)
        musicLine.publisherButton.setText(musicData.publisher)
        musicLine.keyButton.setText(musicData.key)
        musicLine.bpmButton.setText(musicData.bpm)
    
    def beatportComboBoxChanged(self, musicIndex, comboBoxIndex):
        track = self.musicData[musicIndex].beatportData["tracks"][comboBoxIndex]
        self.musicData[musicIndex].beatportId = str(track["id"])

        title = track["name"] +  " (" + track["mix_name"] + ")"

        artists = track["artists"][0]["name"]
        for j in range(1, len(track["artists"])):
            artist = track["artists"][j]
            artists += "/" + artist["name"]

        album = track["release"]["name"]
        year = track["new_release_date"].split("-")[0]
        genre = track["genre"]["name"]
        publisher = track["release"]["label"]["name"]
        key = str(track["key"]["camelot_number"]) + track["key"]["camelot_letter"]
        bpm = str(track["bpm"])

        musicLine = self.mainView.musicLines[musicIndex]

        musicLine.titleButton.setText(title)
        musicLine.artistButton.setText(artists)
        musicLine.albumButton.setText(album)
        musicLine.yearButton.setText(year)
        musicLine.genreButton.setText(genre)
        musicLine.publisherButton.setText(publisher)
        musicLine.keyButton.setText(key)
        musicLine.bpmButton.setText(bpm)

        self.mainView.musicLines[musicIndex].checkBox.setChecked(True)
        self.lineCheckBoxClicked(musicIndex)
    
    def saveButtonClicked(self):
        for index in range(len(self.mainView.musicLines)):
            musicLine = self.mainView.musicLines[index]

            if(musicLine.checkBox.isChecked()):
                self.musicData[index].title = musicLine.titleLineEdit.text()
                self.musicData[index].artist = musicLine.artistLineEdit.text()
                self.musicData[index].album = musicLine.albumLineEdit.text()
                self.musicData[index].year = musicLine.yearLineEdit.text()
                self.musicData[index].genre = musicLine.genreLineEdit.text()
                self.musicData[index].publisher = musicLine.publisherLineEdit.text()
                self.musicData[index].key = musicLine.keyLineEdit.text()
                self.musicData[index].bpm = musicLine.bpmLineEdit.text()

                self.musicData[index].saveTags()