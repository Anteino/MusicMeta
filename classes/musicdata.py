import re
import mutagen

class MusicData:
    beatportData = []
    
    def __init__(self, root, filepath):
        self.fullpath = root + '\\' + filepath
        
        self.prepath = re.sub(r'\\[^\\]*$', '', self.fullpath) + '\\'
        self.filename = self.fullpath.replace(self.prepath, '')
        self.name = re.sub(r'\.[^\.]*$', '', self.filename)

        file = mutagen.File(self.fullpath)
        self.duration = file.info.length
        self.extension = self.filename.split('.')[-1].lower()
        
        self.title = self.extractKey(file, 'TIT2')[0]
        self.artist = self.extractKey(file, 'TPE1')[0]
        self.album = self.extractKey(file, 'TALB')[0]
        self.year = self.extractKey(file, 'TDRC')[0]
        self.genre = self.extractKey(file, 'TCON')[0]
        self.publisher = self.extractKey(file, 'TPUB')[0]
        self.key = self.extractKey(file, 'TKEY')[0]
        self.bpm = self.extractKey(file, 'TBPM')[0]

        if((self.title != "") & (self.artist != "")):
            self.newFilename = self.title + " - " + self.artist + "." + self.extension
        else:
            self.newFilename = ""
    
    def extractKey(self, file, key):
        if(key in file):
            if(type(file.tags[key].text[0]) == mutagen.id3._specs.ID3TimeStamp):
                return [str(file.tags[key].text[0])]
            else:
                return file.tags[key].text
        else:
            return [""]