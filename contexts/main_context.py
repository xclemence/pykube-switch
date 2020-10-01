from PySide2.QtCore import QObject, Slot, Property, Signal

class MainContext(QObject):

    _title = "Pykube Switch"

    def __init__(self):
        QObject.__init__(self)

    def get_title(self):
        return self._title

    @Signal
    def title_changed(self):
        pass

    title = Property(str, get_title, notify=title_changed)
    