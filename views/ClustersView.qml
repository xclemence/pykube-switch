import QtQuick 2.14
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.14
import QtQuick.Dialogs 1.0
import Qt.labs.platform 1.1
import QtQuick.Window 2.1

import "./controls"

Item {
    id: root
    property var model
    property ApplicationWindow window

    Component {
        id: clusterItemTemplate
        Label {
            text: index
        }
    }

    FileDialog {
        id: fileDialog
        title: "Please choose a file"
        folder: shortcuts.home
        nameFilters: [ "All files (*)" ]
        onAccepted: model.add_file(fileDialog.fileUrl)
    }

    RowLayout {
        anchors.fill: parent;

        GroupBox {
            Layout.fillHeight: true
            Layout.preferredWidth: 250
            title: qsTr("Cluster contexts")

            ColumnLayout {
                anchors.fill: parent;
                ListView {
                    id: listView
                    currentIndex: -1
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    clip: true
                    ScrollBar.vertical: ScrollBar {
                        policy: ScrollBar.AsNeeded
                    }

                    model: root.model.clusters

                    onCurrentItemChanged: root.model.selected_index(listView.currentIndex)
                    
                    delegate: ItemDelegate {
                        width: parent.width
                        text: model.display_name + (model.is_current ? " (current)" : "")
                        highlighted: ListView.isCurrentItem
                        onClicked: {
                            if (listView.currentIndex != index) {
                                listView.currentIndex = index
                            }
                        }
                    }
                }

                RowLayout {
                    Button {
                        Layout.fillWidth: true
                        text: "Import"
                        font.capitalization: Font.MixedCase 
                        onClicked: fileDialog.open()
                    }
                    Button {
                        Layout.fillWidth: true
                        text: "Refresh"
                        font.capitalization: Font.MixedCase 
                        onClicked: root.model.refresh()
                    }
                }
            }
        }

        GroupBox {
            Layout.fillWidth: true
            Layout.fillHeight: true

            title: qsTr("Cluster details")
            ClusterItemView {
                anchors.fill: parent;
                model: root.model.selected_cluster
                onDeleted: root.model.delete(cluster)
                onApplied: root.model.apply(cluster.file_name)
                onDataChanged: root.model.update(cluster)
            }
        }
    }

    SystemTrayIcon {
        visible: true
        icon.source: "images/Kube.png"

        menu: Menu {
            Menu {
                title: "Contexts"
                id: contextMenu

                Instantiator {
                    model: root.model.clusters
                    MenuItem {
                        text: model.display_name
                        checked : model.is_current
                        enabled: model.has_file
                        onTriggered: root.model.apply(model.file_name)
                    }

                    // The trick is on those two lines
                    onObjectAdded: contextMenu.insertItem(index, object)
                    onObjectRemoved: contextMenu.removeItem(object)
                }

            }
 
            MenuItem { separator : true }
            MenuItem {
                text: qsTr("Restore")
                onTriggered: {
                    window.visibility = Window.AutomaticVisibility
                    window.visible = true
                }
            }
            
            MenuItem { separator : true }
            MenuItem {
                icon.source: "images/Kube.png"

                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
    }
}