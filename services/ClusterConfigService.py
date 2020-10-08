from os import path, makedirs, remove
import json
import yaml
import urllib
import urllib.request
import filecmp 

from models.Cluster import Cluster

from shutil import copyfile

from .PathService import PathService

class ClusterConfigService:
    _config_directory = "configs"
    _target_file_name = "config"

    def __init__(self, base_directory, target_directory):
        self.base_directory = path.join(base_directory, self._config_directory)
        self.target_directory = target_directory

    def get_base_file(self, file_name):
        return path.join(self.base_directory, file_name)
    
    def get_target_file(self):
        return path.join(self.target_directory, self._target_file_name)

    def add_file(self, file_path):
        if not path.exists(self.base_directory):
            makedirs(self.base_directory)
        
        file_name = path.basename(file_path)
        available_name = PathService.find_available_name(self.base_directory, file_name)
        target_path = self.get_base_file(available_name)

        copyfile(file_path, target_path)

        return target_path

    def apply(self, file_name):

        source_file_path = self.get_base_file(file_name)
        target_file_path = self.get_target_file()

        if(not path.exists(source_file_path)):
           return 

        copyfile(source_file_path, target_file_path)

    def is_current(self, file_name):
        source_file_path = self.get_base_file(file_name)
        target_file_path = self.get_target_file()

        if(not path.exists(source_file_path) or not path.exists(target_file_path)):
           return False

        return filecmp.cmp(source_file_path, target_file_path, False) 

    def exists(self, file_name):
        source_file_path = self.get_base_file(file_name)

        return path.exists(source_file_path)

    def delete(self, file_name):
        source_file_path = self.get_base_file(file_name)
        
        if(not path.exists(source_file_path)):
            return

        remove(source_file_path)

