import QtQuick 2.0
import QtQuick.Layouts 1.11
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1
import QtQuick.Controls 2.15

import "./controls"

ApplicationWindow {
    id: mainWindow
    flags: Qt.Window | Qt.FramelessWindowHint
    width: 800
    height: 600
    visible: true
    Material.theme: Material.Dark
    Material.accent: Material.Green
    title: context.title

    header: Rectangle {
        width: parent.width;
        height: 30;
        color: "#212121"
        MainHeaderView{
            width: parent.width;
            height: 30;
            onMinimized: {
                mainWindow.visibility = Window.Minimized
                mainWindow.visible = false
            }
        } 
    }

    ColumnLayout {
        anchors.fill: parent;
        anchors.leftMargin: 5
        anchors.rightMargin: 5
        anchors.topMargin: 5
        anchors.bottomMargin: 5
       
        ClustersView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: context.clusters_context
            window: mainWindow
        }

    }

    ResizeArea {
        anchors.fill: parent;
        mainWindow: mainWindow
    }
}
