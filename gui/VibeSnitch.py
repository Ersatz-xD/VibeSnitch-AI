import sys
from PyQt5 import QtWidgets
from LoginWindow import Ui_LoginWindow
from ai.text_cleaner import TextCleaner

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(login_window)
    login_window.show()

    sys.exit(app.exec_())