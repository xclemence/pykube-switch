from PySide2.QtCore import QObject, Slot, Property, Signal

from .ClustersContext import ClustersContext

class MainContext(QObject):

    _title = "Pykube Switch"
    _clusters_context = ClustersContext()
    
    cluster_context_changed = Signal()
    title_changed = Signal()

    def __init__(self):
        QObject.__init__(self)

    @Property(str, notify=title_changed)
    def title(self):
        return self._title

    @Property(ClustersContext, notify=cluster_context_changed)
    def clusters_context(self):
        return self._clusters_context
