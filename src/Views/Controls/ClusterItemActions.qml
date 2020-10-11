import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15

Item {
    id: root
    property var model

    signal applyClicked 
    signal deleteClicked
    signal setPasswordClicked
    signal copyPasswordClicked
    signal passwordChanged

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
                enabled: !root.model.is_current && root.model.has_file
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
                onClicked: popup.open()

                SetPasswordPopup {
                    id: popup
                    model: root.model
                    onPasswordChanged: root.passwordChanged()
                }
            }
            
            Button {
                id: copyPasswordButton
                enabled: model.has_password
                text: "Copy password"
                font.capitalization: Font.MixedCase 
                onClicked: root.copyPasswordClicked()
            }
        }
    }
}