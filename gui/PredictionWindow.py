
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(960, 540)
        mainForm.setMinimumSize(QtCore.QSize(960, 540))
        mainForm.setMaximumSize(QtCore.QSize(960, 540))
        mainForm.setWindowTitle("Vibe Sbitch - Personality Prediction")
        mainForm.setStyleSheet("QWidget {\n"
"       border-radius: 20px;\n"
"       background-color: #1a1328;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(mainForm)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.mainCard = QtWidgets.QFrame(mainForm)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainCard)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblHeader = QtWidgets.QLabel(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.lblHeader.setFont(font)
        self.lblHeader.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"\n"
"")
        self.lblHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHeader.setObjectName("lblHeader")
        self.verticalLayout.addWidget(self.lblHeader)
        self.lblSubtitle = QtWidgets.QLabel(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.lblSubtitle.setFont(font)
        self.lblSubtitle.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"")
        self.lblSubtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSubtitle.setObjectName("lblSubtitle")
        self.verticalLayout.addWidget(self.lblSubtitle)
        self.widget_2 = QtWidgets.QWidget(self.mainCard)
        self.widget_2.setStyleSheet("background-color: transparent")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mbtiBox = QtWidgets.QFrame(self.widget_2)
        self.mbtiBox.setMinimumSize(QtCore.QSize(900, 80))
        self.mbtiBox.setMaximumSize(QtCore.QSize(1000, 120))
        self.mbtiBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mbtiBox.setStyleSheet("QFrame#mbtiBox {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.mbtiBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mbtiBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mbtiBox.setObjectName("mbtiBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mbtiBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.mbtiBox)
        self.widget.setMinimumSize(QtCore.QSize(0, 70))
        self.widget.setStyleSheet("background-color: transparent")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblMbtiType = QtWidgets.QLabel(self.widget)
        self.lblMbtiType.setEnabled(True)
        self.lblMbtiType.setMinimumSize(QtCore.QSize(180, 60))
        self.lblMbtiType.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblMbtiType.setFont(font)
        self.lblMbtiType.setStyleSheet("QLabel {\n"
"    color: #dbd2d4;\n"
"    background-color: #892CDC;\n"
"    padding: 8px 24px;\n"
"    border-radius: 18px;\n"
"}\n"
"")
        self.lblMbtiType.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMbtiType.setObjectName("lblMbtiType")
        self.horizontalLayout.addWidget(self.lblMbtiType)
        self.verticalLayout_2.addWidget(self.widget)
        self.lblSummary = QtWidgets.QLabel(self.mbtiBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lblSummary.setFont(font)
        self.lblSummary.setStyleSheet("\n"
"    color: #EDEBE8;\n"
"    background-color: transparent;\n"
"\n"
"")
        self.lblSummary.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSummary.setWordWrap(True)
        self.lblSummary.setObjectName("lblSummary")
        self.verticalLayout_2.addWidget(self.lblSummary)
        self.horizontalLayout_2.addWidget(self.mbtiBox)
        self.verticalLayout.addWidget(self.widget_2)
        self.lblConfidenceScore = QtWidgets.QLabel(self.mainCard)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblConfidenceScore.setFont(font)
        self.lblConfidenceScore.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"")
        self.lblConfidenceScore.setObjectName("lblConfidenceScore")
        self.verticalLayout.addWidget(self.lblConfidenceScore)
        self.confidanceBar = QtWidgets.QProgressBar(self.mainCard)
        self.confidanceBar.setStyleSheet("QProgressBar {\n"
"    border: 1px solid #52057B;\n"
"    border-radius: 10px;\n"
"    background-color: #2d2146;\n"
"    height: 20px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #892CDC;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.confidanceBar.setProperty("value", 80)
        self.confidanceBar.setTextVisible(False)
        self.confidanceBar.setObjectName("confidanceBar")
        self.verticalLayout.addWidget(self.confidanceBar)
        self.widget_3 = QtWidgets.QWidget(self.mainCard)
        self.widget_3.setStyleSheet("background-color: transparent")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblConfidenceScore_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblConfidenceScore_2.setFont(font)
        self.lblConfidenceScore_2.setStyleSheet("color: #dbd2d4;\n"
"background-color: #1a1328;\n"
"")
        self.lblConfidenceScore_2.setObjectName("lblConfidenceScore_2")
        self.horizontalLayout_3.addWidget(self.lblConfidenceScore_2)
        self.lblTrait_1 = QtWidgets.QLabel(self.widget_3)
        self.lblTrait_1.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lblTrait_1.setFont(font)
        self.lblTrait_1.setStyleSheet("\n"
"    background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"\n"
"")
        self.lblTrait_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTrait_1.setObjectName("lblTrait_1")
        self.horizontalLayout_3.addWidget(self.lblTrait_1)
        self.lblTrait_2 = QtWidgets.QLabel(self.widget_3)
        self.lblTrait_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lblTrait_2.setFont(font)
        self.lblTrait_2.setStyleSheet("\n"
"    background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"")
        self.lblTrait_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTrait_2.setObjectName("lblTrait_2")
        self.horizontalLayout_3.addWidget(self.lblTrait_2)
        self.lblTrait_3 = QtWidgets.QLabel(self.widget_3)
        self.lblTrait_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.lblTrait_3.setFont(font)
        self.lblTrait_3.setStyleSheet("  background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"")
        self.lblTrait_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTrait_3.setObjectName("lblTrait_3")
        self.horizontalLayout_3.addWidget(self.lblTrait_3)
        self.verticalLayout.addWidget(self.widget_3)
        self.detailsSection = QtWidgets.QFrame(self.mainCard)
        self.detailsSection.setMinimumSize(QtCore.QSize(0, 140))
        self.detailsSection.setMaximumSize(QtCore.QSize(16777215, 500))
        self.detailsSection.setStyleSheet("QFrame#detailsSection{ background-color: transparent;\n"
"    border: 1px solid #892CDC;\n"
"    border-radius: 12px;\n"
"}")
        self.detailsSection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailsSection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detailsSection.setObjectName("detailsSection")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.detailsSection)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Strengths = QtWidgets.QWidget(self.detailsSection)
        self.Strengths.setStyleSheet("\n"
" background-color: transparent;")
        self.Strengths.setObjectName("Strengths")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Strengths)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblRelationship = QtWidgets.QLabel(self.Strengths)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblRelationship.setFont(font)
        self.lblRelationship.setStyleSheet("QLabel#lblRelationship{\n"
"    color: #dbd2d4;\n"
"    margin-bottom: 6px;\n"
"}\n"
"")
        self.lblRelationship.setObjectName("lblRelationship")
        self.verticalLayout_3.addWidget(self.lblRelationship)
        self.lblRelationshipDescription = QtWidgets.QLabel(self.Strengths)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.lblRelationshipDescription.setFont(font)
        self.lblRelationshipDescription.setStyleSheet("color: #dbd2d4;")
        self.lblRelationshipDescription.setWordWrap(True)
        self.lblRelationshipDescription.setObjectName("lblRelationshipDescription")
        self.verticalLayout_3.addWidget(self.lblRelationshipDescription)
        self.horizontalLayout_4.addWidget(self.Strengths)
        self.Compatibility = QtWidgets.QWidget(self.detailsSection)
        self.Compatibility.setStyleSheet("\n"
" background-color: transparent;")
        self.Compatibility.setObjectName("Compatibility")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Compatibility)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblCompatibility = QtWidgets.QLabel(self.Compatibility)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblCompatibility.setFont(font)
        self.lblCompatibility.setStyleSheet("QLabel#lblCompatibility{\n"
"    color: #dbd2d4;\n"
"    margin-bottom: 6px;\n"
"}")
        self.lblCompatibility.setObjectName("lblCompatibility")
        self.verticalLayout_4.addWidget(self.lblCompatibility)
        self.widget_4 = QtWidgets.QWidget(self.Compatibility)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("margin 0;\n"
"padding 0;")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comp_1 = QtWidgets.QLabel(self.widget_4)
        self.comp_1.setMinimumSize(QtCore.QSize(0, 0))
        self.comp_1.setMaximumSize(QtCore.QSize(125, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comp_1.setFont(font)
        self.comp_1.setStyleSheet("QLabel{  \n"
" background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    padding: 0px 12px;\n"
"    border-radius: 8px;\n"
"    margin-right: 8px;\n"
"}\n"
"")
        self.comp_1.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_1.setObjectName("comp_1")
        self.gridLayout_2.addWidget(self.comp_1, 0, 0, 1, 1)
        self.comp_3 = QtWidgets.QLabel(self.widget_4)
        self.comp_3.setMinimumSize(QtCore.QSize(0, 0))
        self.comp_3.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.comp_3.setFont(font)
        self.comp_3.setStyleSheet("QLabel{  \n"
" background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    padding: 0px 12px;\n"
"    border-radius: 8px;\n"
"    margin-right: 8px;\n"
"}")
        self.comp_3.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_3.setObjectName("comp_3")
        self.gridLayout_2.addWidget(self.comp_3, 1, 0, 1, 1)
        self.comp_2 = QtWidgets.QLabel(self.widget_4)
        self.comp_2.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comp_2.setFont(font)
        self.comp_2.setStyleSheet("QLabel{  \n"
" background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    padding: 0px 12px;\n"
"    border-radius: 8px;\n"
"    margin-right: 8px;\n"
"}")
        self.comp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_2.setObjectName("comp_2")
        self.gridLayout_2.addWidget(self.comp_2, 0, 1, 1, 1)
        self.comp_4 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.comp_4.setFont(font)
        self.comp_4.setStyleSheet("QLabel{  \n"
" background-color: #892CDC;\n"
"    color: #dbd2d4;\n"
"    padding: 0px 12px;\n"
"    border-radius: 8px;\n"
"    margin-right: 8px;\n"
"}")
        self.comp_4.setAlignment(QtCore.Qt.AlignCenter)
        self.comp_4.setObjectName("comp_4")
        self.gridLayout_2.addWidget(self.comp_4, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.horizontalLayout_4.addWidget(self.Compatibility)
        self.verticalLayout.addWidget(self.detailsSection)
        self.gridLayout.addWidget(self.mainCard, 0, 0, 1, 1)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def set_prediction(self, name, mbti_type, report):
            # Set the user's name
            name = name if name else "Anonymous"

            # Set the MBTI type label
            self.lblMbtiType.setText(str(mbti_type))

            # Set the summary text
            self.lblSummary.setText(report.get('vibe_summary', ''))

            # Set confidence score label and progress bar
            confidence = report.get('confidence_score', '')
            confidence_val = 90 if confidence == 'High' else 60 if confidence == 'Medium' else 30 if confidence == 'Low' else 0
            self.lblConfidenceScore.setText(f"Confidence Level: {confidence}")
            self.confidanceBar.setValue(confidence_val)

            # Set traits (assuming list of traits in report)
            traits = report.get('top_traits', [])
            # Fill trait labels or clear if missing
            self.lblTrait_1.setText(traits[0] if len(traits) > 0 else '')
            self.lblTrait_2.setText(traits[1] if len(traits) > 1 else '')
            self.lblTrait_3.setText(traits[2] if len(traits) > 2 else '')

            # Set relationship behavior description
            relationship = report.get('relationship_behavior', '')
            self.lblRelationshipDescription.setText(relationship)

            # Set compatibility types
            compatible = report.get('friend_compatibility', [])
            self.comp_1.setText(compatible[0] if len(compatible) > 0 else "N/A")
            self.comp_2.setText(compatible[1] if len(compatible) > 1 else "N/A")
            self.comp_3.setText(compatible[2] if len(compatible) > 2 else "N/A")
            self.comp_4.setText(compatible[3] if len(compatible) > 3 else "N/A")


    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        self.lblHeader.setText(_translate("mainForm", "🧠 Personality Insights"))
        self.lblSubtitle.setText(_translate("mainForm", "<html><head/><body><p>Here\'s what their vibe says about them...</p></body></html>"))
        self.lblConfidenceScore_2.setText(_translate("mainForm", "<html><head/><body><p>Top Traits</p></body></html>"))
        self.lblRelationship.setText(_translate("mainForm", "❤️ Relationship Behavior"))
        self.lblCompatibility.setText(_translate("mainForm", "🤝 Friend Compatibility"))
        self.comp_1.setText(_translate("mainForm", "INFJ 85%"))
        self.comp_3.setText(_translate("mainForm", "ENFJ 88%"))
        self.comp_2.setText(_translate("mainForm", "ENTP 81%"))
        self.comp_4.setText(_translate("mainForm", "ENFP 50%"))
