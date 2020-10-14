from pathlib import Path
from unittest import mock

from Services.ClusterItemService import ClusterItemService

from DataModels.Cluster import Cluster


def test_create_cluster(mocker):

    class ConfigurationServiceMock(mock.Mock):
        def add_file(self, file_path):
            return Path('c://test_path123.txt')
    

    class MetadataServiceMock(mock.Mock):
        def read_from_file(self, file_path):
            return Cluster("cluster", "C1", "c:\\test", "127.0.0.1")

    service = ClusterItemService(ConfigurationServiceMock(), MetadataServiceMock())
    cluster_context = service.create('file:///d:/test.txt')

    assert cluster_context.file_name == "test_path123.txt"
