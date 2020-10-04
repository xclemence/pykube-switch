import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1



Item {
    id: root
    property var model

    Component {
        id: clusterItemTemplate
        Label {
            text: index
        }
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

                    model: root.model.clusters
                    
                    delegate: ItemDelegate {
                        width: parent.width
                        text: model.display_name 
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
            // ClusterItemView {
            //     anchors.fill: parent;
            // }
        }
    }
}