import sys

import PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

from slicer_devel import convert_img
from pronterface_interface import spawn_and_send_commands

class App():
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle('DK-Plotter')
        self.window.setGeometry(640, 480, 280, 80)

        layout = QVBoxLayout()

        self.img_widget = QLabel()
        self.image_path = "./hello.png"
        self.set_image(self.image_path)

        layout.addWidget(self.img_widget)

        load_image_button = QPushButton('Load image')
        load_image_button.clicked.connect(self.load_image_clicked)
        layout.addWidget(load_image_button)

        convert_button = QPushButton('Convert')
        convert_button.clicked.connect(self.convert_image_clicked)
        layout.addWidget(convert_button)

        print_button = QPushButton('Print')
        print_button.clicked.connect(self.print_image)
        layout.addWidget(print_button)

        self.window.setLayout(layout)

    def load_image_clicked(self):
        fname, extensions = QFileDialog.getOpenFileName(self.window, 'Open file',  'c:\\',"Image files (*.jpg *.jfif *.bnp)") # todo :*.png *.gif
        if fname != "":
            self.image_path = fname
            self.set_image(fname)

    def convert_image_clicked(self):
        fname = convert_img(self.image_path, "tmp.gcode")
        self.set_image(fname)


    def set_image(self, path):
        self.image_path = path
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(640, 480, PyQt5.QtCore.Qt.KeepAspectRatio)
        self.img_widget.setPixmap(pixmap)
    
    def print_image(self):
        spawn_and_send_commands("C:/I/Printrun-Win-Slic3r-03Feb2015/pronsole.exe", "tmp.gcode")

    def run(self):
        self.window.show()
        return self.app.exec_()


if __name__ == '__main__':
    app = App()
    sys.exit(app.run())
