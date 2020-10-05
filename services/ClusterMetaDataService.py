from os import path, makedirs
import json
import yaml
import urllib
import urllib.request

from models.Cluster import Cluster

class ClusterMetaDataService:
    _meta_data_file_name = "clusters.json"

    def __init__(self, base_directory):
        self.base_directory = base_directory

    def get_file_path(self):
        return path.join(self.base_directory, self._meta_data_file_name)

    def save(self, clusters):
        results = [obj.__dict__ for obj in clusters]
        
        if not path.exists(self.base_directory):
            makedirs(self.base_directory)

        file_full_path = self.get_file_path()

        with open(file_full_path, 'w+') as outfile:
            json.dump(clusters, outfile, default = lambda o: o.__dict__, indent=2)

    def load(self):
        file_full_path = self.get_file_path()

        if not path.exists(file_full_path):
            return []

        with open(file_full_path, 'r') as file:
            restults = json.load(file)
        
        return list(map(lambda x: Cluster(**x), restults))
    
    def read_from_file(self, file_url):
        
        with urllib.request.urlopen(file_url) as response:
            yaml_content = yaml.safe_load(response.read().decode('utf-8'))

        name = yaml_content.get('current-context')

        cluster = next(c for c in yaml_content.get('clusters') if c.get('name') == name )

        server = cluster.get('cluster').get('server')

        file_name = path.basename(file_url)
        return Cluster(name, name, file_name, server)
