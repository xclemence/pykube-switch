from PySide2.QtCore import QObject, Slot, Property, Signal
from services.ClusterConfigService import ClusterConfigService

from models.Cluster import Cluster

import pyperclip

class ClusterItemContext(QObject):

    name_changed = Signal()
    display_name_changed = Signal()
    file_name_changed = Signal()
    server_changed = Signal()
    is_current_changed = Signal()
    has_file_changed = Signal()
    has_password_changed = Signal()

    _is_current = False
    _has_file = True

    def __init__(self, cluster, configService):
        QObject.__init__(self)
        self.cluster = cluster
        self.configService = configService

    ##############################
    @Property(str, notify=display_name_changed)
    def display_name(self):
        return self.cluster.display_name

    @display_name.setter
    def set_display_name(self, value):
        if(self.cluster.display_name == value):
            return

        self.cluster.display_name = value
        self.display_name_changed.emit()

    ##############################
    @Property(str, notify=name_changed)
    def name(self):
        return self.cluster.name

    ##############################
    @Property(str, notify=file_name_changed)
    def file_name(self):
        return self.cluster.file_name

    ##############################
    @Property(str, notify=server_changed)
    def server(self):
        return self.cluster.server

    ##############################
    @Property(bool, notify=has_password_changed)
    def has_password(self):
        return self.cluster.password != ''

    ##############################
    @Property(bool, notify=is_current_changed)
    def is_current(self):
        return self._is_current

    @is_current.setter
    def set_is_current(self, value):
        self._is_current = value
        self.is_current_changed.emit()

    ##############################
    @Property(bool, notify=has_file_changed)
    def has_file(self):
        return self._has_file

    @has_file.setter
    def set_has_file(self, value):
        self._has_file = value
        self.has_file_changed.emit()

    ##############################

    @Slot()
    def copy_password_to_clipbord(self):
        pyperclip.copy(self.cluster.password)

    @Slot()
    def apply(self):
        self.configService.apply(self.file_name)
