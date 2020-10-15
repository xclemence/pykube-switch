import json
import yaml

from pathlib import Path

from DataModels.Cluster import Cluster


class ClusterMetaDataService:
    _meta_data_file_name = Path("clusters.json")

    def __init__(self, base_directory):
        self.base_directory = base_directory

    def get_file_path(self):
        return self.base_directory / self._meta_data_file_name

    def save(self, clusters):
        if not self.base_directory.is_dir():
            self.base_directory.makedir()

        file_full_path = self.get_file_path()

        with file_full_path.open('w+') as outfile:
            json.dump(clusters, outfile, default=lambda o: o.__dict__, indent=2)

    def load(self):
        file_full_path = self.get_file_path()

        if not file_full_path.is_file():
            return []

        with file_full_path.open('r') as file:
            restults = json.load(file)

        return list(map(lambda x: Cluster(**x), restults))

    def read_from_file(self, file_path):
        with file_path.open('r') as file:
            yaml_content = yaml.safe_load(file)

        name = yaml_content.get('current-context')

        cluster = next(c for c in yaml_content.get('clusters') if c.get('name') == name)

        server = cluster.get('cluster').get('server')

        return Cluster(name, name, file_path.name, server)
