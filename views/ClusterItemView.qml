import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15

import "./controls"
import "../MaterialIcons/MaterialDesign.js" as MD

Item {
    id: root
    property var model
    signal deleted(var cluster)
    signal applied(var cluster)
    signal dataChanged(var cluster)

    visible: model

    ColumnLayout{

        anchors.fill: parent

        ClusterItemActions {
            id: clusterActions
            Layout.fillWidth: true
            Layout.preferredHeight: 50

            model: root.model

            onApplyClicked: root.applied(root.model)
            onDeleteClicked: root.deleted(root.model)
            onCopyPasswordClicked: root.model.copy_password_to_clipbord()
            onPasswordChanged: root.dataChanged(root.model)
        }

        RowLayout {
            Layout.topMargin: 10
            Layout.bottomMargin: 10

            Label {
                text: root.model ? root.model.name : ''
	            font.pixelSize: 25
            }

            Circle {
                Layout.leftMargin: 15
                Layout.alignment: Qt.AlignVCenter
                visible: root.model.is_current
                color: "green"
                size: 20
            }

            Label {
                Layout.leftMargin: 15
                Layout.alignment: Qt.AlignVCenter
                visible: root.model.has_password
                font.family: iconFont.name
	            font.pixelSize: 20
	            text: MD.icons.lock_outline
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.bottomMargin: 50

            GridLayout {
                anchors.fill: parent

                id: grid
                columns: 2

                Label { 
                    Layout.alignment: Qt.AlignVCenter
                    Layout.rightMargin: 30
                    text: "Short name:" 
                }

                TextField {
                    id: displayNameInput
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    selectByMouse: true
                    text: root.model.display_name
                    onEditingFinished: {
                        root.model.display_name = text
                        root.dataChanged(root.model)
                    }
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    id: serverLabel
                    text: "Server:"
                }

                TextField {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    readOnly: true
                    selectByMouse: true
                    text: root.model ? root.model.server : ''
                }

                Label {
                    Layout.alignment: Qt.AlignVCenter
                    text: "File:"
                }

                TextField {
                    Layout.alignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                    readOnly: true
                    selectByMouse: true
                    text: root.model ? root.model.file_name : ''
                }
            }
        }
    }
}