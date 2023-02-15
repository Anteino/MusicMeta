import json
import xmltodict

def importRbCollection(path):
    try:
        with open(path, encoding='utf8') as xml_file:
            db = xmltodict.parse(xml_file.read())['DJ_PLAYLISTS']['COLLECTION']['TRACK']
            for item in db:
                if("tidal:tracks:" in item["@Location"]):
                    db.remove(item)
            return db
    except:
        return {}