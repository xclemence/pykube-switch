import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import QtQuick.Dialogs 1.3

import "./Controls"

Item {
    id: root
    property var model

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
            SplitView.fillHeight: true
            SplitView.minimumWidth: 220
            title: "Cluster contexts"

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
            SplitView.fillWidth: true
            SplitView.fillHeight: true
            SplitView.minimumWidth: 450

            title: "Cluster details"
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
}