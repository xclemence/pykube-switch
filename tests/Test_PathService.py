from Services.PathService import PathService


def test_get_windows_url():
    path = PathService.url_to_path('file:///d:/test')

    assert path == "/test"


def test_get_no_windows_url(mocker):
    mocker.patch('platform.system', return_value="Linux")
    path = PathService.url_to_path('file:///test')

    assert path == "/test"


def test_get_working_directory(mocker):
    mocker.patch('pathlib.Path.home', return_value="c:\\")
    path = PathService.get_working_directory()

    assert path == "c:\\.pykubeswitch"


def test_get_kube_directory(mocker):
    mocker.patch('pathlib.Path.home', return_value="c:\\")
    path = PathService.get_kube_directory()

    assert path == "c:\\.kube"


def test_find_available_name(mocker):
    mocker.patch("os.path.exists", return_value=False)
    path = PathService.find_available_name("c:\\test", "file")

    assert path == "file"


def test_find_available_name_2_iterations(mocker):
    mocker.patch("os.path.exists", side_effect=[True, True, False])
    path = PathService.find_available_name("c:\\test", "file")

    assert path == "file_2"
