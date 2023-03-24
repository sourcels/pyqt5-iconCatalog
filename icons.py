import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QStyle, QWidget

class Window(QWidget):
    def __init__(self, parent: QWidget = None):
        super(Window, self).__init__(parent)
        icons = sorted([attr for attr in dir(QStyle) if attr.startswith("SP_")])
        layout = QGridLayout()
        for n, name in enumerate(icons):
            btn = QPushButton(name)
            btn.setObjectName(name)
            btn.clicked.connect(self.return_icon_name)
            pixmapi = getattr(QStyle, name)
            icon = self.style().standardIcon(pixmapi)
            btn.setIcon(icon)
            layout.addWidget(btn, int(n / 4), int(n % 4))

        self.setLayout(layout)

    def return_icon_name(self):
        sending_button = self.sender()
        name = sending_button.objectName()
        print(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())