import sys

from os.path import abspath, dirname, join
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle
from PySide2.QtCore import QUrl

from Contexts.MainContext import MainContext
from Services.ErrorService import ErrorService

application_path = (
    sys._MEIPASS
    if getattr(sys, "frozen", False)
    else dirname(abspath(__file__))
)

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

    qmlFile = join(application_path, "views/MainView.qml")
    engine.load(QUrl.fromLocalFile(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
