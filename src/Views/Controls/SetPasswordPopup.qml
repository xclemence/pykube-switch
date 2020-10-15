import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15

Popup {
    id: root

    property var model
    signal passwordChanged


    parent: Overlay.overlay

    x: Math.round((parent.width - width) / 2)
    y: Math.round((parent.height - height) / 2)
    width: 500
    height: 300

    ColumnLayout {
        anchors.fill: parent

        Label {
            text : "Set password:"
        }
        Flickable {
            id: flickable
            Layout.fillWidth: true
            Layout.fillHeight: true

            TextArea.flickable: TextArea {
                wrapMode: TextEdit.WrapAnywhere
                selectByMouse: true
                text: root.model ? model.password : ''
                onEditingFinished: {
                    root.model.password = text
                    root.passwordChanged()
                }
            }

            ScrollBar.vertical: ScrollBar { }
        }

        RowLayout {
            Layout.alignment: Qt.AlignRight

            Layout.fillWidth: true
            Button {
                id: saveButton
                text: "Close"
                font.capitalization: Font.MixedCase
                onClicked: root.close()
            }
        }
    }
}
