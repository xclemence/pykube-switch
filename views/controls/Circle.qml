import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle {
    property int size

    id: rectangle
    width: size
    height: size
    radius: width * 0.5
}