from PySide2.QtCore import QObject, Slot, Property, Signal
from PySide2.QtWidgets import QFileDialog
from pathlib import Path
from os.path import join

from services.ClusterMetaDataService import ClusterMetaDataService

from .ClusterItemContext import ClusterItemContext
from .ListModelContext import ListModelContext
from models.Cluster import Cluster

class ClustersContext(QObject):

    _clusters = ListModelContext([], Cluster) 
    service: ClusterMetaDataService

    def __init__(self):
        QObject.__init__(self)
        self.service = ClusterMetaDataService(self.get_working_directory())
        self.load_clusters()

    def get_clusters(self):
        return self._clusters

    def set_clusters(self, value):
        self._clusters = value
        self.clusters_changed.emit()

    @Signal
    def clusters_changed(self):
        pass

    clusters = Property(QObject, get_clusters, set_clusters, notify=clusters_changed)
    
    def get_working_directory(self):
        return join(str(Path.home()), '.pykubeswitch')

    def load_clusters(self):
        test = self.service.load()
        self.clusters = ListModelContext(test, Cluster)
   
    @Slot()
    def refresh(self):
        self.load_clusters()
    

    @Slot(str)
    def add_file(self, file_path):
        item = self.service.read_from_file(file_path)
        self.clusters.append(item)
        self.service.save(self.clusters.items)
