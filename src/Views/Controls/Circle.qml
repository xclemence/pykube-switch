import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    property int size

    id: rectangle
    width: size
    height: size
    radius: width * 0.5
}