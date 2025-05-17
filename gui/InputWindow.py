from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputWindow(object):
    def setupUi(self, InputWindow):
        InputWindow.setObjectName("InputWindow")
        InputWindow.resize(960, 540)
        InputWindow.setMinimumSize(QtCore.QSize(960, 540))
        InputWindow.setMaximumSize(QtCore.QSize(960, 540))
        InputWindow.setWindowTitle("Vibe Snitch - AI")
        InputWindow.setStyleSheet("QWidget {\n"
" \n"
"background-color: #1a1328;\n"
"border-radius: 20px;\n"
"}")
        self.mainCard = QtWidgets.QFrame(InputWindow)
        self.mainCard.setGeometry(QtCore.QRect(0, 0, 960, 540))
        self.mainCard.setMinimumSize(QtCore.QSize(960, 540))
        self.mainCard.setMaximumSize(QtCore.QSize(960, 540))
        self.mainCard.setStyleSheet("QFrame#mainCard {\n"
"background-color: #1a1328;\n"
"border-radius: 20px;\n"
"border: 2px solid #26183d;\n"
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

    def retranslateUi(self, InputWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lblTitle.setText(_translate("InputWindow", "Vibe Snitch"))
        self.lblSlogan.setText(_translate("InputWindow", "<html><head/><body><p>Drop their posts, and we’ll snitch their vibes.</p></body></html>"))
        self.txtPost01.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost02.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost03.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost04.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.txtPost05.setPlaceholderText(_translate("InputWindow", "Share the thoughts here..."))
        self.pushButton.setText(_translate("InputWindow", "Predict Personality"))
