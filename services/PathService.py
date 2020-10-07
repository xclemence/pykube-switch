import platform 

from models.Cluster import Cluster
from urllib.parse import unquote, urlparse

class PathService:

    @classmethod
    def url_to_path(cls, file_url):
        url = file_url
        if platform.system() == "Windows": 
            url = file_url.replace("file:///", "file://")
            
        return unquote(urlparse(url).path)

