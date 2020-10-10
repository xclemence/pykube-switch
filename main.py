import sys
import os

from os.path import abspath, dirname, join
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle


from contexts.MainContext import MainContext
from services.ErrorService import ErrorService

def shutdown():
    del globals()["engine"]

if __name__ == '__main__':

    main_context = MainContext()
    error_service = ErrorService()
    
    app = QGuiApplication(sys.argv)
    app.aboutToQuit.connect(shutdown)
    
    app.setOrganizationName("xavier CLEMENCE")
    app.setOrganizationDomain("xavier CLEMENCE")
    
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()

    context = engine.rootContext()

    context.setContextProperty("context", main_context)
    context.setContextProperty("error", error_service)

    qmlFile = join(dirname(__file__), 'views/MainView.qml')
    engine.load(abspath(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
