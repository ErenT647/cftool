import QtQuick
import QtQuick.Controls

Window{
    id: root
    width: 640
    height: 480
    visible: true
    title: "Test"

    property bool isRed: true
    property int currWidget: 0

    Image {
        id: background
        source: "C:\Users\K1518375\Downloads\Project\logo.png"
        anchors.fill: parent
        fillMode: Image.PreserveAspectCrop
    }

    

}
