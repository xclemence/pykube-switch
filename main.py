import sys
import os

from os.path import abspath, dirname, join
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle

from contexts.main_context import MainContext

def shutdown():
    del globals()["engine"]

if __name__ == '__main__':
    main_context = MainContext()
    app = QGuiApplication(sys.argv)
    app.aboutToQuit.connect(shutdown)
    
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()

    context = engine.rootContext()

    context.setContextProperty("context", main_context)

    qmlFile = join(dirname(__file__), 'views/MainView.qml')
    engine.load(abspath(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
