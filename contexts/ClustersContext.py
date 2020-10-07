from PySide2.QtCore import QObject, Slot, Property, Signal
from PySide2.QtWidgets import QFileDialog
from pathlib import Path
from os.path import join

from services.ClusterMetaDataService import ClusterMetaDataService
from services.ClusterConfigService import ClusterConfigService
from services.ClusterItemService import ClusterItemService
from services.PathService import PathService

from .ClusterItemContext import ClusterItemContext
from .ListModelContext import ListModelContext
from models.Cluster import Cluster

class ClustersContext(QObject):

    _clusters = ListModelContext([], ClusterItemContext) 
    service: ClusterMetaDataService
    _selected_cluster = None

    def __init__(self):
        QObject.__init__(self)
        self.service = ClusterMetaDataService(self.get_working_directory())
        self.config_service = ClusterConfigService(self.get_working_directory(), self.get_kube_directory())
        self.item_service = ClusterItemService(self.config_service)
        self.load_clusters()

    ##################################

    def get_clusters(self):
        return self._clusters

    def set_clusters(self, value):
        self._clusters = value
        self.clusters_changed.emit()

    @Signal
    def clusters_changed(self):
        pass

    clusters = Property(QObject, get_clusters, set_clusters, notify=clusters_changed)

    ##############################

    _selected_cluster: ClusterItemContext

    def get_selected_cluster(self):
        return self._selected_cluster

    def set_selected_cluster(self, value):
        self._selected_cluster = value
        self.selected_cluster_changed.emit()

    @Signal
    def selected_cluster_changed(self):
        pass

    selected_cluster = Property(ClusterItemContext, get_selected_cluster, set_selected_cluster, notify=selected_cluster_changed)

    ####################

    
    def get_working_directory(self):
        return join(str(Path.home()), '.pykubeswitch')

    def get_kube_directory(self):
        return join(str(Path.home()), '.kube')

    def load_clusters(self):
        test = self.service.load()

        items = [ClusterItemContext(item, self.config_service) for item in test]
        
        self.item_service.refresh(items)
        self.clusters = ListModelContext(items, ClusterItemContext)
   
    @Slot()
    def refresh(self):
        self.load_clusters()
    

    @Slot(str)
    def add_file(self, file_url):
        file_path = PathService.url_to_path(file_url)

        self.config_service.add_file(file_path)
        
        item = self.service.read_from_file(file_path)

        new_cluster = ClusterItemContext(item, self.config_service)
        self.clusters.append(new_cluster)

        items = [item_context.cluster for item_context in self.clusters.items]

        self.service.save(items)

    @Slot(int)
    def selected_index(self, index):
        cluster = self.clusters.items[index]
        self.selected_cluster = cluster

    @Slot(ClusterItemContext)
    def delete(self, cluster):
        print(f"delete cluster: {cluster.name}")        
