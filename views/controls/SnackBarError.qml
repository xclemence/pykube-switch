import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    id: root

    signal reemitted(var error)

    Component.onCompleted: {
        error.onError.connect(reemitted)
    }

    onReemitted: {
        snackBar.open(error)
    }

    SnackBar {
        id: snackBar
    }
}
