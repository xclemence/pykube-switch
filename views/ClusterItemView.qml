import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

Rectangle {
    // anchors.fill: parent
    id: root
    property var model

    color: "transparent"
    GridLayout {
        anchors.fill: parent
        id: grid
        columns: 2
        rows: 4
        Rectangle {
            Layout.column: 0
            Layout.row: 0
            
            Layout.fillWidth: true
            color: "blue"

            Label {
                id: nameLabel
                text: "Name:"
            }
        }

        TextField {
            Layout.column: 1
            Layout.row: 0
            Layout.alignment: Qt.AlignVCenter
            Layout.fillWidth: true

            id: nameText
            text: root.model.name
        }

        Label {
            Layout.column: 0
            Layout.row: 1
            Layout.alignment: Qt.AlignVCenter
            Layout.fillWidth: true

            id: serverLabel
            text: "Server:"
        }

        TextField {
            Layout.column: 1
            Layout.row: 1
            Layout.alignment: Qt.AlignVCenter
            Layout.fillWidth: true

            id: serverText
            text: root.model.server
        }

        Label {
            Layout.column: 0
            Layout.row: 2
            Layout.alignment: Qt.AlignVCenter
            Layout.fillWidth: true

            id: hasPasswordLabel
            text: "has password:"
        }

        CheckBox {
            Layout.column: 1
            Layout.row: 2
            id: hasPasswordCheckBox
            anchors.leftMargin: 0
        }

        RowLayout {
            Layout.row: 3
            Layout.columnSpan: 2
            Layout.alignment: Qt.AlignRight

            Layout.fillHeight: true
            Button {
                text: "Set password"
                font.capitalization: Font.MixedCase 
            }

            Button {
                text: "Copy password to clipboard"
                font.capitalization: Font.MixedCase 
                onClicked: root.model.copy_password_to_clipbord()
            }
        }
    }
}