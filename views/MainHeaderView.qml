import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1

import "./controls"

Item {
    id: root
    signal minimized

    MouseArea {
        property variant clickPos: "1,1"
        anchors.fill: parent

        onPressed: {
            clickPos = Qt.point(mouse.x,mouse.y)
        }

        onPositionChanged: {
           var delta = Qt.point(mouse.x-clickPos.x, mouse.y-clickPos.y)
            mainWindow.x += delta.x;
            mainWindow.y += delta.y;
        }

        RowLayout {
            width: parent.width;
            Image {
                source: "images/Kube.png"
                Layout.leftMargin: 10;
                Layout.preferredWidth: 20;
                Layout.preferredHeight: 20;
            }

            Label {
                text: context.title
                horizontalAlignment: Text.AlignHCenter;
                font.bold: true;
                Layout.alignment: Qt.AlignRight;
                Layout.fillWidth: true;
            }

            HeaderButton {
                Layout.preferredHeight: 30;
                Layout.preferredWidth: 40;
                path: "M3 8 13 8 13 7 3 7z"
                onClicked: root.minimized()
            }

            HeaderButton {
                Layout.preferredHeight: 30;
                Layout.preferredWidth: 40;
                path: "M8.583 8 13 12.424 12.424 13 8 8.583 3.576 13 3 12.424 7.417 8 3 3.576 3.576 3 8 7.417 12.424 3 13 3.576z"
                onClicked: Qt.quit()
            }
        }
    }
}