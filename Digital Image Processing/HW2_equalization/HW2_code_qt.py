import numpy as np
import cv2
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QColor

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1054, 502)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1031, 491))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 20, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_Q1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Q1.setGeometry(QtCore.QRect(170, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q1.setFont(font)
        self.pushButton_Q1.setObjectName("pushButton_Q1")
        self.label_Q1 = QtWidgets.QLabel(self.tab)
        self.label_Q1.setGeometry(QtCore.QRect(60, 120, 316, 316))
        self.label_Q1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q1.setText("")
        self.label_Q1.setObjectName("label_Q1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 691, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_Q2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Q2.setGeometry(QtCore.QRect(510, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q2.setFont(font)
        self.pushButton_Q2.setObjectName("pushButton_Q2")
        self.label_Q2_3 = QtWidgets.QLabel(self.tab_2)
        self.label_Q2_3.setGeometry(QtCore.QRect(700, 140, 316, 316))
        self.label_Q2_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q2_3.setText("")
        self.label_Q2_3.setObjectName("label_Q2_3")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(830, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(170, 110, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_Q2_1 = QtWidgets.QLabel(self.tab_2)
        self.label_Q2_1.setGeometry(QtCore.QRect(20, 140, 316, 316))
        self.label_Q2_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q2_1.setText("")
        self.label_Q2_1.setObjectName("label_Q2_1")
        self.label_Q2_2 = QtWidgets.QLabel(self.tab_2)
        self.label_Q2_2.setGeometry(QtCore.QRect(360, 140, 316, 316))
        self.label_Q2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q2_2.setText("")
        self.label_Q2_2.setObjectName("label_Q2_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(510, 110, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_Q3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Q3.setGeometry(QtCore.QRect(160, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q3.setFont(font)
        self.pushButton_Q3.setObjectName("pushButton_Q3")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(150, 110, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_Q3_1 = QtWidgets.QLabel(self.tab_3)
        self.label_Q3_1.setGeometry(QtCore.QRect(40, 140, 316, 316))
        self.label_Q3_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q3_1.setText("")
        self.label_Q3_1.setObjectName("label_Q3_1")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(520, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_Q3_2 = QtWidgets.QLabel(self.tab_3)
        self.label_Q3_2.setGeometry(QtCore.QRect(400, 140, 316, 316))
        self.label_Q3_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q3_2.setText("")
        self.label_Q3_2.setObjectName("label_Q3_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(80, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_Q4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Q4.setGeometry(QtCore.QRect(70, 310, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q4.setFont(font)
        self.pushButton_Q4.setObjectName("pushButton_Q4")
        self.verticalSlider = QtWidgets.QSlider(self.tab_4)
        self.verticalSlider.setGeometry(QtCore.QRect(100, 110, 16, 181))
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label_threshold = QtWidgets.QLabel(self.tab_4)
        self.label_threshold.setGeometry(QtCore.QRect(130, 180, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_threshold.setFont(font)
        self.label_threshold.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_threshold.setText("")
        self.label_threshold.setObjectName("label_threshold")
        self.label_Q4_1 = QtWidgets.QLabel(self.tab_4)
        self.label_Q4_1.setGeometry(QtCore.QRect(230, 90, 316, 316))
        self.label_Q4_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q4_1.setText("")
        self.label_Q4_1.setObjectName("label_Q4_1")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(340, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_Q4_2 = QtWidgets.QLabel(self.tab_4)
        self.label_Q4_2.setGeometry(QtCore.QRect(580, 90, 316, 316))
        self.label_Q4_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q4_2.setText("")
        self.label_Q4_2.setObjectName("label_Q4_2")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(690, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 721, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_Q5 = QtWidgets.QLabel(self.tab_5)
        self.label_Q5.setGeometry(QtCore.QRect(370, 60, 400, 400))
        self.label_Q5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q5.setText("")
        self.label_Q5.setObjectName("label_Q5")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(30, 240, 53, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.pushButton_Q5 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_Q5.setGeometry(QtCore.QRect(140, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q5.setFont(font)
        self.pushButton_Q5.setObjectName("pushButton_Q5")
        self.spinBox = QtWidgets.QSpinBox(self.tab_5)
        self.spinBox.setGeometry(QtCore.QRect(80, 240, 81, 24))
        self.spinBox.setMaximum(8)
        self.spinBox.setObjectName("spinBox")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setGeometry(QtCore.QRect(40, 140, 53, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_5)
        self.label_25.setGeometry(QtCore.QRect(40, 180, 53, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalSlider_h = QtWidgets.QSlider(self.tab_5)
        self.horizontalSlider_h.setGeometry(QtCore.QRect(90, 140, 251, 16))
        self.horizontalSlider_h.setMaximum(400)
        self.horizontalSlider_h.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_h.setObjectName("horizontalSlider_h")
        self.horizontalSlider_w = QtWidgets.QSlider(self.tab_5)
        self.horizontalSlider_w.setGeometry(QtCore.QRect(90, 180, 251, 16))
        self.horizontalSlider_w.setMaximum(400)
        self.horizontalSlider_w.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_w.setObjectName("horizontalSlider_w")
        self.label_height = QtWidgets.QLabel(self.tab_5)
        self.label_height.setGeometry(QtCore.QRect(200, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_height.setFont(font)
        self.label_height.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_height.setText("")
        self.label_height.setObjectName("label_height")
        self.label_width = QtWidgets.QLabel(self.tab_5)
        self.label_width.setGeometry(QtCore.QRect(200, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_width.setFont(font)
        self.label_width.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_width.setText("")
        self.label_width.setObjectName("label_width")
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(30, 60, 321, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_Q6_1 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_Q6_1.setGeometry(QtCore.QRect(100, 90, 113, 23))
        self.lineEdit_Q6_1.setObjectName("lineEdit_Q6_1")
        self.lineEdit_Q6_2 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_Q6_2.setGeometry(QtCore.QRect(100, 160, 113, 23))
        self.lineEdit_Q6_2.setObjectName("lineEdit_Q6_2")
        self.label_17 = QtWidgets.QLabel(self.tab_6)
        self.label_17.setGeometry(QtCore.QRect(12, 90, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(12, 160, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.pushButton_Q6 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_Q6.setGeometry(QtCore.QRect(70, 210, 80, 24))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q6.setFont(font)
        self.pushButton_Q6.setObjectName("pushButton_Q6")
        self.label_13 = QtWidgets.QLabel(self.tab_6)
        self.label_13.setGeometry(QtCore.QRect(360, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_Q6_1 = QtWidgets.QLabel(self.tab_6)
        self.label_Q6_1.setGeometry(QtCore.QRect(240, 90, 316, 316))
        self.label_Q6_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q6_1.setText("")
        self.label_Q6_1.setObjectName("label_Q6_1")
        self.label_14 = QtWidgets.QLabel(self.tab_6)
        self.label_14.setGeometry(QtCore.QRect(710, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_Q6_2 = QtWidgets.QLabel(self.tab_6)
        self.label_Q6_2.setGeometry(QtCore.QRect(590, 90, 316, 316))
        self.label_Q6_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q6_2.setText("")
        self.label_Q6_2.setObjectName("label_Q6_2")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_7 = QtWidgets.QLabel(self.tab_7)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_Q7_1 = QtWidgets.QLabel(self.tab_7)
        self.label_Q7_1.setGeometry(QtCore.QRect(50, 130, 316, 316))
        self.label_Q7_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q7_1.setText("")
        self.label_Q7_1.setObjectName("label_Q7_1")
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(170, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_7)
        self.label_21.setGeometry(QtCore.QRect(490, 100, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_Q7_2 = QtWidgets.QLabel(self.tab_7)
        self.label_Q7_2.setGeometry(QtCore.QRect(390, 130, 316, 316))
        self.label_Q7_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q7_2.setText("")
        self.label_Q7_2.setObjectName("label_Q7_2")
        self.pushButton_Q7 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_Q7.setGeometry(QtCore.QRect(230, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Q7.setFont(font)
        self.pushButton_Q7.setObjectName("pushButton_Q7")
        self.label_Q7_3 = QtWidgets.QLabel(self.tab_7)
        self.label_Q7_3.setGeometry(QtCore.QRect(800, 30, 200, 200))
        self.label_Q7_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q7_3.setText("")
        self.label_Q7_3.setObjectName("label_Q7_3")
        self.label_27 = QtWidgets.QLabel(self.tab_7)
        self.label_27.setGeometry(QtCore.QRect(850, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_7)
        self.label_28.setGeometry(QtCore.QRect(840, 240, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_Q7_4 = QtWidgets.QLabel(self.tab_7)
        self.label_Q7_4.setGeometry(QtCore.QRect(800, 260, 200, 200))
        self.label_Q7_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Q7_4.setText("")
        self.label_Q7_4.setObjectName("label_Q7_4")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "1. Read a color BMP or JPEG image file and display it."))
        self.pushButton_Q1.setText(_translate("Form", "load image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Q1"))
        self.label_2.setText(_translate("Form", "2. Convert a color image into a grayscale image using the following equations: \n"
"A. GRAY = (R+G+B)/3.0 \n"
"B. GRAY = 0.299*R + 0.587*G + 0.114*B\n"
"Compare the grayscale images obtained from the above equations."))
        self.pushButton_Q2.setText(_translate("Form", "generate"))
        self.label_26.setText(_translate("Form", "abs(A - B)"))
        self.label_8.setText(_translate("Form", "A"))
        self.label_9.setText(_translate("Form", "B"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Q2"))
        self.label_3.setText(_translate("Form", "3. Determine and display the histogram of a grayscale image."))
        self.pushButton_Q3.setText(_translate("Form", "generate"))
        self.label_10.setText(_translate("Form", "Original image"))
        self.label_22.setText(_translate("Form", "Histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Q3"))
        self.label_4.setText(_translate("Form", "4. Implement a manual threshold function to convert a grayscale image into a binary image."))
        self.label_12.setText(_translate("Form", "threshold"))
        self.pushButton_Q4.setText(_translate("Form", "generate"))
        self.label_19.setText(_translate("Form", "Original image"))
        self.label_23.setText(_translate("Form", "Binary image "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Q4"))
        self.label_5.setText(_translate("Form", "5. Implement a function to adjust the spatial resolution (enlarge or shrink) and grayscale levels of an image."))
        self.label_15.setText(_translate("Form", "resolution："))
        self.label_16.setText(_translate("Form", "bits"))
        self.pushButton_Q5.setText(_translate("Form", "generate"))
        self.label_24.setText(_translate("Form", "height"))
        self.label_25.setText(_translate("Form", "width"))
        self.label_11.setText(_translate("Form", "**此題運算量較大，按完按鈕請稍等幾十秒**"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Q5"))
        self.label_6.setText(_translate("Form", "6. Implement a function to adjust the brightness and constrast of an image."))
        self.lineEdit_Q6_1.setPlaceholderText(_translate("Form", "1"))
        self.lineEdit_Q6_2.setPlaceholderText(_translate("Form", "1"))
        self.label_17.setText(_translate("Form", "brightness"))
        self.label_18.setText(_translate("Form", "contrast"))
        self.pushButton_Q6.setText(_translate("Form", "generate"))
        self.label_13.setText(_translate("Form", "Origin image"))
        self.label_14.setText(_translate("Form", "Adjust image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Q6"))
        self.label_7.setText(_translate("Form", "7. Implement a histogram equalization function for automatic constrast adjustment."))
        self.label_20.setText(_translate("Form", "Original image"))
        self.label_21.setText(_translate("Form", "Histogram equalization"))
        self.pushButton_Q7.setText(_translate("Form", "generate"))
        self.label_27.setText(_translate("Form", "Original histogram"))
        self.label_28.setText(_translate("Form", "Equalized histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Q7"))


## -------------------------------------------------------controllor----------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()     #UI.py中class名稱
        self.ui.setupUi(self)
        self.setup_control()

    def load(self,filename):
        img = cv2.imread(filename)  # read image
        img =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h,w,d = img.shape   # shape of image
        return img,h,w,d
    
    # convert RGB image into Grayscale A. GRAY = (R+G+B)/3.0 
    def RGB2GRAY_A(self, filename):   
        img,h,w,d = self.load(filename)  # load image
        A_gray = np.zeros((h,w), dtype=np.uint8)    # 初始化成uint8以儲存灰階值
        for i in range(0,h):
            for j in range(0,w):
                tmp = (img[i][j][0] + img[i][j][1] + img[i][j][2]) / 3
                A_gray[i][j] = int(tmp)  
        return A_gray

    # convert RGB image into Grayscale B. GRAY = 0.299*R + 0.587*G + 0.114*B
    def RGB2GRAY_B(self, filename):   
        img,h,w,d = self.load(filename)  # load image
        B_gray = np.zeros((h,w), dtype=np.uint8)    # 初始化矩陣以儲存灰階值
        for i in range(0,h):
            for j in range(0,w):
                tmp = (img[i][j][0]) * 0.299 + (img[i][j][1]) * 0.587 + (img[i][j][2]) * 0.114
                B_gray[i][j] = int(tmp)
        return B_gray

    def histogram(self,filename):   # input img_name and img_arr to calculate histogram
        img_arr = self.RGB2GRAY_B(filename) # grayscale image
        h,w = img_arr.shape
        his_arr = np.zeros(256, np.uint16)
        for i in range(0,h):
            for j in range(0,w):
                tmp = int(img_arr[i][j])
                his_arr[tmp] = his_arr[tmp] + 1
        
        # 畫直方圖
        hist_height = h
        hist_width = w
        hist_image = np.zeros((hist_height, hist_width), dtype=np.uint8) #要用uint8才能cv2正常顯示
        # Perform min-max scaling
        min_val = 0
        max_val = np.max(his_arr)
        scaled_matrix = (his_arr - min_val) / (max_val - min_val)*hist_height
        bin_width = hist_width // 256    #每條直方圖的寬度
        for i in range(256):
            x1 = i * bin_width
            x2 = (i + 1) * bin_width
            y1 = hist_height
            y2 =hist_height - int(scaled_matrix[i])
            color = (255)  # (B,G,R)藍色
            thickness = -1  # 將長方形填滿
            cv2.rectangle(hist_image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)     
        # hist_image = cv2.resize(hist_image, (200,200))
        hist_image =hist_image.astype("uint8")
        return hist_image

    def manual_binary(self,filename,threshold):
        img_arr = self.RGB2GRAY_B(filename) # grayscale image
        h,w = img_arr.shape
        binary_arr = np.zeros((h,w),np.uint8)

        for i in range(0,h):
            for j in range(0,w):
                if img_arr[i][j] >= threshold:    # 大於閥值則設為255
                    binary_arr[i][j]=255
                else:   # 小於閥值則設為0
                    binary_arr[i][j]=0
        return binary_arr

    def nearest_neighbour(self,filename, neigh_h, neigh_w ,level):
        # (1) adjust the spatial resolution
        img,h,w,d = self.load(filename)  # load image

        neigh_arr = np.zeros((neigh_h, neigh_w,3), dtype=np.uint8)     # 初始化矩陣以儲存新影像
        for i in range(0,neigh_w):
            for j in range(0,neigh_h):            
                new_x = i * (w/neigh_w)     # 原影像像素映射到新影像的位置
                new_y = j * (h/neigh_h)  
                new_x = np.clip(int(np.around(new_x)), 0, w-1)           
                new_y = np.clip(int(np.around(new_y)), 0, h-1)        
                neigh_arr [j, i, :] = img[new_y, new_x, :]

        neigh_arr_gray = np.zeros((neigh_h, neigh_w), dtype=np.uint8)    # 初始化矩陣以儲存灰階值
        for i in range(0, neigh_h):
            for j in range(0,neigh_w):
                tmp = (neigh_arr[i][j][0]) * 0.299 + (neigh_arr[i][j][1]) * 0.587 + (neigh_arr[i][j][2]) * 0.114
                neigh_arr_gray[i][j] = int(tmp)

        # (2) grayscale level
        gray_arr = np.zeros((neigh_h, neigh_w), dtype=np.uint8)    # 初始化矩陣以儲存新影像
        L = 2**(level)
        arr = np.arange(0,255,256/L)     
        for i in range(0,neigh_h):
            for j in range(0,neigh_w): 
                for k in range(0,len(arr)):
                    if k == 0: 
                        tmp = 0
                    else:    
                        tmp = int(arr[k-1])
                    if neigh_arr_gray[i][j]<=int(arr[k]) and neigh_arr_gray[i][j]>tmp:
                        gray_arr[i][j]=arr[k]
                        break
        return gray_arr

    def adjust_brightness_contrast(self,filename, brightness_factor, contrast_factor):
        """
        Adjust the brightness and contrast of an image.
        :param brightness_factor: Factor to adjust brightness (1.0 is no change).
        :param contrast_factor: Factor to adjust contrast (1.0 is no change).
        :return: Adjusted image (PIL Image object).
        """
        # Create a copy of the input image
        img,h,w,d = self.load(filename)  # load image
        adjusted_image = np.copy(img)
        adjusted_image = adjusted_image.astype(np.float64)
        # Adjust brightness
        print(adjusted_image[:,:,0])
        adjusted_image[:,:,0] = adjusted_image[:,:,0] * brightness_factor
        adjusted_image[:,:,1] = adjusted_image[:,:,1] * brightness_factor
        adjusted_image[:,:,2] = adjusted_image[:,:,2] * brightness_factor
        adjusted_image = np.clip(adjusted_image, 0, 255)
        print(adjusted_image[:,:,0])
        # Adjust contrast
        adjusted_image[:,:,0] = ((adjusted_image[:,:,0] / 255.0 - 0.5) * contrast_factor + 0.5) * 255.0
        adjusted_image[:,:,1] = ((adjusted_image[:,:,1] / 255.0 - 0.5) * contrast_factor + 0.5) * 255.0
        adjusted_image[:,:,2] = ((adjusted_image[:,:,2] / 255.0 - 0.5) * contrast_factor + 0.5) * 255.0
        adjusted_image = np.clip(adjusted_image, 0, 255)
        adjusted_image = adjusted_image.astype(np.uint8) #轉回uint8才能正常print到qt
        return  adjusted_image

    def histogram_equalization_gray(self, filename):
        img= self.RGB2GRAY_B(filename)  # load image
        h, w = img.shape
        # 計算直方圖
        histogram = np.zeros(256, dtype=int)
        for i in range(h):
            for j in range(w):
                pixel_value = img[i, j]
                histogram[pixel_value] += 1
        # 計算累積機率函數(CDF)
        cumulative_histogram = np.cumsum(histogram)

        # 計算histogram equalization後的映射表
        mapping_table = (cumulative_histogram - cumulative_histogram.min()) * 255 / (cumulative_histogram.max() - cumulative_histogram.min())
        mapping_table = mapping_table.astype(int)

        # 利用映射表將原圖做histogram equalization
        equalized_image = np.zeros_like(img)
        for i in range(h):
            for j in range(w):
                equalized_image[i, j] = mapping_table[img[i, j]]

        histogram_equalized = np.zeros(256, dtype=int)
        for i in range(h):
            for j in range(w):
                pixel_value = equalized_image[i, j]
                histogram_equalized[pixel_value] += 1
        
        # 畫直方圖
        hist_height = h
        hist_width = w
        hist_image = np.zeros((hist_height, hist_width), dtype=np.uint8) #要用uint8才能cv2正常顯示
        # Perform min-max scaling
        min_val = 0
        max_val = np.max(histogram_equalized)
        scaled_matrix = (histogram_equalized - min_val) / (max_val - min_val)*hist_height
        bin_width = hist_width // 256    #每條直方圖的寬度
        for i in range(256):
            x1 = i * bin_width
            x2 = (i + 1) * bin_width
            y1 = hist_height
            y2 =hist_height - int(scaled_matrix[i])
            color = (255)  # (B,G,R)藍色
            thickness = -1  # 將長方形填滿
            cv2.rectangle(hist_image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)     
        hist_image = cv2.resize(hist_image, (200,200))
        hist_image =hist_image.astype("uint8")

        return equalized_image, hist_image

    ## Q1
    def Q1(self, filename):
        img,h,w,d = self.load(filename)
        bytesPerline = w * d
        self.myqimage = QImage(img, w, h, bytesPerline, QImage.Format_RGB888)
        self.ui.label_Q1.setPixmap(QPixmap.fromImage(self.myqimage))
    ## Q2
    def Q2(self,filename):

        A_gray = self.RGB2GRAY_A(filename)
        B_gray = self.RGB2GRAY_B(filename)
        h, w= A_gray.shape   # shape of image

        subt = np.zeros((h,w))    # 初始化矩陣以儲存灰階值
        subt = abs(A_gray - B_gray)
        subt = subt.astype("uint8")
        bytesPerline = w * 1
        #print A
        self.myqimage1 = QImage(A_gray, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q2_1.setPixmap(QPixmap.fromImage(self.myqimage1))
        #print B
        self.myqimage2 = QImage(B_gray, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q2_2.setPixmap(QPixmap.fromImage(self.myqimage2))
        #print abs(A - B)
        self.myqimage3 = QImage(subt, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q2_3.setPixmap(QPixmap.fromImage(self.myqimage3))
        return 
    
    ## Q3
    def Q3(self, filename):
        # print original image
        img_arr = self.RGB2GRAY_B(filename)
        h, w = img_arr.shape
        bytesPerline = w * 1
        self.myqimage = QImage(img_arr, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q3_1.setPixmap(QPixmap.fromImage(self.myqimage))

        # print histogram
        hist_image = self.histogram(filename)
        h, w = hist_image.shape
        bytesPerline = w * 1
        self.myqimage = QImage(hist_image, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q3_2.setPixmap(QPixmap.fromImage(self.myqimage))

    ## Q4
    def Q4(self, filename):
        # print original image
        img_arr = self.RGB2GRAY_B(filename)
        h, w = img_arr.shape
        bytesPerline = w * 1
        self.myqimage_Q4_1 = QImage(img_arr, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q4_1.setPixmap(QPixmap.fromImage(self.myqimage_Q4_1))

        # print binary image
        threshold = self.ui.verticalSlider.value()
        self.manual_binary(filename, threshold)
        binary_arr = self.manual_binary(filename, threshold)
        h, w = binary_arr.shape
        bytesPerline = w * 1
        self.myqimage_Q4_2 = QImage(binary_arr, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q4_2.setPixmap(QPixmap.fromImage(self.myqimage_Q4_2))
    
    # horizontalSlider改變時會更新label,顯示當前的threshold值
    def update_label_height_value(self, value):
        self.ui.label_height.setText(f'{value}')
        self.ui.label_height.adjustSize()   #會隨字數自動調整大小，避免顯示失敗

    # horizontalSlider改變時會更新label,顯示當前的threshold值
    def update_label_width_value(self, value):
        self.ui.label_width.setText(f'{value}')
        self.ui.label_width.adjustSize()

    ## Q5
    def Q5(self, filename):
        neigh_h = self.ui.horizontalSlider_h.value()
        neigh_w = self.ui.horizontalSlider_w.value()
        level = self.ui.spinBox.value()
        enlarge_img = self.nearest_neighbour(filename,neigh_h, neigh_w ,level)
        h, w = enlarge_img.shape
        bytesPerline = w * 1
        self.myqimage_Q5 = QImage(enlarge_img, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q5.setPixmap(QPixmap.fromImage(self.myqimage_Q5))
        return
    





    # verticalSlider改變時會更新label,顯示當前的threshold值
    def update_label_threshold_value(self, value):
        self.ui.label_threshold.setText(f'{value}')
        self.ui.label_threshold.adjustSize()
    
    ## Q6
    def Q6(self, filename):
        brightness = float(self.ui.lineEdit_Q6_1.text())    #記得轉成int才能當參數
        contrast = float(self.ui.lineEdit_Q6_2.text())    #記得轉成int才能當參數
        adjusted_image = self.adjust_brightness_contrast(filename, brightness, contrast)
        #print original image
        img_arr, h, w, d = self.load(filename)
        bytesPerline = w * d
        self.myqimage_Q6_1 = QImage(img_arr, w, h, bytesPerline, QImage.Format_RGB888)
        self.ui.label_Q6_1.setPixmap(QPixmap.fromImage(self.myqimage_Q6_1))
        # print adjusted_image
        self.myqimage_Q6_2 = QImage(adjusted_image, w, h, bytesPerline, QImage.Format_RGB888)
        self.ui.label_Q6_2.setPixmap(QPixmap.fromImage(self.myqimage_Q6_2))


    def Q7(self, filename):
        #print original image
        img_arr = self.RGB2GRAY_B(filename)
        h, w = img_arr.shape
        bytesPerline = w * 1
        self.myqimage_Q7_1 = QImage(img_arr, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q7_1.setPixmap(QPixmap.fromImage(self.myqimage_Q7_1))
        
        # print original histogram
        his_origin = self.histogram(filename)
        his_origin = cv2.resize(his_origin, (200,200))
        h, w = his_origin.shape
        bytesPerline = w * 1
        self.myqimage_Q7_3 = QImage(his_origin, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q7_3.setPixmap(QPixmap.fromImage(self.myqimage_Q7_3))

        # print equalized image
        equalized_image, his_equalized= self.histogram_equalization_gray(filename)
        h, w = equalized_image.shape
        bytesPerline = w * 1
        self.myqimage_Q7_2 = QImage(equalized_image, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q7_2.setPixmap(QPixmap.fromImage(self.myqimage_Q7_2))

        # print equalized histogram
        h, w = his_equalized.shape
        bytesPerline = w * 1
        self.myqimage_Q7_4 = QImage(his_equalized, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Q7_4.setPixmap(QPixmap.fromImage(self.myqimage_Q7_4))
    
    def setup_control(self):
    
        self.ui.pushButton_Q1.clicked.connect(lambda:self.Q1('Lenna.jpg') )
        self.ui.pushButton_Q2.clicked.connect(lambda: self.Q2('Lenna.jpg'))
        self.ui.pushButton_Q3.clicked.connect(lambda: self.Q3('Lenna.jpg'))
        # verticalSlider
        self.ui.verticalSlider.valueChanged.connect(self.update_label_threshold_value)
        self.ui.pushButton_Q4.clicked.connect(lambda: self.Q4('Lenna.jpg'))        
        # horizontalSlider
        self.ui.horizontalSlider_h.valueChanged.connect(self.update_label_height_value)
        self.ui.horizontalSlider_w.valueChanged.connect(self.update_label_width_value)
        self.ui.pushButton_Q5.clicked.connect(lambda: self.Q5('Lenna.jpg'))
        self.ui.pushButton_Q6.clicked.connect(lambda: self.Q6('Lenna.jpg'))
        self.ui.pushButton_Q7.clicked.connect(lambda: self.Q7('Lenna.jpg'))
        return

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())