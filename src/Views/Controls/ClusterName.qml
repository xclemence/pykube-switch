import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item {
    id: root
    property var item

    RowLayout {
        anchors.fill: parent;

        Label {
            text: root.item.display_name
        }

        Circle {
            visible: root.item.is_current
            Layout.alignment: Qt.AlignRight
            color: "green"
            size: 15
        }
    }
}