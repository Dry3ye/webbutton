from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def open_url():
    import webbrowser
    webbrowser.open("https://lunatech.co.za/")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Lets go")
    win.setGeometry(100, 100, 600, 400)
    
    label = QtWidgets.QLabel(win)
    label.setText("Lets go")
    label.setGeometry(250, 180, 100, 30)    
    label.move(250, 180)

    b1= QtWidgets.QPushButton(win)
    b1.setText("Enter")
    b1.move(250, 220)
    b1.setGeometry(250, 220, 100, 30)
    b1.clicked.connect(open_url)

    
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()






