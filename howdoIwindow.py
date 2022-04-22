from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QGroupBox, QTextEdit, QPushButton
from howdoi import howdoi
import sys

from pip import main
app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HowDoI")

        # Main toolbox
        maintoolbox = QGroupBox("Question")
        maintoolbox.setAlignment(Qt.AlignTop)

        # Widgets
        label = QLabel("Write your question:", maintoolbox)
        self.lineEdit = QLineEdit(maintoolbox)
        self.textbox = QTextEdit()
        self.textbox.setReadOnly(True)
        button = QPushButton("Ask", maintoolbox)
        button.clicked.connect(self.answer_question)

        # Layout
        toolboxlayout = QHBoxLayout()
        toolboxlayout.addWidget(label)
        toolboxlayout.addWidget(self.lineEdit)
        toolboxlayout.addWidget(button)
        toolboxlayout.setAlignment(Qt.AlignTop)
        maintoolbox.setLayout(toolboxlayout)

        # Main layout
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(maintoolbox)
        mainlayout.addWidget(self.textbox)

        # Container
        container = QWidget()
        container.setLayout(mainlayout)
        self.setCentralWidget(container)

    def answer_question(self):
        if __name__ == "__main__":
            answer = howdoi.howdoi(self.lineEdit.text())
            self.textbox.setText(answer)


window = MainWindow()
window.show()

app.exec_()