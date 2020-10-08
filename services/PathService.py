import platform 

from os import path
from models.Cluster import Cluster
from urllib.parse import unquote, urlparse

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
