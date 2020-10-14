from pathlib import Path
from Services.ClusterConfigService import ClusterConfigService


def test_add_file(mocker):

    mocker.patch("Services.ClusterConfigService.find_available_name", return_value="test_file.txt")
    copy_mock = mocker.patch("Services.ClusterConfigService.copyfile")
    service = ClusterConfigService(Path("c:/hello"), Path("c:/test"))

    mocker.patch.object(Path, "is_dir", return_value=True)

    file = service.add_file(Path("c:/input/file.txt"))

    assert file == Path("c:/hello/configs/test_file.txt")
    copy_mock.assert_called_with(Path('c:/input/file.txt'), Path('c:/hello/configs/test_file.txt'))


def test_is_current(mocker):
    mocker.patch.object(Path, "is_file", return_value=True)
    mocker.patch("filecmp.cmp", return_value=True)

    service = ClusterConfigService(Path("c:/hello"), Path("c:/test"))

    result = service.is_current("file.txt")

    assert result

def test_is_current_no_source(mocker):
    mocker.patch.object(Path, "is_file", return_value=False)
    mocker.patch("filecmp.cmp", return_value=True)

    service = ClusterConfigService(Path("c:/hello"), Path("c:/test"))

    result = service.is_current("file.txt")

    assert not result

def test_is_current_no_target(mocker):
    mocker.patch.object(Path, "is_file", side_effect=[True, False])
    mocker.patch("filecmp.cmp", return_value=True)

    service = ClusterConfigService(Path("c:/hello"), Path("c:/test"))

    result = service.is_current("file.txt")

    assert not result


