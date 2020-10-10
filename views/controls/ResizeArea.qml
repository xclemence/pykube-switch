import QtQuick 2.0
import QtQuick.Controls 2.1

Item {
    id: root
    property var mainWindow

    property int previousX
    property int previousY

    property int borderSize: 5
    property int cornerSize: 10

    function bottomResize(mouseY,previousY ){
        var dy = mouseY - previousY
        mainWindow.setHeight(mainWindow.height + dy)
    }

    function leftResize(mouseX, previousX){
        var dx = mouseX - previousX
        mainWindow.setX(mainWindow.x + dx)
        mainWindow.setWidth(mainWindow.width - dx)
    }

    function rightResize(mouseX, previousX){
        var dx = mouseX - previousX
        mainWindow.setWidth(mainWindow.width + dx)
    }

    MouseArea {
        id: bottomArea
        height: borderSize
        anchors {
            bottom: parent.bottom
            left: parent.left
            right: parent.right
            leftMargin: cornerSize
            rightMargin: cornerSize
        }

        cursorShape: Qt.SizeVerCursor
        
        onPressed: { previousY = mouseY }
 
        onMouseYChanged: bottomResize(mouseY, root.previousY)
    }
 
    MouseArea {
        id: leftArea
        width: borderSize
        anchors {
            top: parent.top
            bottom: bottomArea.top
            left: parent.left
            topMargin: cornerSize
            bottomMargin: cornerSize
        }
        cursorShape: Qt.SizeHorCursor
 
        onPressed: { previousX = mouseX }
 
        onMouseXChanged: leftResize(mouseX, root.previousX)
    }
 
    MouseArea {
        id: rightArea
        width: borderSize
        anchors {
            top: parent.top
            bottom: parent.bottom
            right: parent.right
            topMargin: cornerSize
            bottomMargin: cornerSize
        }
        cursorShape:  Qt.SizeHorCursor
 
        onPressed: { previousX = mouseX }
 
        onMouseXChanged: rightResize(mouseX, root.previousX)
    }

    MouseArea {
        id: rightBottomArea
        anchors {
            top: rightArea.bottom
            bottom: parent.bottom
            right: parent.right
            left: bottomArea.right
        }
        cursorShape:  Qt.SizeFDiagCursor
 
        onPressed: {
            previousX = mouseX
            previousY = mouseY
        }
 
        onMouseXChanged: rightResize(mouseX, root.previousX)
        onMouseYChanged: bottomResize(mouseY, root.previousY)
    }

     MouseArea {
        id: leftBottomArea
        anchors {
            top: leftArea.bottom
            bottom: parent.bottom
            right: bottomArea.left
            left: parent.left
        }
        cursorShape:  Qt.SizeBDiagCursor
 
        onPressed: {
            previousX = mouseX
            previousY = mouseY
        }
 
        onMouseXChanged: leftResize(mouseX, root.previousX)
        onMouseYChanged: bottomResize(mouseY, root.previousY)
    }
}
