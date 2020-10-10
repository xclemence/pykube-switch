import platform 

from pathlib import Path
from os import path
from urllib.parse import unquote, urlparse

from models.Cluster import Cluster

class PathService:

    @classmethod
    def url_to_path(cls, file_url):
        url = file_url
        if platform.system() == "Windows": 
            url = file_url.replace("file:///", "file://")
            
        return unquote(urlparse(url).path)

    @classmethod
    def find_available_name(cls, directory, file_name):
        index = 1
        available_name = file_name

        while path.exists(path.join(directory, available_name)):
            available_name = f"{file_name}_{index}"
            index += 1
            
        return available_name

    @classmethod
    def get_working_directory(self):
        return path.join(str(Path.home()), '.pykubeswitch')

    @classmethod
    def get_kube_directory(self):
        return path.join(str(Path.home()), '.kube')