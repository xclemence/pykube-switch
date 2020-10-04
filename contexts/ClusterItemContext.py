from PySide2.QtCore import QObject, Slot, Property, Signal

from models.Cluster import Cluster

class ClusterItemContext(QObject):

    def __init__(self, cluster):
        QObject.__init__(self)
        self.cluster = cluster

    def get_display_name(self):
        return self.cluster.display_name

    def set_display_name(self, value):
        self.cluster.display_name = value
        self.display_name_changed.emit()

    @Signal
    def display_name_changed(self):
        pass

    name = Property(str, get_display_name, set_display_name, notify=display_name_changed)
