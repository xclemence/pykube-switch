from PySide2.QtCore import QObject, Slot, Property, Signal, QModelIndex

import sys

from PySide2.QtWidgets import QFileDialog
from pathlib import Path
from os.path import join

from services.ClusterMetaDataService import ClusterMetaDataService
from services.ClusterConfigService import ClusterConfigService
from services.ClusterItemService import ClusterItemService
from services.PathService import PathService
from services.ErrorService import ErrorService

from .ClusterItemContext import ClusterItemContext
from .ListModelContext import ListModelContext
from models.Cluster import Cluster

class ClustersContext(QObject):

    _clusters = ListModelContext([], ClusterItemContext) 
    _selected_cluster: ClusterItemContext = None

    clusters_changed = Signal()
    selected_cluster_changed = Signal()

    def __init__(self):
        QObject.__init__(self)
        self.metadata_service = ClusterMetaDataService(self.get_working_directory())
        self.config_service = ClusterConfigService(self.get_working_directory(), self.get_kube_directory())
        self.item_service = ClusterItemService(self.config_service, self.metadata_service)
        self.load_clusters()

    ##################################

    @Property(QObject, notify=clusters_changed)
    def clusters(self):
        return self._clusters

    @clusters.setter
    def set_clusters(self, value):
        if (self._clusters == value):
            return

        self._clusters = value
        self.clusters_changed.emit()

    ##############################

    @Property(ClusterItemContext, notify=selected_cluster_changed)
    def selected_cluster(self):
        return self._selected_cluster

    @selected_cluster.setter
    def set_selected_cluster(self, value):
        if(self._selected_cluster == value):
            return

        self._selected_cluster = value
        self.selected_cluster_changed.emit()

    ####################
    
    def get_working_directory(self):
        return join(str(Path.home()), '.pykubeswitch')


    def get_kube_directory(self):
        return join(str(Path.home()), '.kube')


    def load_clusters(self):
        try:
            cluster_models = self.metadata_service.load()

            items = [ClusterItemContext(item, self.config_service) for item in cluster_models]
            self.item_service.refresh(items)

            self.clusters = ListModelContext(items, ClusterItemContext)
        except: 
            ErrorService().send_error(f'Error during configurations loading')

    @Slot()
    def refresh(self):
        self.load_clusters()

    @Slot(str)
    def add_file(self, file_url):
        try:
            file_path = PathService.url_to_path(file_url)

            config_file = self.config_service.add_file(file_path)
        
            item = self.metadata_service.read_from_file(config_file)

            new_cluster = ClusterItemContext(item, self.config_service)
            self.clusters.append(new_cluster)

            self.item_service.refresh(self.clusters)

            self.save_clusters()
        except:
            ErrorService().send_error(f'Error during file "{file_path}" import')


    def save_clusters(self):
        items = [item_context.cluster for item_context in self.clusters.items]
        self.metadata_service.save(items)


    @Slot(int)
    def selected_index(self, index):
        if (index >= len(self.clusters.items)):
            self.selected_cluster = None
            return

        cluster = self.clusters.items[index]
        self.selected_cluster = cluster


    @Slot(ClusterItemContext)
    def delete(self, cluster):
        try:
            self.config_service.delete(cluster.file_name)
            self.clusters.remove(cluster)
            self.save_clusters()
        except:
            ErrorService().send_error(f'Error during "{cluster}" deletion')

    
    @Slot(ClusterItemContext)
    def update(self, cluster):
        self.clusters.update(cluster)
        self.save_clusters()


    @Slot(str)
    def apply(self, file):
        try:
            self.config_service.apply(file)
            self.item_service.refresh_is_current(self.clusters.items)
            self.clusters.update_all()
        except:
            ErrorService().send_error(f'Error during configuration switch ({file})')
