import platform

from pathlib import Path
from urllib.parse import unquote, urlparse


def url_to_path(file_uri):
    is_windows = platform.system() == "Windows"

    file_uri_parsed = urlparse(file_uri)
    file_uri_path_unquoted = unquote(file_uri_parsed.path)

    if is_windows and file_uri_path_unquoted.startswith("/"):
        result = Path(file_uri_path_unquoted[1:])
    else:
        result = Path(file_uri_path_unquoted)

    return result


def find_available_name(directory, file_name):
    index = 1
    available_name = file_name

    while directory.joinpath(available_name).is_file():
        available_name = f"{file_name}_{index}"
        index += 1

    return available_name


def get_working_directory():
    return Path.home() / '.pykubeswitch'


def get_kube_directory():
    return Path.home() / '.kube'
