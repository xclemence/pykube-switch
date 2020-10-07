import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1

import "./controls"

Item {
    id: root
    property var model
    signal deleted(var cluster)

    visible: model

    ColumnLayout{

        anchors.fill: parent

        ClusterItemActions {
            id: clusterActions
            Layout.fillWidth: true
            Layout.preferredHeight: 50

            canApply: !root.model.is_current && root.model.has_file

            onApplyClicked: root.model.apply()
            onDeleteClicked: root.deleted(root.model)
            onCopyPasswordClicked: root.model.copy_password_to_clipbord()
        }

        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true

            GridLayout {
                anchors.fill: parent

                id: grid
                columns: 2

           
                Label { 
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    text: "Display name:" 
                }

                TextField {
                    id: displayNameInput
                    selectByMouse: true
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    text: root.model.display_name
                    onTextChanged : root.model.display_name = text
                }

                Label { 
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    id: nameLabel 
                    text: "Name:" 
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    text: root.model ? root.model.name : ''
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true

                    id: serverLabel
                    text: "Server:"
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true

                    id: serverText
                    text: root.model ? root.model.server : ''
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    text: "File:"
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    text: root.model ? root.model.file_name : ''
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    id: hasPasswordLabel
                    text: "has password:"
                }

                CheckBox {
                    id: hasPasswordCheckBox
                    anchors.leftMargin: 0
                }
            }
        }
    }
}