import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1

Item {
    id: root
    property var model

    signal applyClicked 
    signal deleteClicked
    signal setPasswordClicked
    signal copyPasswordClicked

    property alias canApply : applyButton.enabled

    RowLayout {

        anchors.fill: parent

        RowLayout {
            Layout.alignment: Qt.AlignLeft
            Layout.fillWidth: true

            Button {
                id: applyButton
                text: "Apply"
                font.capitalization: Font.MixedCase 
                onClicked: root.applyClicked()
            }

            Button {
                id: deleteButton
                text: "Delete"
                font.capitalization: Font.MixedCase 
                onClicked: root.deleteClicked()
            }
        }
            
        RowLayout {
            Layout.alignment: Qt.AlignRight

            Layout.fillWidth: true
            Button {
                id: setPasswordButton
                text: "Set password"
                font.capitalization: Font.MixedCase 
            }
            
            Button {
                id: copyPasswordButton
                text: "Copy password to clipboard"
                font.capitalization: Font.MixedCase 
                onClicked: root.copyPasswordClicked()
            }
        }
    }
}