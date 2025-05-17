import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from MainShell import Ui_MainShell
from InputWindow import Ui_InputWindow


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up MainShell UI
        self.ui = Ui_MainShell()
        self.ui.setupUi(self)

        # Create an instance of InputWindow UI
        self.input_window = QWidget()
        self.input_ui = Ui_InputWindow()
        self.input_ui.setupUi(self.input_window)

        # Add InputWindow to the stacked widget in MainShell
        self.ui.stackedWidget.addWidget(self.input_window)

        # Set InputWindow as the default view (index 0)
        self.ui.stackedWidget.setCurrentWidget(self.input_window)

        # Show the main window
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())
