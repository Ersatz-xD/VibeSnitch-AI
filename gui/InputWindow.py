
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject  # Add this import

class Ui_InputWindow(QObject):  # Change inheritance to QObject
    predictClicked = QtCore.pyqtSignal(str, list)

    def __init__(self):
        super().__init__()

    def setupUi(self, InputWindow):
        InputWindow.setObjectName("InputWindow")
        InputWindow.resize(960, 540)
        InputWindow.setMinimumSize(QtCore.QSize(960, 540))
        InputWindow.setMaximumSize(QtCore.QSize(960, 540))
        InputWindow.setWindowTitle("Vibe Snitch - AI")
        InputWindow.setStyleSheet("QWidget {\n"
"       border-radius: 20px;\n"
"       background-color: #1a1328;\n"
"}")
        self.mainCard = QtWidgets.QFrame(InputWindow)
        self.mainCard.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.mainCard.setMinimumSize(QtCore.QSize(960, 540))
        self.mainCard.setMaximumSize(QtCore.QSize(960, 540))
        self.mainCard.setStyleSheet("QFrame#mainCard {\n"
"    background-color: #1a1328;\n"
"    border-radius: 20px;\n"
"    border: 2px solid #26183d;\n"
"}\n"
"\n"
"\n"
"")
        self.mainCard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainCard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainCard.setObjectName("mainCard")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainCard)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitle = QtWidgets.QLabel(self.mainCard)
        self.lblTitle.setMinimumSize(QtCore.QSize(100, 70))
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"\n"
"")
        self.lblTitle.setScaledContents(False)
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_2.addWidget(self.lblTitle)
        self.lblSlogan = QtWidgets.QLabel(self.mainCard)
        self.lblSlogan.setMinimumSize(QtCore.QSize(0, 50))
        self.lblSlogan.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.lblSlogan.setFont(font)
        self.lblSlogan.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"\n"
"")
        self.lblSlogan.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSlogan.setWordWrap(True)
        self.lblSlogan.setObjectName("lblSlogan")
        self.verticalLayout_2.addWidget(self.lblSlogan)
        self.widget = QtWidgets.QWidget(self.mainCard)
        self.widget.setStyleSheet("background: transparent;")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtName = QtWidgets.QLineEdit(self.widget)
        self.txtName.setEnabled(True)
        self.txtName.setMinimumSize(QtCore.QSize(200, 50))
        self.txtName.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.txtName.setFont(font)
        self.txtName.setMouseTracking(True)
        self.txtName.setTabletTracking(False)
        self.txtName.setStyleSheet("background-color: #120c20;\n"
"color:#C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 3px 15px;\n"
"")
        self.txtName.setAlignment(QtCore.Qt.AlignCenter)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout.addWidget(self.txtName)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget)
        self.txtPost01 = QtWidgets.QLineEdit(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtPost01.setFont(font)
        self.txtPost01.setStyleSheet("background-color: #120c20;\n"
"color:#C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtPost01.setObjectName("txtPost01")
        self.verticalLayout_2.addWidget(self.txtPost01)
        self.txtPost02 = QtWidgets.QLineEdit(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtPost02.setFont(font)
        self.txtPost02.setStyleSheet("background-color: #120c20;\n"
"color: #C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtPost02.setObjectName("txtPost02")
        self.verticalLayout_2.addWidget(self.txtPost02)
        self.txtPost03 = QtWidgets.QLineEdit(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtPost03.setFont(font)
        self.txtPost03.setStyleSheet("background-color: #120c20;\n"
"color: #C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtPost03.setObjectName("txtPost03")
        self.verticalLayout_2.addWidget(self.txtPost03)
        self.txtPost04 = QtWidgets.QLineEdit(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtPost04.setFont(font)
        self.txtPost04.setStyleSheet("background-color: #120c20;\n"
"color: #C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtPost04.setObjectName("txtPost04")
        self.verticalLayout_2.addWidget(self.txtPost04)
        self.txtPost05 = QtWidgets.QLineEdit(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtPost05.setFont(font)
        self.txtPost05.setStyleSheet("background-color: #120c20;\n"
"color: #C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtPost05.setObjectName("txtPost05")
        self.verticalLayout_2.addWidget(self.txtPost05)
        self.pushButton = QtWidgets.QPushButton(self.mainCard)
        self.pushButton.clicked.connect(self.send_data_to_main)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: #3a1a6e;\n"
"color: #dbd2d4;\n"
"border-radius: 15px;\n"
"padding: 12px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #892CDC;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(InputWindow)
        QtCore.QMetaObject.connectSlotsByName(InputWindow)

    def send_data_to_main(self):
        try:
            name = self.txtName.text().strip()
            posts = [
                self.txtPost01.text().strip(),
                self.txtPost02.text().strip(),
                self.txtPost03.text().strip(),
                self.txtPost04.text().strip(),
                self.txtPost05.text().strip()
            ]

            # Filter out empty posts
            posts = [p for p in posts if p]

            # Validate inputs
            if not name:
                QtWidgets.QMessageBox.warning(None, "Input Error", "Please enter a name")
                return

            if len(posts) < 1:
                QtWidgets.QMessageBox.warning(None, "Input Error", "Please enter at least one post")
                return

            self.predictClicked.emit(name, posts)

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to process input: {str(e)}")


    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lblTitle.setText(_translate("InputWindow", "Vibe Snitch"))
        self.lblSlogan.setText(_translate("InputWindow", "<html><head/><body><p>Drop their posts, and we’ll snitch their vibes.</p></body></html>"))
        self.label.setText(_translate("InputWindow", ""))
        self.txtName.setPlaceholderText(_translate("InputWindow", "Their Name"))
        self.label_2.setText(_translate("InputWindow", ""))
        self.txtPost01.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost02.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost03.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost04.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost05.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.pushButton.setText(_translate("InputWindow", "Predict Personality"))
