import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

import Qt.labs.platform 1.1 as LabsPlatform

Item {
    id: root
    property var model
    property ApplicationWindow window
    
    LabsPlatform.SystemTrayIcon {
        visible: true
        icon.source: "Images/Kube.png"

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
                text: "Restore"
                onTriggered: {
                    window.visibility = Window.AutomaticVisibility
                    window.visible = true
                }
            }
            
            LabsPlatform.MenuItem { separator : true }
            LabsPlatform.MenuItem {
                text: "Quit"
                onTriggered: Qt.quit()
            }
        }
    }
}