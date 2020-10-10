import QtQuick 2.14
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.14
import QtQuick.Window 2.15

import Qt.labs.platform 1.1 as LabsPlatform
import QtQuick.Dialogs 1.3

import "./controls"

Item {
    id: root
    property var model
    property ApplicationWindow window

    FileDialog {
        id: fileDialog
        title: "Please choose a file"
        nameFilters: [ "All files (*)" ]
        folder: shortcuts.home
        visible: false
        onAccepted: model.add_file(fileDialog.fileUrl)
    }

    SplitView {
        anchors.fill: parent;
        orientation: Qt.Horizontal

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
                        id: item
                        width: parent.width
                        highlighted: ListView.isCurrentItem
                        contentItem: ClusterName {
                            item: model
                        }
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
                anchors.leftMargin: 10
                anchors.rightMargin: 10
                anchors.bottomMargin: 10

                model: root.model.selected_cluster
                onDeleted: root.model.delete(cluster)
                onApplied: root.model.apply(cluster.file_name)
                onDataChanged: root.model.update(cluster)
            }
        }
    }

    LabsPlatform.SystemTrayIcon {
        visible: true
        icon.source: "images/Kube.png"

        menu: LabsPlatform.Menu {
            LabsPlatform.Menu {
                title: "Contexts"
                id: contextMenu

                Instantiator {
                    model: root.model.clusters
                    LabsPlatform.MenuItem {
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
 
            LabsPlatform.MenuItem { separator : true }
            LabsPlatform.MenuItem {
                text: qsTr("Restore")
                onTriggered: {
                    window.visibility = Window.AutomaticVisibility
                    window.visible = true
                }
            }
            
            LabsPlatform.MenuItem { separator : true }
            LabsPlatform.MenuItem {
                icon.source: "images/Kube.png"

                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
    }
}