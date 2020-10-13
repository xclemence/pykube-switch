from Services.ClusterConfigService import ClusterConfigService


def test_add_file(mocker):
    mocker.patch("os.path.exists", return_value=True)
    mocker.patch("Services.ClusterConfigService.find_available_name", return_value="test_file.txt")
    copy_mock = mocker.patch("Services.ClusterConfigService.copyfile")

    service = ClusterConfigService("c:\\hello", "c:\\test")

    file = service.add_file("c:\\input\\file.txt")

    assert file == "c:\\hello\\configs\\test_file.txt"
    copy_mock.assert_called_with('c:\\input\\file.txt', 'c:\\hello\\configs\\test_file.txt')


def test_is_current(mocker):
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("filecmp.cmp", return_value=True)

    service = ClusterConfigService("c:\\hello", "c:\\test")

    result = service.is_current("file.txt")

    assert result

def test_is_current_no_source(mocker):
    mocker.patch("os.path.isfile", return_value=False)
    mocker.patch("filecmp.cmp", return_value=True)

    service = ClusterConfigService("c:\\hello", "c:\\test")

    result = service.is_current("file.txt")

    assert not result

def test_is_current_no_target(mocker):
    mocker.patch("os.path.isfile", side_effect=[True, False])
    mocker.patch("filecmp.cmp", return_value=True)

    service = ClusterConfigService("c:\\hello", "c:\\test")

    result = service.is_current("file.txt")

    assert not result


