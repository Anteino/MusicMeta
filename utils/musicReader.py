import os
import re
import soundfile as sf

from utils.constants import ALLOWED_EXTENSIONS

#   Taken + adapted from the question asked and answered here:
#       https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

class musicPath:
    prepath = ""
    filename = ""
    fullpath = ""
    duration = ""

    def __init__(self, root, filepath):
        self.fullpath = root + '\\' + filepath
        
        self.prepath = re.sub(r'\\[^\\]*$', '', self.fullpath) + '\\'
        self.filename = self.fullpath.replace(self.prepath, '')

        f = sf.SoundFile(self.fullpath)
        self.duration = f.frames / f.samplerate

def _get_dir_content(path, include_folders, recursive):
    entries = os.listdir(path)
    for entry in entries:
        entry_with_path = os.path.join(path, entry)
        if os.path.isdir(entry_with_path):
            if include_folders:
                yield entry_with_path
            if recursive:
                for sub_entry in _get_dir_content(entry_with_path, include_folders, recursive):
                    yield sub_entry
        else:
            yield entry_with_path


def get_dir_content(path, include_folders=True, recursive=True, prepend_folder_name=True):
    path_len = len(path) + len(os.path.sep)
    for item in _get_dir_content(path, include_folders, recursive):
        yield item if prepend_folder_name else item[path_len:]


def _get_dir_content_old(path, include_folders, recursive):
    entries = os.listdir(path)
    ret = list()
    for entry in entries:
        entry_with_path = os.path.join(path, entry)
        if os.path.isdir(entry_with_path):
            if include_folders:
                ret.append(entry_with_path)
            if recursive:
                ret.extend(_get_dir_content_old(entry_with_path, include_folders, recursive))
        else:
            ret.append(entry_with_path)
    return ret

def get_dir_content_old(path, include_folders=True, recursive=True, prepend_folder_name=True):
    path_len = len(path) + len(os.path.sep)
    return [item if prepend_folder_name else item[path_len:] for item in _get_dir_content_old(path, include_folders, recursive)]

def musicReader(path):
    tmp = get_dir_content_old(path, include_folders=False, recursive=True, prepend_folder_name=False)
    
    contents = []
    for item in tmp:
        extension = item.split('.')[-1].lower()
        if(extension in ALLOWED_EXTENSIONS):
            contents.append(musicPath(path, item))
    
    return contents

