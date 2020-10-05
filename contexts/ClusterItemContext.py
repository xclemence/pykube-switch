from PySide2.QtCore import QObject, Slot, Property, Signal

from models.Cluster import Cluster

import pyperclip

class ClusterItemContext(QObject):

    def __init__(self, cluster):
        QObject.__init__(self)
        self.cluster = cluster

    def get_name(self):
        return self.cluster.name

    def set_name(self, value):
        self.cluster.display_name = value
        self.name_changed.emit()

    @Signal
    def name_changed(self):
        pass

    name = Property(str, get_name, set_name, notify=name_changed)


    @Slot()
    def copy_password_to_clipbord(self):
        pyperclip.copy(self.cluster.password)
