import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from Extractors import lbp


class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        loadUi('lbp.ui', self)
        self.fillCombobox()
        self.processPushButton.clicked.connect(self.process)
        self.clearTextPushButton.clicked.connect(self.clearMessages)
        self.pathButton.clicked.connect(self.path)

    def process(self):
        method = self.comboBox.currentText()
        radius = self.radiusSpinBox.value()
        sampling_points = self.npointsSpinBox.value()
        path = self.directoryLineEdit.text()
        self.messagesPlainTextEdit.setPlainText("Processing, please wait")
        lbp(path, sampling_points, radius, method)

        self.messagesPlainTextEdit.setPlainText("Success")

    def fillCombobox(self):
        methods = ["default", "ror", "uniform", "nri_uniform", "var"]
        for x in methods:
            self.comboBox.addItem(x)

    def clearMessages(self):
        self.messagesPlainTextEdit.clear()

    def path(self):
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))

        if fileName:
            print(fileName)
            self.directoryLineEdit.setText(fileName)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())
