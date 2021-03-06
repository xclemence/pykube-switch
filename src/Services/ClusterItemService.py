from .ClusterConfigService import ClusterConfigService
from .ClusterMetaDataService import ClusterMetaDataService

from Contexts.ClusterItemContext import ClusterItemContext

from Services.PathService import url_to_path


class ClusterItemService:
    def __init__(self, config_service: ClusterConfigService, metadata_service: ClusterMetaDataService):
        self.config_service = config_service
        self.metadata_service = metadata_service

    def refresh_is_current(self, clusters):
        for cluster in clusters:
            cluster.set_is_current(self.config_service.is_current(cluster.file_name))

    def refresh_has_file(self, clusters):
        for cluster in clusters:
            cluster.set_has_file(self.config_service.exists(cluster.file_name))

    def refresh(self, clusters):
        self.refresh_is_current(clusters)
        self.refresh_has_file(clusters)

    def save(self, clusters):
        items = [item_context.cluster for item_context in self.clusters.items]
        self.metadata_service.save(items)

    def create(self, file_url):
        file_path = url_to_path(file_url)

        item = self.metadata_service.read_from_file(file_path)

        config_file = self.config_service.add_file(file_path)
        item.file_name = config_file.name

        return ClusterItemContext(item)
