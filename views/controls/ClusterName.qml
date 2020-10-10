import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.11

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