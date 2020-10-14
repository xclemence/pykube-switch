import pytest
from pathlib import Path

from Services.ClusterMetaDataService import ClusterMetaDataService


def test_read_from_file(mocker):

    mock_open = mocker.mock_open(read_data="""
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tL
    server: https://127.0.0.1:6443
  name: default
contexts:
- context:
    cluster: default
    user: default
  name: default
current-context: default
    """)

    mocker.patch.object(Path,"open", mock_open)
    
    service = ClusterMetaDataService(Path("./test"))

    cluster = service.read_from_file(Path("./test.file"))

    assert cluster.name == "default"
    assert cluster.display_name == "default"
    assert cluster.file_name == "test.file"
    assert cluster.server == "https://127.0.0.1:6443"

def test_read_from_file_error(mocker):

    mock_open = mocker.mock_open(read_data="""
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tL
    server: https://127.0.0.1:6443
  name: default
    """)

    mocker.patch.object(Path,"open", mock_open)
    
    service = ClusterMetaDataService(Path("./test"))
    with pytest.raises(Exception):
        service.read_from_file(Path("./test.file"))
