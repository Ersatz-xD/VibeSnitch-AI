from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QProgressBar, QSizePolicy
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import Qt

class ResultsCardWidget(QWidget):
    def __init__(self, personality_type, name, description, confidence_level, parent=None):
        super().__init__(parent)

        # Main layout
        self.setStyleSheet("""
            QWidget {
                background-color: #26183d;
                border: 2px solid #35214b;
                border-radius: 16px;
            }
            QLabel {
                color: #dbd2d4;
            }
        """)
        self.setFixedHeight(130)

        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(15, 10, 15, 10)
        main_layout.setSpacing(20)

        # Personality type block
        self.personality_label = QLabel(personality_type)
        self.personality_label.setStyleSheet("""
            QLabel {
                background-color: #5d28d0;
                color: #dbd2d4;
                border-radius: 12px;
                padding: 12px 20px;
                font: bold 18px 'Segoe UI';
            }
        """)
        self.personality_label.setAlignment(Qt.AlignCenter)

        # Right side: Name, Description, Confidence
        content_layout = QVBoxLayout()
        content_layout.setSpacing(6)

        self.name_label = QLabel(f"{name}'s Results")
        self.name_label.setFont(QFont("Segoe UI", 16, QFont.Bold))
        self.description_label = QLabel(description)
        self.description_label.setWordWrap(True)

        self.confidence_label = QLabel(f"Confidence Level: {confidence_level}")
        self.progress = QProgressBar()
        self.progress.setMaximum(100)
        self.progress.setValue(self.confidence_to_value(confidence_level))
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #1a1328;
                border: 1px solid #3c2c52;
                border-radius: 5px;
                height: 6px;
            }
            QProgressBar::chunk {
                background-color: #792be3;
                border-radius: 5px;
            }
        """)

        content_layout.addWidget(self.name_label)
        content_layout.addWidget(self.description_label)
        content_layout.addWidget(self.confidence_label)
        content_layout.addWidget(self.progress)

        main_layout.addWidget(self.personality_label)
        main_layout.addLayout(content_layout)
        self.setLayout(main_layout)

    def confidence_to_value(self, level):
        mapping = {
            "High": 90,
            "Medium": 60,
            "Low": 30
        }
        return mapping.get(level, 50)
