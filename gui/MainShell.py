

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtGui import QColor
from db.db_manager import get_current_user
from InputWindow import Ui_InputWindow
from PredictionWindow import Ui_mainForm
import pickle
from ai.gemini_wrapper import get_personality_report
from ai.text_cleaner import TextCleaner
from SavedResultsWindow import Ui_SavedResultsWindow


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
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(50)
        self.shadow.setOffset(0, 0)
        self.shadow.setColor(QColor(0, 0, 0, 150))

        self.header_shadow = QGraphicsDropShadowEffect()
        self.header_shadow.setBlurRadius(30)
        self.header_shadow.setOffset(0, 0)
        self.header_shadow.setColor(QColor(0, 0, 0, 120))

        self.headerFrame = QtWidgets.QFrame(MainShell)
        self.headerFrame.setGeometry(QtCore.QRect(180, 50, 960, 80))
        self.headerFrame.setMinimumSize(QtCore.QSize(960, 80))
        self.headerFrame.setMaximumSize(QtCore.QSize(960, 80))
        self.headerFrame.setGraphicsEffect(self.header_shadow)
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
        self.stackedWidget.setGraphicsEffect(self.shadow)

        self.retranslateUi(MainShell)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainShell)

        # Create the widgets and their UIs
        self.input_widget = QtWidgets.QWidget()
        self.prediction_widget = QtWidgets.QWidget()
        self.saved_results_widget = QtWidgets.QWidget()

        # Initialize the UI classes - modified to ensure proper QObject hierarchy
        self.input_ui = Ui_InputWindow()  # Now properly inherits from QObject
        self.input_ui.setupUi(self.input_widget)

        self.prediction_ui = Ui_mainForm()
        self.prediction_ui.setupUi(self.prediction_widget)

        self.saved_results_ui = Ui_SavedResultsWindow()
        self.saved_results_ui.setupUi(self.saved_results_widget)

        # Add widgets to stacked widget
        self.stackedWidget.addWidget(self.input_widget)
        self.stackedWidget.addWidget(self.prediction_widget)
        self.stackedWidget.addWidget(self.saved_results_widget)
        self.stackedWidget.setCurrentIndex(0)

        # Connect navigation signals
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))

        # Connect signal with error handling
        try:
                self.input_ui.predictClicked.connect(self.handlePredictionRequest)
        except Exception as e:
                QtWidgets.QMessageBox.critical(None, "Connection Error",
                                               f"Failed to connect signals: {str(e)}")
                print(f"Signal connection error: {str(e)}")

    def handlePredictionRequest(self, name, posts):
            try:
                    # Additional input validation
                    if not name or not isinstance(name, str):
                            raise ValueError("Invalid name provided")

                    if not posts or not isinstance(posts, list):
                            raise ValueError("Posts must be a non-empty list")

                    # Show processing message
                    processing_msg = QtWidgets.QMessageBox()
                    processing_msg.setWindowTitle("Processing")
                    processing_msg.setText("Analyzing personality...")
                    processing_msg.setStandardButtons(QtWidgets.QMessageBox.NoButton)
                    processing_msg.show()
                    QtWidgets.QApplication.processEvents()  # Keep UI responsive

                    # --- Your existing prediction code here ---
                    full_text = ' '.join(posts)

                    try:
                            with open('../models/personality_pipeline_lr.pkl', 'rb') as f:
                                    pipeline = pickle.load(f)
                            with open('../models/label_encoder.pkl', 'rb') as f:
                                    label_encoder = pickle.load(f)

                            mbti_type_label = pipeline.predict([full_text])[0]
                            mbti_type = label_encoder.inverse_transform([mbti_type_label])[0]

                    except Exception as e:
                            processing_msg.close()
                            QtWidgets.QMessageBox.critical(None, "Model Error", f"Prediction failed: {str(e)}")
                            return

                    try:
                            report = get_personality_report(mbti_type, posts)
                            if not report:
                                    raise ValueError("Empty report generated")
                    except Exception as e:
                            processing_msg.close()
                            QtWidgets.QMessageBox.critical(None, "API Error", f"Report generation failed: {str(e)}")
                            return

                    # Update UI
                    try:
                            self.prediction_ui.set_prediction(name, mbti_type, report)
                            self.stackedWidget.setCurrentIndex(1)
                    except Exception as e:
                            QtWidgets.QMessageBox.critical(None, "Display Error", f"Failed to show results: {str(e)}")

                    processing_msg.close()

            except Exception as e:
                    QtWidgets.QMessageBox.critical(None, "Error", f"Personality analysis failed: {str(e)}")
                    print(f"Error details: {str(e)}")
    def retranslateUi(self, MainShell):
        _translate = QtCore.QCoreApplication.translate
        MainShell.setWindowTitle(_translate("MainShell", "Vibe Snitch - AI"))
        self.pushButton.setText(_translate("MainShell", " Home"))
        self.pushButton_2.setText(_translate("MainShell", " Saved Results"))
