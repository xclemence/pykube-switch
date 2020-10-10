from PySide2.QtCore import QObject, Signal

from .Singleton import QObjectSingleton

class ErrorService(QObject, metaclass=QObjectSingleton):
    
    error = Signal(str, arguments=['error'])

    def __init__(self):
        QObject.__init__(self)

    def send_error(self, message):
        self.error.emit(message)
