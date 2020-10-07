from .ClusterConfigService import ClusterConfigService
from os import path

class ClusterItemService:
    def __init__(self, configService: ClusterConfigService):
        self.configService = configService

    def refresh_is_current(self, clusters):
        for cluster in clusters:
            cluster.set_is_current(self.configService.is_current(cluster.file_name))

    def refresh_has_file(self, clusters):
        for cluster in clusters:
            cluster.set_has_file(self.configService.exists(cluster.file_name))

    def refresh(self, clusters):
        self.refresh_is_current(clusters)
        self.refresh_has_file(clusters)
