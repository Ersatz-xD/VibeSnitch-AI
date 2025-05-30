from PyQt5 import QtCore, QtGui, QtWidgets
from db.db_manager import signup_user

class Ui_SignupWindow(object):
    def setupUi(self, SignupWindow):
        self.SignupWindow = SignupWindow
        SignupWindow.setObjectName("SignupWindow")
        SignupWindow.resize(1280, 720)
        SignupWindow.setMinimumSize(QtCore.QSize(1280, 720))
        SignupWindow.setMaximumSize(QtCore.QSize(1280, 720))
        SignupWindow.setStyleSheet("QWidget#SignupWindow {\n"
"    background: qlineargradient(\n"
"        spread:pad,\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:1,\n"
"        stop:0 #1c192b,\n"
"        stop:0.2 #434262,\n"
"        stop:0.4 #25223c,\n"
"        stop:0.6 #363353,\n"
"        stop:1 #151321\n"
"    );\n"
"}")
        self.mainCard = QtWidgets.QFrame(SignupWindow)
        self.mainCard.setGeometry(QtCore.QRect(180, 100, 960, 540))
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
        self.lblTitle.setMinimumSize(QtCore.QSize(100, 80))
        self.lblTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
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
        self.lblSlogan.setMinimumSize(QtCore.QSize(0, 40))
        self.lblSlogan.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.lblUsername = QtWidgets.QLabel(self.mainCard)
        self.lblUsername.setMinimumSize(QtCore.QSize(0, 25))
        self.lblUsername.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lblUsername.setFont(font)
        self.lblUsername.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;")
        self.lblUsername.setObjectName("lblUsername")
        self.verticalLayout_2.addWidget(self.lblUsername)
        self.txtUsername = QtWidgets.QLineEdit(self.mainCard)
        self.txtUsername.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtUsername.setFont(font)
        self.txtUsername.setStyleSheet("background-color: #120c20;\n"
"color:#C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtUsername.setObjectName("txtUsername")
        self.verticalLayout_2.addWidget(self.txtUsername)
        self.label = QtWidgets.QLabel(self.mainCard)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.txtPass = QtWidgets.QLineEdit(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.txtPass.setFont(font)
        self.txtPass.setStyleSheet("background-color: #120c20;\n"
"color: #C8C8C8;\n"
"border: 1px solid #2D0B4E;\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.verticalLayout_2.addWidget(self.txtPass)
        self.btnSignup = QtWidgets.QPushButton(self.mainCard)
        self.btnSignup.clicked.connect(self.handleSignup)
        self.btnSignup.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignup.setFont(font)
        self.btnSignup.setStyleSheet("QPushButton {\n"
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
        self.btnSignup.setObjectName("btnSignup")
        self.verticalLayout_2.addWidget(self.btnSignup)
        self.label_2 = QtWidgets.QLabel(self.mainCard)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.btnGoToLogin = QtWidgets.QPushButton(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btnGoToLogin.setFont(font)
        self.btnGoToLogin.setStyleSheet("QPushButton {\n"
"background-color: #553a7d;\n"
"color: #dbd2d4;\n"
"border-radius: 15px;\n"
"padding: 12px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #892CDC;\n"
"}")
        self.btnGoToLogin.setObjectName("btnGoToLogin")
        self.btnGoToLogin.clicked.connect(self.go_to_login)
        self.verticalLayout_2.addWidget(self.btnGoToLogin)

        self.retranslateUi(SignupWindow)
        QtCore.QMetaObject.connectSlotsByName(SignupWindow)

    def handleSignup(self):
        username = self.txtUsername.text().strip()
        password = self.txtPass.text().strip()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self.SignupWindow, "Warning", "Please fill in all fields!")
            return

        print("About to call signup_user...")

        try:
            result = signup_user(username, password)
            print("signup_user returned:", result)

            if result:
                QtWidgets.QMessageBox.information(self.SignupWindow, "Success", "Account created successfully!")
                self.go_to_login()
            else:
                QtWidgets.QMessageBox.critical(self.SignupWindow, "Signup Failed",
                                               "Username already exists. Try a different one.")
        except Exception as e:
            print("Exception occurred in signup_user:", e)
            QtWidgets.QMessageBox.critical(self.SignupWindow, "Error", "Something went wrong during signup.")

    def go_to_login(self):
        from LoginWindow import Ui_LoginWindow

        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_LoginWindow()
        self.login_ui.setupUi(self.login_window)
        self.login_window.show()

        self.SignupWindow.close()

    def retranslateUi(self, SignupWindow):
        _translate = QtCore.QCoreApplication.translate
        SignupWindow.setWindowTitle(_translate("SignupWindow", "Vibe Snitch - Signup"))
        self.lblTitle.setText(_translate("SignupWindow", "Register Now!"))
        self.lblSlogan.setText(_translate("SignupWindow", "<html><head/><body><p>Ready to Snitch Some Vibes?</p></body></html>"))
        self.lblUsername.setText(_translate("SignupWindow", "   Username:"))
        self.txtUsername.setPlaceholderText(_translate("SignupWindow", "Enter your username here..."))
        self.label.setText(_translate("SignupWindow", "   Password:"))
        self.txtPass.setPlaceholderText(_translate("SignupWindow", "Enter your password here..."))
        self.btnSignup.setText(_translate("SignupWindow", "Sign Up"))
        self.label_2.setText(_translate("SignupWindow", "Already have an account?"))
        self.btnGoToLogin.setText(_translate("SignupWindow", "Login"))
