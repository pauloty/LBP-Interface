# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lbp.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_lbp(object):
    def setupUi(self, lbp):
        lbp.setObjectName("lbp")
        lbp.resize(400, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(lbp)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(lbp)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 382, 563))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.processPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.processPushButton.setEnabled(True)
        self.processPushButton.setObjectName("processPushButton")
        self.verticalLayout.addWidget(self.processPushButton)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.messagesPlainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.messagesPlainTextEdit.setReadOnly(True)
        self.messagesPlainTextEdit.setOverwriteMode(True)
        self.messagesPlainTextEdit.setObjectName("messagesPlainTextEdit")
        self.gridLayout_4.addWidget(self.messagesPlainTextEdit, 0, 0, 1, 1)
        self.clearTextPushButton = QtWidgets.QPushButton(self.groupBox)
        self.clearTextPushButton.setObjectName("clearTextPushButton")
        self.gridLayout_4.addWidget(self.clearTextPushButton, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.directoryLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.directoryLineEdit.setObjectName("directoryLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.directoryLineEdit)
        self.label_1 = QtWidgets.QLabel(self.groupBox_2)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.radiusSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.radiusSpinBox.setMinimum(1)
        self.radiusSpinBox.setMaximum(50)
        self.radiusSpinBox.setProperty("value", 2)
        self.radiusSpinBox.setObjectName("radiusSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.radiusSpinBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.npointsSpinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.npointsSpinBox.setMinimum(1)
        self.npointsSpinBox.setMaximum(100)
        self.npointsSpinBox.setProperty("value", 8)
        self.npointsSpinBox.setObjectName("npointsSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.npointsSpinBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.pathButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pathButton.setObjectName("pathButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pathButton)
        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.label_title = QtWidgets.QLabel(lbp)
        self.label_title.setObjectName("label_title")
        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)

        self.retranslateUi(lbp)
        QtCore.QMetaObject.connectSlotsByName(lbp)

    def retranslateUi(self, lbp):
        _translate = QtCore.QCoreApplication.translate
        lbp.setWindowTitle(_translate("lbp", "Form"))
        self.groupBox_3.setTitle(_translate("lbp", "Actions"))
        self.processPushButton.setText(_translate("lbp", "Process"))
        self.groupBox.setTitle(_translate("lbp", "Messages"))
        self.clearTextPushButton.setText(_translate("lbp", "Clear messages"))
        self.groupBox_2.setTitle(_translate("lbp", "Parameters"))
        self.label_1.setText(_translate("lbp", "Radius"))
        self.label_2.setText(_translate("lbp", "Number of Points"))
        self.label_3.setText(_translate("lbp", "Method"))
        self.pathButton.setText(_translate("lbp", "Choose the path"))
        self.label_title.setText(_translate("lbp", "Local Binary Pattern"))

