import filecmp

from shutil import copyfile

from .PathService import find_available_name


class ClusterConfigService:
    _config_directory = "configs"
    _target_file_name = "config"

    def __init__(self, base_directory, target_directory):
        self.base_directory = base_directory / self._config_directory
        self.target_directory = target_directory

    def get_base_file(self, file_name):
        return self.base_directory / file_name

    def get_target_file(self):
        return self.target_directory / self._target_file_name

    def add_file(self, file_path):
        if not self.base_directory.is_dir():
            self.base_directory.mkdir(parents=True)

        file_name = file_path.name
        available_name = find_available_name(self.base_directory, file_name)
        target_path = self.get_base_file(available_name)

        copyfile(file_path, target_path)

        return target_path

    def apply(self, file_name):

        source_file_path = self.get_base_file(file_name)
        target_file_path = self.get_target_file()

        if(not source_file_path.is_file()):
            return

        copyfile(source_file_path, target_file_path)

    def is_current(self, file_name):
        source_file_path = self.get_base_file(file_name)
        target_file_path = self.get_target_file()

        if(not source_file_path.is_file() or not target_file_path.is_file()):
            return False

        return filecmp.cmp(source_file_path, target_file_path, False)

    def exists(self, file_name):
        source_file_path = self.get_base_file(file_name)

        return source_file_path.is_file()

    def delete(self, file_name):
        source_file_path = self.get_base_file(file_name)

        source_file_path.unlink(True)
