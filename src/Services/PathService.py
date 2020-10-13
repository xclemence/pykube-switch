import platform 

from pathlib import Path
from os import path
from urllib.parse import unquote, urlparse


def url_to_path(file_url):
    url = file_url
    if platform.system() == "Windows":
        url = file_url.replace("file:///", "file://")

    return unquote(urlparse(url).path)


def find_available_name(directory, file_name):
    index = 1
    available_name = file_name

    while path.isfile(path.join(directory, available_name)):
        available_name = f"{file_name}_{index}"
        index += 1

    return available_name


def get_working_directory():
    return path.join(str(Path.home()), '.pykubeswitch')


def get_kube_directory():
    return path.join(str(Path.home()), '.kube')
