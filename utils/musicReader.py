from sys import path
from os import listdir
from os.path import isdir, join, sep

path.append('../MusicMeta')
from utils.constants import ALLOWED_EXTENSIONS
from classes.musicdata import MusicData

#   Taken + adapted from the question asked and answered here:
#       https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory


def _get_dir_content(path, include_folders, recursive):
    entries = listdir(path)
    for entry in entries:
        entry_with_path = join(path, entry)
        if isdir(entry_with_path):
            if include_folders:
                yield entry_with_path
            if recursive:
                for sub_entry in _get_dir_content(entry_with_path, include_folders, recursive):
                    yield sub_entry
        else:
            yield entry_with_path


def get_dir_content(path, include_folders=True, recursive=True, prepend_folder_name=True):
    path_len = len(path) + len(sep)
    for item in _get_dir_content(path, include_folders, recursive):
        yield item if prepend_folder_name else item[path_len:]


def _get_dir_content_old(path, include_folders, recursive):
    entries = listdir(path)
    ret = list()
    for entry in entries:
        entry_with_path = join(path, entry)
        if isdir(entry_with_path):
            if include_folders:
                ret.append(entry_with_path)
            if recursive:
                ret.extend(_get_dir_content_old(entry_with_path, include_folders, recursive))
        else:
            ret.append(entry_with_path)
    return ret

def get_dir_content_old(path, include_folders=True, recursive=True, prepend_folder_name=True):
    path_len = len(path) + len(sep)
    return [item if prepend_folder_name else item[path_len:] for item in _get_dir_content_old(path, include_folders, recursive)]

def musicReader(path):
    tmp = get_dir_content_old(path, include_folders=False, recursive=True, prepend_folder_name=False)
    
    contents = []
    for item in tmp:
        extension = item.split('.')[-1].lower()
        if(extension in ALLOWED_EXTENSIONS):
            contents.append(MusicData(path, item))
    
    return contents

