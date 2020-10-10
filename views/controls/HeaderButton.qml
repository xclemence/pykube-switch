import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Shapes 1.15

Item {
    id: root
    property var path
    signal clicked

    Button {
        padding : 0;
        topInset: 0;
        bottomInset: 0;
        
        anchors.fill: parent
        onClicked: root.clicked()
        flat: true
        focusPolicy: Qt.NoFocus
        contentItem: Item {
            Shape {
                id: minimizeShape
                anchors.centerIn: parent
                width: 15
                height: 15
                opacity: 0.25
                ShapePath {
                    strokeWidth: 1
                    PathSvg { path: root.path }
                }
            } 
        }
    }
}
