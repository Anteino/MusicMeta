import re
import mutagen
from mutagen.id3 import ID3NoHeaderError, ID3, TIT2, TPE1, TALB, TDRC, TCON, TPUB, TKEY, TBPM, COMM

class MusicData:
    beatportData = {}
    
    def __init__(self, root, filepath):
        self.fullpath = root + '\\' + filepath
        
        self.prepath = re.sub(r'\\[^\\]*$', '', self.fullpath) + '\\'
        self.filename = self.fullpath.replace(self.prepath, '')
        self.name = re.sub(r'\.[^\.]*$', '', self.filename)

        file = mutagen.File(self.fullpath)
        self.duration = file.info.length
        self.extension = self.filename.split('.')[-1].lower()
        
        self.title = self.extractKey(file, 'TIT2')[0]
        self.artist = re.sub(r'\s*,\s*', '/', self.extractKey(file, 'TPE1')[0])
        self.album = self.extractKey(file, 'TALB')[0]
        self.year = self.extractKey(file, 'TDRC')[0]
        self.genre = self.extractKey(file, 'TCON')[0]
        self.publisher = self.extractKey(file, 'TPUB')[0]
        self.key = self.extractKey(file, 'TKEY')[0]
        self.bpm = self.extractKey(file, 'TBPM')[0]
    
    def extractKey(self, file, key):
        if(key in file):
            if(type(file.tags[key].text[0]) == mutagen.id3._specs.ID3TimeStamp):
                return [str(file.tags[key].text[0])]
            else:
                return file.tags[key].text
        else:
            return [""]
    
    def saveTags(self):
        try:
            tags = ID3(self.fullpath)
        except ID3NoHeaderError:
            print("Adding ID3 header")
            tags = ID3()
        
        tags["TIT2"] = TIT2(encoding=3, text=self.title)
        tags["TPE1"] = TPE1(encoding=3, text=self.artist)
        tags["TALB"] = TALB(encoding=3, text=self.album)
        tags["TDRC"] = TDRC(encoding=3, text=self.year)
        tags["TCON"] = TCON(encoding=3, text=self.genre)
        tags["TPUB"] = TPUB(encoding=3, text=self.publisher)
        tags["TKEY"] = TKEY(encoding=3, text=self.key)
        tags["TBPM"] = TBPM(encoding=3, text=self.bpm)

        tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'MusicMeta by Anteino was used to edit meta data of this song.')

        tags.save(self.fullpath)