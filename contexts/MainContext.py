from PySide2.QtCore import QObject, Slot, Property, Signal

from .ClustersContext import ClustersContext

class MainContext(QObject):

    _title = "Pykube Switch"
    _clusters_context = ClustersContext()

    def __init__(self):
        QObject.__init__(self)

    def get_title(self):
        return self._title

    @Signal
    def title_changed(self):
        pass

    title = Property(str, get_title, notify=title_changed)

    ########################

    def get_cluster_context(self):
        return self._clusters_context

    @Signal
    def cluster_context_changed(self):
        pass

    clusters_context = Property(ClustersContext, get_cluster_context, notify=cluster_context_changed)
    


    