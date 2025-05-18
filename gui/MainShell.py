

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QColor
from db.db_manager import get_current_user
from InputWindow import Ui_InputWindow
from PredictionWindow import Ui_mainForm
import pickle
from ai.gemini_wrapper import get_personality_report


# Add drop shadow to stackedWidget
shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(50)
shadow.setOffset(0, 0)
shadow.setColor(QColor(0, 0, 0, 150))

# Drop shadow for headerFrame
header_shadow = QGraphicsDropShadowEffect()
header_shadow.setBlurRadius(30)
header_shadow.setOffset(0, 0)
header_shadow.setColor(QColor(0, 0, 0, 120))


class Ui_MainShell(object):
    def setupUi(self, MainShell):
        MainShell.setObjectName("MainShell")
        MainShell.resize(1280, 720)
        MainShell.setMinimumSize(QtCore.QSize(1280, 720))
        MainShell.setMaximumSize(QtCore.QSize(1280, 720))
        MainShell.setStyleSheet("QWidget {\n"
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
        self.headerFrame = QtWidgets.QFrame(MainShell)
        self.headerFrame.setGeometry(QtCore.QRect(180, 50, 960, 80))
        self.headerFrame.setMinimumSize(QtCore.QSize(960, 80))
        self.headerFrame.setMaximumSize(QtCore.QSize(960, 80))
        self.headerFrame.setGraphicsEffect(header_shadow)
        self.headerFrame.setStyleSheet("QFrame#headerFrame {\n"
"background-color: #1a1328;\n"
"    border: 2px solid#26183d;\n"
"    border-radius: 20px;\n"
"}")
        self.headerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerFrame.setObjectName("headerFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.headerFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iconUser = QtWidgets.QLabel(self.headerFrame)
        self.iconUser.setMaximumSize(QtCore.QSize(33, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.iconUser.setFont(font)
        self.iconUser.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"margin-left: 3px;\n"
"font-size: 34pt;")
        self.iconUser.setText("")
        self.iconUser.setPixmap(QtGui.QPixmap("../assets/user.png"))
        self.iconUser.setObjectName("iconUser")
        self.horizontalLayout.addWidget(self.iconUser)
        self.lblUsername = QtWidgets.QLabel(self.headerFrame)
        self.lblUsername.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername.setFont(font)
        self.lblUsername.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"margin-bottom: 3px;\n"
"")
        self.lblUsername.setObjectName("lblUsername")
        self.lblUsername.setText(get_current_user())
        self.horizontalLayout.addWidget(self.lblUsername)
        self.pushButton = QtWidgets.QPushButton(self.headerFrame)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
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
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(22, 22))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_2 = QtWidgets.QPushButton(self.headerFrame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: #3a1a6e;\n"
"color: #dbd2d4;\n"
"border-radius: 15px;\n"
"padding: 12px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #892CDC;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/rectangle-vertical-history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.stackedWidget = QtWidgets.QStackedWidget(MainShell)
        self.stackedWidget.setGeometry(QtCore.QRect(175, 140, 965, 545))
        self.stackedWidget.setMinimumSize(QtCore.QSize(965, 545))
        self.stackedWidget.setMaximumSize(QtCore.QSize(965, 545))
        self.stackedWidget.setStyleSheet("QStackedWidget#stackedWidget {\n"
"background-color: #1a1328;\n"
"    border: 2px solid#26183d;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setGraphicsEffect(shadow)

        self.retranslateUi(MainShell)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainShell)

        self.input_widget = QtWidgets.QWidget()
        self.prediction_widget = QtWidgets.QWidget()
        self.input_ui = Ui_InputWindow()
        self.input_ui.predictClicked.connect(self.handlePredictionRequest)
        self.input_ui.setupUi(self.input_widget)
        self.prediction_ui = Ui_mainForm()
        self.prediction_ui.setupUi(self.prediction_widget)

        self.stackedWidget.addWidget(self.input_widget)
        self.stackedWidget.addWidget(self.prediction_widget)
        self.stackedWidget.setCurrentIndex(0)

    def handlePredictionRequest(self, name, posts):
            try:
                    # --- STEP 1: Join posts for ML pipeline ---
                    full_text = ' '.join(posts)

                    # --- STEP 2: Load ML pipeline and predict MBTI ---
                    with open('models/personality_pipeline_lr.pkl', 'rb') as f:
                            pipeline = pickle.load(f)

                    mbti_type = pipeline.predict([full_text])[0]  # e.g., "INTP"

                    # --- STEP 3: Get Gemini personality report ---
                    report = get_personality_report(mbti_type, posts)

                    if report is None:
                            raise Exception("Gemini API failed or returned invalid JSON.")

                    # --- STEP 4: Send results to PredictionWindow ---
                    self.prediction_ui.set_prediction(name, mbti_type, report)

                    # --- STEP 5: Switch to prediction screen ---
                    self.stackedWidget.setCurrentIndex(1)

            except FileNotFoundError:
                    QMessageBox.critical(None, "Model Error", "❌ Model file not found. Check the 'models' folder.")
            except pickle.UnpicklingError:
                    QMessageBox.critical(None, "Model Error", "❌ Failed to load the model file. It might be corrupted.")
            except Exception as e:
                    print("❌ Error during prediction:", str(e))
                    QMessageBox.critical(None, "Prediction Error", f"Something went wrong:\n{str(e)}")

    def retranslateUi(self, MainShell):
        _translate = QtCore.QCoreApplication.translate
        MainShell.setWindowTitle(_translate("MainShell", "Vibe Snitch - AI"))
        self.pushButton.setText(_translate("MainShell", " Home"))
        self.pushButton_2.setText(_translate("MainShell", " Saved Results"))
