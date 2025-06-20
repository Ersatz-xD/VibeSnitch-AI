from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from db.db_manager import login_user
from MainShell import Ui_MainShell


class MainShell(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainShell()
        self.ui.setupUi(self)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        self.LoginWindow = LoginWindow
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1280, 720)
        LoginWindow.setMinimumSize(QtCore.QSize(1280, 720))
        LoginWindow.setMaximumSize(QtCore.QSize(1280, 720))
        LoginWindow.setStyleSheet("QWidget#LoginWindow {\n"
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
        self.mainCard = QtWidgets.QFrame(LoginWindow)
        self.mainCard.setGeometry(QtCore.QRect(170, 100, 960, 540))
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
        self.btnLogin = QtWidgets.QPushButton(self.mainCard)
        self.btnLogin.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton {\n"
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
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.handle_login)
        self.verticalLayout_2.addWidget(self.btnLogin)
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
        self.btnGoToSignUp = QtWidgets.QPushButton(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.btnGoToSignUp.setFont(font)
        self.btnGoToSignUp.setStyleSheet("QPushButton {\n"
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
        self.btnGoToSignUp.setObjectName("btnGoToSignUp")
        self.btnGoToSignUp.clicked.connect(self.go_to_signup)
        self.verticalLayout_2.addWidget(self.btnGoToSignUp)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def handle_login(self):
        username = self.txtUsername.text()
        password = self.txtPass.text()
        if not username or not password:
            QMessageBox.warning(self.LoginWindow, "Warning", "Please enter your username and password")
            return
        else:
            try:
                result = login_user(username, password)
                print("login_user returned:", result)
                if result:
                    self.main_shell = MainShell()
                    self.main_shell.show()
                    self.LoginWindow.close()
                else:
                    QMessageBox.warning(self.LoginWindow, "Warning", "Invalid username or password")
            except Exception as e:
                print("Exception occurred in handleLogin:", e)
                QtWidgets.QMessageBox.critical(self.LoginWindow, "Error", "Something went wrong during login.")

    def go_to_signup(self):
        from SignupWindow import Ui_SignupWindow
        self.signup_window = QtWidgets.QMainWindow()
        self.signup_ui = Ui_SignupWindow()
        self.signup_ui.setupUi(self.signup_window)
        self.signup_window.show()
        self.LoginWindow.close()


    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Vibe Snitch - Login"))
        self.lblTitle.setText(_translate("LoginWindow", "Welcome Back!"))
        self.lblSlogan.setText(_translate("LoginWindow", "<html><head/><body><p>Ready to Snitch Some Vibes?</p></body></html>"))
        self.lblUsername.setText(_translate("LoginWindow", "   Username:"))
        self.txtUsername.setPlaceholderText(_translate("LoginWindow", "Enter your username here..."))
        self.label.setText(_translate("LoginWindow", "   Password:"))
        self.txtPass.setPlaceholderText(_translate("LoginWindow", "Enter your password here..."))
        self.btnLogin.setText(_translate("LoginWindow", "Login"))
        self.label_2.setText(_translate("LoginWindow", "Don\'t have an account already?"))
        self.btnGoToSignUp.setText(_translate("LoginWindow", "Sign up"))
