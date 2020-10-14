from Services.PathService import *

from pathlib import Path, PosixPath, WindowsPath

def test_get_windows_url(mocker):
    mocker.patch('platform.system', return_value="Windows")
    path = url_to_path('file:///d:/test')

    assert path == Path("d:/test")


def test_get_no_windows_url(mocker):
    mocker.patch('platform.system', return_value="Linux")
    path = url_to_path('file:///test')

    assert path == Path("/test")


def test_get_working_directory(mocker):
    mocker.patch.object(Path, 'home', return_value=Path("./test"))
    path = get_working_directory()

    assert path == Path("./test/.pykubeswitch")


def test_get_kube_directory(mocker):
    mocker.patch.object(Path, 'home', return_value=Path("./test"))
    path = get_kube_directory()

    assert path == Path("./test/.kube")


def test_find_available_name(mocker):
    mocker.patch.object(Path, 'is_file', return_value=False)
    path = find_available_name(Path("./test"), "file")

    assert path == "file"


def test_find_available_name_2_iterations(mocker):
    mocker.patch.object(Path, 'is_file', side_effect=[True, True, False])
    path = find_available_name(Path("./test"), "file")

    assert path == "file_2"
