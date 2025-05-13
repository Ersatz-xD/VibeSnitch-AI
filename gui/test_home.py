from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QPushButton, QLineEdit, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QSequentialAnimationGroup, QPauseAnimation, Qt, QPropertyAnimation, QRect, QEasingCurve
import sys

# === Color Palette ===
PRIMARY_COLOR = "#000000"     # black
SECONDARY_COLOR = "#52057B"   # deep purple
TIRTIARY_COLOR = "#892CDC"    # vibrant purple
FOURTH_COLOR = "#BC6FF1"      # light purple
TEXT_COLOR = "#EDEBE8"        # light text for contrast
INPUT_BG = "#1A1A1A"          # dark input field background
HOVER_COLOR = "#6D30B6"       # hover version of secondary

class VibeSnitchDark(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vibe Snitch")
        self.setGeometry(100, 100, 1280, 720)
        self.setStyleSheet(f"background-color: {PRIMARY_COLOR};")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(200, 60, 200, 60)
        layout.setSpacing(25)
        self.setLayout(layout)

        # Title
        self.title = QLabel("🕵️ Vibe Snitch")
        self.title.setFont(QFont("Segoe UI", 36, QFont.Bold))
        self.title.setStyleSheet(f"color: {FOURTH_COLOR};")
        self.title.setAlignment(Qt.AlignCenter)

        # Slogan
        self.slogan = QLabel("Discover who you are through your digital voice. Let's decode your personality.")
        self.slogan.setFont(QFont("Segoe UI", 14))
        self.slogan.setStyleSheet(f"color: {TEXT_COLOR};")
        self.slogan.setAlignment(Qt.AlignCenter)
        self.slogan.setWordWrap(True)

        layout.addWidget(self.title)
        layout.addWidget(self.slogan)

        # Input Fields
        self.inputs = []
        for i in range(5):
            input_box = QLineEdit()
            input_box.setPlaceholderText(f"Post {i+1} - Share your thoughts...")
            input_box.setFont(QFont("Segoe UI", 11))
            input_box.setStyleSheet(f"""
                QLineEdit {{
                    background-color: {INPUT_BG};
                    color: {TEXT_COLOR};
                    padding: 12px;
                    border: 1px solid {TIRTIARY_COLOR};
                    border-radius: 10px;
                }}
                QLineEdit:focus {{
                    border: 1px solid {FOURTH_COLOR};
                }}
            """)
            self.inputs.append(input_box)
            layout.addWidget(input_box)

        # Predict Button
        self.predict_btn = QPushButton("🔍 Predict Personality")
        self.predict_btn.setFont(QFont("Segoe UI", 13, QFont.Bold))
        self.predict_btn.setCursor(Qt.PointingHandCursor)
        self.predict_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {SECONDARY_COLOR};
                color: {TEXT_COLOR};
                padding: 14px;
                border: none;
                border-radius: 10px;
            }}
            QPushButton:hover {{
                background-color: {HOVER_COLOR};
            }}
        """)
        layout.addWidget(self.predict_btn)

        # Animate components
        self.animate_widget(self.title, delay=100)
        self.animate_widget(self.slogan, delay=300)
        for idx, inp in enumerate(self.inputs):
            self.animate_widget(inp, delay=500 + idx * 100)
        self.animate_widget(self.predict_btn, delay=1100)

    def animate_widget(self, widget, delay=0):
        pause = QPauseAnimation(delay)
        animation = QPropertyAnimation(widget, b"geometry")
        animation.setDuration(600)
        animation.setStartValue(QRect(widget.x(), widget.y() - 40, widget.width(), widget.height()))
        animation.setEndValue(QRect(widget.x(), widget.y(), widget.width(), widget.height()))
        animation.setEasingCurve(QEasingCurve.OutCubic)

        group = QSequentialAnimationGroup()
        group.addAnimation(pause)
        group.addAnimation(animation)
        group.start()
        setattr(widget, "_animation", animation)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VibeSnitchDark()
    window.show()
    sys.exit(app.exec_())
