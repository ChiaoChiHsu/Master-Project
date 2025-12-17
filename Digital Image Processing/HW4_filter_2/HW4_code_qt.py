import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
import cmath
from functools import wraps
import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QColor


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1450, 970)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1441, 951))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_Part1_input = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_input.setGeometry(QtCore.QRect(310, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_input.setFont(font)
        self.pushButton_Part1_input.setObjectName("pushButton_Part1_input")
        self.label_Part1_original = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_original.setGeometry(QtCore.QRect(10, 50, 431, 401))
        self.label_Part1_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_original.setText("")
        self.label_Part1_original.setObjectName("label_Part1_original")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(190, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_Part1_spectrum = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_spectrum.setGeometry(QtCore.QRect(670, 50, 431, 401))
        self.label_Part1_spectrum.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_spectrum.setText("")
        self.label_Part1_spectrum.setObjectName("label_Part1_spectrum")
        self.label_Part1_angle = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_angle.setGeometry(QtCore.QRect(10, 490, 431, 411))
        self.label_Part1_angle.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_angle.setText("")
        self.label_Part1_angle.setObjectName("label_Part1_angle")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(860, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_phase_angle = QtWidgets.QLabel(self.tab_4)
        self.label_phase_angle.setGeometry(QtCore.QRect(180, 460, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_phase_angle.setFont(font)
        self.label_phase_angle.setObjectName("label_phase_angle")
        self.label_Part1_minus = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_minus.setGeometry(QtCore.QRect(670, 490, 431, 411))
        self.label_Part1_minus.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_minus.setText("")
        self.label_Part1_minus.setObjectName("label_Part1_minus")
        self.label_inverse = QtWidgets.QLabel(self.tab_4)
        self.label_inverse.setGeometry(QtCore.QRect(730, 460, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_inverse.setFont(font)
        self.label_inverse.setObjectName("label_inverse")
        self.pushButton_Part1_spectrum = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_spectrum.setGeometry(QtCore.QRect(970, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_spectrum.setFont(font)
        self.pushButton_Part1_spectrum.setObjectName("pushButton_Part1_spectrum")
        self.pushButton_Part1_minus = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_minus.setGeometry(QtCore.QRect(1020, 450, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_minus.setFont(font)
        self.pushButton_Part1_minus.setObjectName("pushButton_Part1_minus")
        self.pushButton_Part1_angle = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_angle.setGeometry(QtCore.QRect(310, 450, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_angle.setFont(font)
        self.pushButton_Part1_angle.setObjectName("pushButton_Part1_angle")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_Part2_ideal = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_ideal.setGeometry(QtCore.QRect(1220, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_ideal.setFont(font)
        self.pushButton_Part2_ideal.setObjectName("pushButton_Part2_ideal")
        self.label_Part2_original = QtWidgets.QLabel(self.tab)
        self.label_Part2_original.setGeometry(QtCore.QRect(10, 40, 411, 391))
        self.label_Part2_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_original.setText("")
        self.label_Part2_original.setObjectName("label_Part2_original")
        self.comboBox_Part2_ideal = QtWidgets.QComboBox(self.tab)
        self.comboBox_Part2_ideal.setGeometry(QtCore.QRect(1210, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part2_ideal.setFont(font)
        self.comboBox_Part2_ideal.setObjectName("comboBox_Part2_ideal")
        self.comboBox_Part2_ideal.addItem("")
        self.comboBox_Part2_ideal.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(190, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_Part2_ideal = QtWidgets.QLabel(self.tab)
        self.label_Part2_ideal.setGeometry(QtCore.QRect(740, 40, 441, 391))
        self.label_Part2_ideal.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_ideal.setText("")
        self.label_Part2_ideal.setObjectName("label_Part2_ideal")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(940, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_Part2_input = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_input.setGeometry(QtCore.QRect(430, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_input.setFont(font)
        self.pushButton_Part2_input.setObjectName("pushButton_Part2_input")
        self.lineEdit_Part2_ideal_D0 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Part2_ideal_D0.setGeometry(QtCore.QRect(1270, 190, 51, 41))
        self.lineEdit_Part2_ideal_D0.setObjectName("lineEdit_Part2_ideal_D0")
        self.comboBox_Part2_gaussian = QtWidgets.QComboBox(self.tab)
        self.comboBox_Part2_gaussian.setGeometry(QtCore.QRect(430, 530, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part2_gaussian.setFont(font)
        self.comboBox_Part2_gaussian.setObjectName("comboBox_Part2_gaussian")
        self.comboBox_Part2_gaussian.addItem("")
        self.comboBox_Part2_gaussian.addItem("")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(1220, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(160, 450, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_Part2_gaussian = QtWidgets.QLabel(self.tab)
        self.label_Part2_gaussian.setGeometry(QtCore.QRect(10, 480, 411, 391))
        self.label_Part2_gaussian.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_gaussian.setText("")
        self.label_Part2_gaussian.setObjectName("label_Part2_gaussian")
        self.pushButton_Part2_gaussian = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_gaussian.setGeometry(QtCore.QRect(440, 670, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_gaussian.setFont(font)
        self.pushButton_Part2_gaussian.setObjectName("pushButton_Part2_gaussian")
        self.lineEdit_Part2_gaussian_D0 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Part2_gaussian_D0.setGeometry(QtCore.QRect(490, 600, 51, 41))
        self.lineEdit_Part2_gaussian_D0.setObjectName("lineEdit_Part2_gaussian_D0")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(440, 610, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(900, 450, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_Part2_butter = QtWidgets.QLabel(self.tab)
        self.label_Part2_butter.setGeometry(QtCore.QRect(740, 480, 441, 391))
        self.label_Part2_butter.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_butter.setText("")
        self.label_Part2_butter.setObjectName("label_Part2_butter")
        self.pushButton_Part2_butter = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_butter.setGeometry(QtCore.QRect(1220, 730, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_butter.setFont(font)
        self.pushButton_Part2_butter.setObjectName("pushButton_Part2_butter")
        self.lineEdit_Part2_butter_D0 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Part2_butter_D0.setGeometry(QtCore.QRect(1260, 590, 51, 41))
        self.lineEdit_Part2_butter_D0.setObjectName("lineEdit_Part2_butter_D0")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(1210, 600, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.comboBox_Part2_butter = QtWidgets.QComboBox(self.tab)
        self.comboBox_Part2_butter.setGeometry(QtCore.QRect(1200, 520, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part2_butter.setFont(font)
        self.comboBox_Part2_butter.setObjectName("comboBox_Part2_butter")
        self.comboBox_Part2_butter.addItem("")
        self.comboBox_Part2_butter.addItem("")
        self.lineEdit_Part2_butter_n = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_Part2_butter_n.setGeometry(QtCore.QRect(1260, 660, 51, 41))
        self.lineEdit_Part2_butter_n.setText("")
        self.lineEdit_Part2_butter_n.setObjectName("lineEdit_Part2_butter_n")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(1210, 670, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_Part3_homomor = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3_homomor.setGeometry(QtCore.QRect(1010, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3_homomor.setFont(font)
        self.pushButton_Part3_homomor.setObjectName("pushButton_Part3_homomor")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(180, 40, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_Part3_original = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_original.setGeometry(QtCore.QRect(10, 80, 400, 400))
        self.label_Part3_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_original.setText("")
        self.label_Part3_original.setObjectName("label_Part3_original")
        self.label_Part3_homomor = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_homomor.setGeometry(QtCore.QRect(520, 80, 400, 400))
        self.label_Part3_homomor.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_homomor.setText("")
        self.label_Part3_homomor.setObjectName("label_Part3_homomor")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(650, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_Part3_input = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3_input.setGeometry(QtCore.QRect(280, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3_input.setFont(font)
        self.pushButton_Part3_input.setObjectName("pushButton_Part3_input")
        self.lineEdit_Part3_D0 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Part3_D0.setGeometry(QtCore.QRect(1040, 230, 51, 41))
        self.lineEdit_Part3_D0.setObjectName("lineEdit_Part3_D0")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(990, 240, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(990, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_Part3_gammaL = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Part3_gammaL.setGeometry(QtCore.QRect(1100, 170, 51, 41))
        self.lineEdit_Part3_gammaL.setObjectName("lineEdit_Part3_gammaL")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(990, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.lineEdit_Part3_gammaH = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Part3_gammaH.setGeometry(QtCore.QRect(1100, 110, 51, 41))
        self.lineEdit_Part3_gammaH.setObjectName("lineEdit_Part3_gammaH")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(610, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_Part4_blur = QtWidgets.QLabel(self.tab_3)
        self.label_Part4_blur.setGeometry(QtCore.QRect(470, 40, 411, 411))
        self.label_Part4_blur.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part4_blur.setText("")
        self.label_Part4_blur.setObjectName("label_Part4_blur")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(1110, 10, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_Part4_deblur = QtWidgets.QLabel(self.tab_3)
        self.label_Part4_deblur.setGeometry(QtCore.QRect(950, 40, 411, 411))
        self.label_Part4_deblur.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part4_deblur.setText("")
        self.label_Part4_deblur.setObjectName("label_Part4_deblur")
        self.label_Part4_original = QtWidgets.QLabel(self.tab_3)
        self.label_Part4_original.setGeometry(QtCore.QRect(10, 40, 411, 411))
        self.label_Part4_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part4_original.setText("")
        self.label_Part4_original.setObjectName("label_Part4_original")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(190, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.pushButton_Part4_input = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Part4_input.setGeometry(QtCore.QRect(130, 460, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part4_input.setFont(font)
        self.pushButton_Part4_input.setObjectName("pushButton_Part4_input")
        self.pushButton_Part4_blur = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Part4_blur.setGeometry(QtCore.QRect(610, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part4_blur.setFont(font)
        self.pushButton_Part4_blur.setObjectName("pushButton_Part4_blur")
        self.comboBox_Part4_blur = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_Part4_blur.setGeometry(QtCore.QRect(550, 470, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part4_blur.setFont(font)
        self.comboBox_Part4_blur.setObjectName("comboBox_Part4_blur")
        self.comboBox_Part4_blur.addItem("")
        self.comboBox_Part4_blur.addItem("")
        self.comboBox_Part4_filter = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_Part4_filter.setGeometry(QtCore.QRect(1030, 470, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part4_filter.setFont(font)
        self.comboBox_Part4_filter.setObjectName("comboBox_Part4_filter")
        self.comboBox_Part4_filter.addItem("")
        self.comboBox_Part4_filter.addItem("")
        self.pushButton_Part4_filter = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Part4_filter.setGeometry(QtCore.QRect(1090, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part4_filter.setFont(font)
        self.pushButton_Part4_filter.setObjectName("pushButton_Part4_filter")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Part1_input.setText(_translate("Form", "Input Image"))
        self.label_15.setText(_translate("Form", "Original"))
        self.label_18.setText(_translate("Form", "Spectrum"))
        self.label_phase_angle.setText(_translate("Form", "Phase angle"))
        self.label_inverse.setText(_translate("Form", "original image minus Inverse FFT"))
        self.pushButton_Part1_spectrum.setText(_translate("Form", "Generate"))
        self.pushButton_Part1_minus.setText(_translate("Form", "Generate"))
        self.pushButton_Part1_angle.setText(_translate("Form", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Part1"))
        self.pushButton_Part2_ideal.setText(_translate("Form", "Generate"))
        self.comboBox_Part2_ideal.setItemText(0, _translate("Form", "lowpass filter"))
        self.comboBox_Part2_ideal.setItemText(1, _translate("Form", "highpass filter"))
        self.label_11.setText(_translate("Form", "Original"))
        self.label_12.setText(_translate("Form", "Ideal filter"))
        self.pushButton_Part2_input.setText(_translate("Form", "Input Image"))
        self.comboBox_Part2_gaussian.setItemText(0, _translate("Form", "lowpass filter"))
        self.comboBox_Part2_gaussian.setItemText(1, _translate("Form", "highpass filter"))
        self.label_16.setText(_translate("Form", "D0 = "))
        self.label_19.setText(_translate("Form", "Gaussian filter"))
        self.pushButton_Part2_gaussian.setText(_translate("Form", "Generate"))
        self.label_21.setText(_translate("Form", "D0 = "))
        self.label_23.setText(_translate("Form", "Butterworth filter"))
        self.pushButton_Part2_butter.setText(_translate("Form", "Generate"))
        self.label_24.setText(_translate("Form", "D0 = "))
        self.comboBox_Part2_butter.setItemText(0, _translate("Form", "lowpass filter"))
        self.comboBox_Part2_butter.setItemText(1, _translate("Form", "highpass filter"))
        self.label_25.setText(_translate("Form", "n = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Part2"))
        self.pushButton_Part3_homomor.setText(_translate("Form", "generate"))
        self.label_8.setText(_translate("Form", "Original"))
        self.label_9.setText(_translate("Form", "Homomorphic filter"))
        self.pushButton_Part3_input.setText(_translate("Form", "Input Image"))
        self.label_26.setText(_translate("Form", "D0 = "))
        self.label_27.setText(_translate("Form", "GammaL = "))
        self.label_28.setText(_translate("Form", "GammaH = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Part3"))
        self.label_10.setText(_translate("Form", " blurred image"))
        self.label_22.setText(_translate("Form", "de-blurring"))
        self.label_13.setText(_translate("Form", "original"))
        self.pushButton_Part4_input.setText(_translate("Form", "Input Image"))
        self.pushButton_Part4_blur.setText(_translate("Form", "generate"))
        self.comboBox_Part4_blur.setItemText(0, _translate("Form", "motion blurred"))
        self.comboBox_Part4_blur.setItemText(1, _translate("Form", "zero-mean white Gaussian noise "))
        self.comboBox_Part4_filter.setItemText(0, _translate("Form", "inverse filter"))
        self.comboBox_Part4_filter.setItemText(1, _translate("Form", "Wiener filter"))
        self.pushButton_Part4_filter.setText(_translate("Form", "generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Part4"))


## -------------------------------------------------------controllor----------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()     #UI.py中class名稱
        self.ui.setupUi(self)
        self.setup_control()
        self.file_path_Part1 = None
        self.file_path_Part2 = None
        self.file_path_Part3 = None
        self.file_path_Part4 = None
## -------------------------------------------------------Part1----------------------------------------------  
    # input image
    def button_clicked_input1(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part1 = file_path
        print('path:', self.file_path_Part1)

        # display on frame of label
        img = cv.imread(self.file_path_Part1, cv.IMREAD_GRAYSCALE)
        qimg = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(431, 401, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_original.setPixmap(pixmap)
        return self.file_path_Part1

    # FFT
    def fft(self, imagepath):   
        img = cv.imread(imagepath, cv.IMREAD_GRAYSCALE)
        f = np.fft.fft2(img)
        # spectrum平移到中心
        shift = np.fft.fftshift(f)
        phase_angle = np.angle(shift)
        # diaplay 只供顯示影像用，請使用shift或f做運算
        display = 20 * np.log(np.abs(shift))
        return img, shift, display, phase_angle

    # inverse FFT
    def ifft(self, spectrum):
        # 反向平移
        shift = np.fft.ifftshift(spectrum)
        img_back = np.fft.ifft2(shift)
        img_back = np.real(img_back)
        return img_back
    
    def display_spectrum(self, imagepath):
        # scale
        X_std = (self.fft(imagepath)[2] - np.min(self.fft(imagepath)[2])) / (255 - 0)
        X_scaled = X_std *(255 - 0) + 0

        X_scaled_reshape = np.clip( X_scaled.reshape((X_scaled.shape[0], X_scaled.shape[1], 1)), 0, 255).astype(np.uint8)

        # display
        qimg = QtGui.QImage(X_scaled_reshape.tobytes(), X_scaled_reshape.shape[1], X_scaled_reshape.shape[0], X_scaled_reshape.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(431, 401, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part1_spectrum.setPixmap(pixmap)

    def display_angle(self, imagepath):
        # display
        angle = self.fft(imagepath)[3].astype(np.uint8)
        qimg = QtGui.QImage(angle.tobytes(), angle.shape[1], angle.shape[0], angle.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(431, 401, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part1_angle.setPixmap(pixmap)

    def display_minus(self, imagepath):
        # display
        img = np.clip(self.fft(imagepath)[0] - self.ifft(self.fft( imagepath)[1]), 0, 255).astype(np.uint8)
        print(img)
        qimg = QtGui.QImage(img.tobytes(), img.shape[1], img.shape[0], img.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(431, 401, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_minus.setPixmap(pixmap)

    # 比較FFT運算時間和影像大小之關係
    def fft_vs_size(imagepath, size):   
        img = cv.imread(imagepath, cv.IMREAD_GRAYSCALE)
        img_re = cv.resize(img, (size, size))
        start_time = time.time()
        # fft
        f = np.fft.fft2(img_re)
        end_time = time.time()
        Computation_time = end_time - start_time
        """
        # spectrum平移到中心
        shift = np.fft.fftshift(f)
        phase_angle = np.angle(shift).astype(np.uint8)
        display = 20 * np.log(np.abs(shift))
        return img, shift, display, phase_angle
        """
        return Computation_time
    # print(fft_vs_size('peka.jpg', 512))
    # print(fft_vs_size('peka.jpg', 1024))
    # print(fft_vs_size('peka.jpg', 2048))   
    
## -------------------------------------------------------Part2----------------------------------------------    
    # input image
    def button_clicked_input2(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part2 = file_path
        print('path:', self.file_path_Part2)

        # display on frame of label
        img = cv.imread(self.file_path_Part2, cv.IMREAD_GRAYSCALE)
        qimg = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(431, 401, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_original.setPixmap(pixmap)
        return self.file_path_Part2
    
    # ideal filter
    def ideal_filter(self, imagepath):
        index = self.ui.comboBox_Part2_ideal.currentIndex()
        r = int(self.ui.lineEdit_Part2_ideal_D0.text())
        img, shift, display , phase_angle = self.fft(imagepath)
        img_h, img_w = img.shape
        origin = [img_h // 2, img_w // 2]

        # filter 
        filter = np.zeros((img_h, img_w), np.uint8)
        for i in range(origin[0] - r, origin[0] + r):
            for j in range(origin[1] - r, origin[1] + r):
                if math.sqrt((i - origin[0]) ** 2 +  (j - origin[1]) **2) <= r:
                    filter[i][j] = 1
                    
        # lowpass/highpass filter   
        if index == 0:         # lowpass filter 
            trans_spectrum = shift * filter
            print('D0 =', r)
            print('lowpass filter')
        elif index == 1:        # highpass filter
            trans_spectrum = shift * (1 - filter)
            print('D0 =', r)
            print('highpass filter')
        return trans_spectrum
    
    # display
    def display_ideal(self, imagepath):
        img = self.ifft( self.ideal_filter(imagepath))
        img_re = np.clip(img.reshape((img.shape[0], img.shape[1], 1)), 0, 255).astype(np.uint8)

        qimg = QtGui.QImage(img_re.tobytes(), img_re.shape[1], img_re.shape[0], img_re.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(441, 391, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part2_ideal.setPixmap(pixmap)
    
    # gaussian filter
    def gaussian_filter(self, imagepath):
        index = self.ui.comboBox_Part2_gaussian.currentIndex()
        D0 = float(self.ui.lineEdit_Part2_gaussian_D0.text())

        img, shift, display , phase_angle = self.fft(imagepath)
        img_h, img_w = img.shape
        origin = [img_h // 2, img_w // 2]
        ratio = 2 * D0 ** 2
        
        # filter 
        filter = np.zeros((img_h, img_w), dtype = np.float16)
        print(filter.shape)
        for i in range(0, img_h):
            for j in range(0, img_w):
                filter[i][j] = math.exp(-((i - origin[0]) ** 2 +  (j - origin[1]) **2) / ratio)
                
        # lowpass/highpass filter
        if index == 0:  
            trans_spectrum = shift * filter
        elif index == 1:
            trans_spectrum = shift * (1 - filter)
        return trans_spectrum
    
    # display
    def display_gaussian(self, imagepath):
        img = self.ifft( self.gaussian_filter(imagepath))
        img_re = np.clip(img.reshape((img.shape[0], img.shape[1], 1)), 0, 255).astype(np.uint8)

        qimg = QtGui.QImage(img_re.tobytes(), img_re.shape[1], img_re.shape[0], img_re.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(411, 391, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part2_gaussian.setPixmap(pixmap)

    # butterworth filter
    def butterworth_filter(self, imagepath):
        index = self.ui.comboBox_Part2_butter.currentIndex()
        D0 = float(self.ui.lineEdit_Part2_butter_D0.text())
        n = float(self.ui.lineEdit_Part2_butter_n.text())

        img, shift, display , phase_angle = self.fft(imagepath)
        img_h, img_w = img.shape
        origin = [img_h // 2, img_w // 2]
        
        # filter 
        filter = np.zeros((img_h, img_w), dtype = np.float16)
        for i in range(0, img_h):
            for j in range(0, img_w):
                filter[i][j] = 1 / (1 + math.pow((math.sqrt((i - origin[0]) ** 2 +  (j - origin[1]) **2) / D0) , 2 * n))

        # lowpass/highpass filter
        if index == 0:            
            trans_spectrum = shift * filter
        elif index == 1:
            trans_spectrum = shift * (1 - filter)
        return trans_spectrum
    
    # display
    def display_butterworth(self, imagepath):
        img = self.ifft( self.butterworth_filter(imagepath))
        img_re = np.clip(img.reshape((img.shape[0], img.shape[1], 1)), 0, 255).astype(np.uint8)

        qimg = QtGui.QImage(img_re.tobytes(), img_re.shape[1], img_re.shape[0], img_re.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(441, 391, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part2_butter.setPixmap(pixmap)
        
        
    
## -------------------------------------------------------Part3----------------------------------------------    
    # input image
    def button_clicked_input3(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part3 = file_path
        print('path:', self.file_path_Part3)

        # display on frame of label
        img = cv.imread(self.file_path_Part3, cv.IMREAD_GRAYSCALE)
        qimg = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part3_original.setPixmap(pixmap)
        return self.file_path_Part3
    
    def homomorphic_filter(self, imagepath):
        D0 = float(self.ui.lineEdit_Part3_D0.text())
        gammaH = float(self.ui.lineEdit_Part3_gammaH.text())
        gammaL = float(self.ui.lineEdit_Part3_gammaL.text())

        img, shift, display , phase_angle = self.fft(imagepath)
        img_h, img_w = img.shape
        origin = [img_h // 2, img_w // 2]
        ratio =  D0 ** 2
        gamma = gammaH - gammaL
        
        # filter 
        filter = np.zeros((img_h, img_w), dtype = np.float16)
        print(filter.shape)
        for i in range(0, img_h):
            for j in range(0, img_w):
                filter[i][j] = (1 - math.exp(- 5 *((i - origin[0]) ** 2 +  (j - origin[1]) **2) / ratio)) * gamma + gammaL
        trans_spectrum = shift * filter
        return trans_spectrum

    # display
    def display_homomorphic(self, imagepath):
        img = self.ifft( self.homomorphic_filter(imagepath))
        img_re = np.clip(img.reshape((img.shape[0], img.shape[1], 1)), 0, 255).astype(np.uint8)

        qimg = QtGui.QImage(img_re.tobytes(), img_re.shape[1], img_re.shape[0], img_re.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part3_homomor.setPixmap(pixmap)
        
    
## -------------------------------------------------------Part4----------------------------------------------  
    # input image
    def button_clicked_input4(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part4 = file_path
        print('path:', self.file_path_Part4)

        # display on frame of label
        img = cv.imread(self.file_path_Part4, cv.IMREAD_GRAYSCALE)
        qimg = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(411, 411, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part4_original.setPixmap(pixmap)
        return self.file_path_Part4
    
    def Part4(self, imagepath):
        img = cv.imread(imagepath, cv.IMREAD_GRAYSCALE)
        eps =1e-6

        def normalize(img):
            return (img - img.min()) / (img.max() - img.min())

        def normalizeWrap(func):
            @wraps(func)
            def wrapFunc(*args, **kwargs):
                return normalize(func(*args, **kwargs))
            return wrapFunc

        def motionFilter(dx, dy):
            """ A motion blur formula """
            def f(i, j):
                uv = (dx * j + dy * i) * np.pi
                filter_feq = np.sin(uv) * np.exp(-1j * uv) / uv
                filter_feq[np.abs(uv) < eps] = 0
                return filter_feq
            return f

        def feqOperationXY(img, func):
            """
            Filtering the map by func in frequency domain.
            The input of func is X and Y.
            """
            # fft
            trans_img = img.copy().astype(np.float64)
            trans_img[0::2, 1::2] *= -1
            trans_img[1::2, 0::2] *= -1
            feq = np.fft.fft2(trans_img)

            # distance and func
            s = img.shape
            j, i = np.meshgrid(np.arange(s[1]) - s[1] // 2,
                            np.arange(s[0]) - s[0] // 2)
            filter_feq = func(i, j)

            # inverse
            filter_img = np.fft.ifft2(filter_feq * feq)
            filter_img[0::2, 1::2] *= -1
            filter_img[1::2, 0::2] *= -1
            filter_img = np.real(filter_img)

            # Ensure the data type is uint8
            filter_img = (filter_img - filter_img.min()) / (filter_img.max() - filter_img.min()) * 255
            filter_img = filter_img.astype(np.uint8)

            return filter_img


        @normalizeWrap
        # 用這個
        def motionBlur(img, dx, dy):
            """ Degradation by Motion  """
            return feqOperationXY(img, motionFilter(dx, dy))

        # 用這個
        def noiseGaussian(img, mean, sig):
            """ Add noise: gaussian """
            return img + np.random.normal(mean / 255, np.sqrt(sig) / 255, img.shape)

        @normalizeWrap
        def invFilter(img, formula):
            """ Reconstruction by genernal inverse filter """
            def filterInv(i, j):
                filter_feq = formula(i, j)
                filter_feq[np.abs(filter_feq) < eps] = np.inf
                return filter_feq ** -1
            return feqOperationXY(img, filterInv)

        @normalizeWrap
        def wienerFilter(img, k, formula):
            """ Degradation by Motion  """
            def wiener(i, j):
                feq = formula(i, j)
                return feq.conj() / (np.abs(feq) ** 2 + k)
            return feqOperationXY(img, wiener)


        def motionInv(img, dx, dy):
            """ Reconstruction Motion by Inverse """
            return invFilter(img, motionFilter(dx, dy))


        def motionWiener(img, k, dx, dy):
            """ Reconstruction Motion by Wiener """
            return wienerFilter(img, k, motionFilter(dx, dy))

        img = cv.imread('C1HW04_IMG02_2022.bmp', 0)

        blur = motionBlur(img, 0.1, 0.1)
        noise = noiseGaussian(blur, 0, 20)
        inv_img = motionInv(noise, 0.1, 0.1)
        wie_img = motionWiener(noise, k = 0.001, dx = 0.1, dy = 0.1)
        return inv_img, wie_img, inv_img, wie_img 

    def motion_blurred(self, imagepath):
        img, shift, display , phase_angle = self.fft(imagepath)
        img_h, img_w = img.shape
        origin = [img_h // 2, img_w // 2]

        # filter
        motion_filter = np.zeros((img_h, img_w), dtype = complex)
        print(motion_filter.shape)
        for i in range(0 - origin[1], img_h - origin[1]):
            for j in range(0 - origin[0], img_w - origin[0]):
                tmp = i * 0.1 + j * 0.1
                power = complex(0, - math.pi * tmp)
                if tmp == 0:
                    continue
                else:
                    motion_filter[i, j] = (1 / (math.pi * tmp)) * math.sin(math.pi * tmp) * cmath.exp(power)

        trans_spectrum = shift * motion_filter
        return trans_spectrum, motion_filter
    
    def display_blur(self, imagepath):
        index = self.ui.comboBox_Part4_blur.currentIndex()
        if index == 0:
            img = self.motion_blurred(imagepath)[0]
            img = self.ifft(img)
            img_re = np.clip(img.reshape((img.shape[0], img.shape[1], 1)), 0, 255).astype(np.uint8)
        elif index == 1:
            img_re = self.Part4(imagepath)[1]

        qimg = QtGui.QImage(img_re.tobytes(), img_re.shape[1], img_re.shape[0], img_re.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(411, 411, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part4_blur.setPixmap(pixmap)

    def display_filter(self, imagepath):
        index = self.ui.comboBox_Part4_filter.currentIndex()
        if index == 0:
            img = self.Part4(imagepath)[2]
            img_re = np.clip(img.reshape((img.shape[0], img.shape[1], 1)), 0, 255).astype(np.uint8)
        elif index == 1:
            img_re = self.Part4(imagepath)[3]

        qimg = QtGui.QImage(img_re.tobytes(), img_re.shape[1], img_re.shape[0], img_re.shape[1], QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    # 轉成QPixmap
        pixmap = pixmap.scaled(411, 411, QtCore.Qt.KeepAspectRatio) # 縮小圖片並保持比例
        self.ui.label_Part4_deblur.setPixmap(pixmap)


 ## -------------------------------------------------------controller----------------------------------------------     
    def setup_control(self):
        # Part 1
        self.ui.pushButton_Part1_input.clicked.connect(self.button_clicked_input1)
        self.ui.pushButton_Part1_spectrum.clicked.connect(lambda: self.display_spectrum(self.file_path_Part1))
        self.ui.pushButton_Part1_angle.clicked.connect(lambda: self.display_angle(self.file_path_Part1))
        self.ui.pushButton_Part1_minus.clicked.connect(lambda: self.display_minus(self.file_path_Part1))
        # Part2
        self.ui.pushButton_Part2_input.clicked.connect(self.button_clicked_input2)
        self.ui.pushButton_Part2_ideal.clicked.connect(lambda: self.display_ideal(self.file_path_Part2))
        self.ui.pushButton_Part2_gaussian.clicked.connect(lambda: self.display_gaussian(self.file_path_Part2))
        self.ui.pushButton_Part2_butter.clicked.connect(lambda: self.display_butterworth(self.file_path_Part2))
        # Part3
        self.ui.pushButton_Part3_input.clicked.connect(self.button_clicked_input3)
        self.ui.pushButton_Part3_homomor.clicked.connect(lambda: self.display_homomorphic(self.file_path_Part3))
        # Part4
        self.ui.pushButton_Part4_input.clicked.connect(self.button_clicked_input4)
        self.ui.pushButton_Part4_blur.clicked.connect(lambda: self.display_blur(self.file_path_Part4))
        self.ui.pushButton_Part4_filter.clicked.connect(lambda: self.display_filter(self.file_path_Part4))
        return

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())