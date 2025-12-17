import math
import pywt
import cv2 as cv
import numpy as np
from skimage import io
from skimage.color import label2rgb
from skimage.segmentation import slic, mark_boundaries

from PyQt5 import QtWidgets, QtGui, QtCore



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1286, 885)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1271, 871))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_Part1_Tra_input = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_Tra_input.setGeometry(QtCore.QRect(240, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_Tra_input.setFont(font)
        self.pushButton_Part1_Tra_input.setObjectName("pushButton_Part1_Tra_input")
        self.label_Part1_Tra_input = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_Tra_input.setGeometry(QtCore.QRect(90, 50, 430, 430))
        self.label_Part1_Tra_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_Tra_input.setText("")
        self.label_Part1_Tra_input.setObjectName("label_Part1_Tra_input")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(250, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_Part1_Tra_output = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_Tra_output.setGeometry(QtCore.QRect(680, 50, 430, 430))
        self.label_Part1_Tra_output.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_Tra_output.setText("")
        self.label_Part1_Tra_output.setObjectName("label_Part1_Tra_output")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(790, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.pushButton_Part1_Tra_generate = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_Tra_generate.setGeometry(QtCore.QRect(820, 660, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_Tra_generate.setFont(font)
        self.pushButton_Part1_Tra_generate.setObjectName("pushButton_Part1_Tra_generate")
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setGeometry(QtCore.QRect(760, 510, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.lineEdit_Part1_Tra_k = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_Part1_Tra_k.setGeometry(QtCore.QRect(960, 500, 51, 41))
        self.lineEdit_Part1_Tra_k.setObjectName("lineEdit_Part1_Tra_k")
        self.lineEdit_Part1_Tra_m = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_Part1_Tra_m.setGeometry(QtCore.QRect(960, 560, 51, 41))
        self.lineEdit_Part1_Tra_m.setObjectName("lineEdit_Part1_Tra_m")
        self.label_28 = QtWidgets.QLabel(self.tab_4)
        self.label_28.setGeometry(QtCore.QRect(760, 570, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab_4)
        self.label_29.setGeometry(QtCore.QRect(590, 570, 641, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_Part1_Wavy_generate = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Part1_Wavy_generate.setGeometry(QtCore.QRect(850, 600, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_Wavy_generate.setFont(font)
        self.pushButton_Part1_Wavy_generate.setObjectName("pushButton_Part1_Wavy_generate")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(250, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_Part1_Wavy_output = QtWidgets.QLabel(self.tab_3)
        self.label_Part1_Wavy_output.setGeometry(QtCore.QRect(680, 50, 430, 430))
        self.label_Part1_Wavy_output.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_Wavy_output.setText("")
        self.label_Part1_Wavy_output.setObjectName("label_Part1_Wavy_output")
        self.pushButton_Part1_Wavy_input = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Part1_Wavy_input.setGeometry(QtCore.QRect(240, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_Wavy_input.setFont(font)
        self.pushButton_Part1_Wavy_input.setObjectName("pushButton_Part1_Wavy_input")
        self.lineEdit_Part1_Wavy_A = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Part1_Wavy_A.setGeometry(QtCore.QRect(930, 500, 51, 41))
        self.lineEdit_Part1_Wavy_A.setObjectName("lineEdit_Part1_Wavy_A")
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(800, 510, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_Part1_Wavy_input = QtWidgets.QLabel(self.tab_3)
        self.label_Part1_Wavy_input.setGeometry(QtCore.QRect(90, 50, 430, 430))
        self.label_Part1_Wavy_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_Wavy_input.setText("")
        self.label_Part1_Wavy_input.setObjectName("label_Part1_Wavy_input")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(810, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(690, 560, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pushButton_Part1_Cir_generate = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_Part1_Cir_generate.setGeometry(QtCore.QRect(820, 650, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_Cir_generate.setFont(font)
        self.pushButton_Part1_Cir_generate.setObjectName("pushButton_Part1_Cir_generate")
        self.label_22 = QtWidgets.QLabel(self.tab_5)
        self.label_22.setGeometry(QtCore.QRect(250, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_Part1_Cir_output = QtWidgets.QLabel(self.tab_5)
        self.label_Part1_Cir_output.setGeometry(QtCore.QRect(680, 50, 430, 430))
        self.label_Part1_Cir_output.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_Cir_output.setText("")
        self.label_Part1_Cir_output.setObjectName("label_Part1_Cir_output")
        self.pushButton_Part1_Cir_input = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_Part1_Cir_input.setGeometry(QtCore.QRect(240, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_Cir_input.setFont(font)
        self.pushButton_Part1_Cir_input.setObjectName("pushButton_Part1_Cir_input")
        self.lineEdit_Part1_Cir_k = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_Part1_Cir_k.setGeometry(QtCore.QRect(960, 500, 51, 41))
        self.lineEdit_Part1_Cir_k.setObjectName("lineEdit_Part1_Cir_k")
        self.label_33 = QtWidgets.QLabel(self.tab_5)
        self.label_33.setGeometry(QtCore.QRect(760, 510, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_Part1_Cir_input = QtWidgets.QLabel(self.tab_5)
        self.label_Part1_Cir_input.setGeometry(QtCore.QRect(90, 50, 430, 430))
        self.label_Part1_Cir_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_Cir_input.setText("")
        self.label_Part1_Cir_input.setObjectName("label_Part1_Cir_input")
        self.label_23 = QtWidgets.QLabel(self.tab_5)
        self.label_23.setGeometry(QtCore.QRect(790, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(690, 570, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_Part2_generate = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_generate.setGeometry(QtCore.QRect(940, 640, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_generate.setFont(font)
        self.pushButton_Part2_generate.setObjectName("pushButton_Part2_generate")
        self.label_Part2_input1 = QtWidgets.QLabel(self.tab)
        self.label_Part2_input1.setGeometry(QtCore.QRect(10, 50, 351, 321))
        self.label_Part2_input1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_input1.setText("")
        self.label_Part2_input1.setObjectName("label_Part2_input1")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(120, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_Part2_output = QtWidgets.QLabel(self.tab)
        self.label_Part2_output.setGeometry(QtCore.QRect(780, 190, 430, 430))
        self.label_Part2_output.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_output.setText("")
        self.label_Part2_output.setObjectName("label_Part2_output")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(840, 160, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_Part2_input1 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_input1.setGeometry(QtCore.QRect(120, 380, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_input1.setFont(font)
        self.pushButton_Part2_input1.setObjectName("pushButton_Part2_input1")
        self.label_Part2_input2 = QtWidgets.QLabel(self.tab)
        self.label_Part2_input2.setGeometry(QtCore.QRect(370, 50, 341, 321))
        self.label_Part2_input2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_input2.setText("")
        self.label_Part2_input2.setObjectName("label_Part2_input2")
        self.pushButton_Part2_input2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_input2.setGeometry(QtCore.QRect(480, 380, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_input2.setFont(font)
        self.pushButton_Part2_input2.setObjectName("pushButton_Part2_input2")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(470, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_Part2_input3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_input3.setGeometry(QtCore.QRect(120, 790, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_input3.setFont(font)
        self.pushButton_Part2_input3.setObjectName("pushButton_Part2_input3")
        self.label_Part2_input3 = QtWidgets.QLabel(self.tab)
        self.label_Part2_input3.setGeometry(QtCore.QRect(10, 460, 351, 321))
        self.label_Part2_input3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_input3.setText("")
        self.label_Part2_input3.setObjectName("label_Part2_input3")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(120, 430, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_Part3_generate = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3_generate.setGeometry(QtCore.QRect(750, 570, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3_generate.setFont(font)
        self.pushButton_Part3_generate.setObjectName("pushButton_Part3_generate")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(260, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_Part3_input = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_input.setGeometry(QtCore.QRect(110, 50, 430, 430))
        self.label_Part3_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_input.setText("")
        self.label_Part3_input.setObjectName("label_Part3_input")
        self.label_Part3_output_2 = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_output_2.setGeometry(QtCore.QRect(590, 50, 430, 430))
        self.label_Part3_output_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_output_2.setText("")
        self.label_Part3_output_2.setObjectName("label_Part3_output_2")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(740, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_Part3_input = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3_input.setGeometry(QtCore.QRect(260, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3_input.setFont(font)
        self.pushButton_Part3_input.setObjectName("pushButton_Part3_input")
        self.lineEdit_Part3_n = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Part3_n.setGeometry(QtCore.QRect(860, 510, 51, 41))
        self.lineEdit_Part3_n.setObjectName("lineEdit_Part3_n")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(730, 520, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Part1_Tra_input.setText(_translate("Form", "Input Image"))
        self.label_15.setText(_translate("Form", "Original Image"))
        self.label_18.setText(_translate("Form", "Trapezoidal Transformation"))
        self.pushButton_Part1_Tra_generate.setText(_translate("Form", "Generate"))
        self.label_27.setText(_translate("Form", "Rate of shrink(width) = "))
        self.label_28.setText(_translate("Form", "Rate of shrink(height) = "))
        self.label_29.setText(_translate("Form", "* In the beginning, you can set this two coefficient by 0.5 and 0.5, respectively."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Part1 - Trapezoid"))
        self.pushButton_Part1_Wavy_generate.setText(_translate("Form", "Generate"))
        self.label_20.setText(_translate("Form", "Original Image"))
        self.pushButton_Part1_Wavy_input.setText(_translate("Form", "Input Image"))
        self.label_32.setText(_translate("Form", "Coefficient A = "))
        self.label_21.setText(_translate("Form", "Wavy Transformation"))
        self.label_30.setText(_translate("Form", "* In the beginning, you can set this coefficient by 20."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Part1 - Wavy"))
        self.pushButton_Part1_Cir_generate.setText(_translate("Form", "Generate"))
        self.label_22.setText(_translate("Form", "Original Image"))
        self.pushButton_Part1_Cir_input.setText(_translate("Form", "Input Image"))
        self.label_33.setText(_translate("Form", "Rate of shrink(width) = "))
        self.label_23.setText(_translate("Form", "Circular Transformation"))
        self.label_31.setText(_translate("Form", "* In the beginning, you can set this coefficient by 1."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Part1 - Circular"))
        self.pushButton_Part2_generate.setText(_translate("Form", "Generate"))
        self.label_11.setText(_translate("Form", "Original Image1"))
        self.label_12.setText(_translate("Form", "Superpixel-based Regional Segmentation"))
        self.pushButton_Part2_input1.setText(_translate("Form", "Input Image"))
        self.pushButton_Part2_input2.setText(_translate("Form", "Input Image"))
        self.label_24.setText(_translate("Form", " Original Image2"))
        self.pushButton_Part2_input3.setText(_translate("Form", "Input Image"))
        self.label_13.setText(_translate("Form", "Original Image3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Part2"))
        self.pushButton_Part3_generate.setText(_translate("Form", "generate"))
        self.label_8.setText(_translate("Form", "Original Image"))
        self.label_9.setText(_translate("Form", "Superpixel Image"))
        self.pushButton_Part3_input.setText(_translate("Form", "Input Image"))
        self.label_26.setText(_translate("Form", "n_segments    = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Part3"))




## -------------------------------------------------------controllor----------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()     #UI.py中class名稱
        self.ui.setupUi(self)
        self.setup_control()
        self.file_path_Part1_Trapezoidal = None
        self.file_path_Part1_Wavy = None
        self.file_path_Part1_Circular = None
        self.file_path_Part2_1 = None
        self.file_path_Part2_2 = None
        self.file_path_Part2_3 = None
        self.file_path_Part3 = None
## -------------------------------------------------------Part1 - Trapezoidal----------------------------------------------  
    # input image
    def button_clicked_input1_Trapezoidal(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part1_Trapezoidal = file_path
        print('path:', self.file_path_Part1_Trapezoidal)

        # display on frame of label
        img = cv.imread(self.file_path_Part1_Trapezoidal)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_Tra_input.setPixmap(pixmap)
        return self.file_path_Part1_Trapezoidal

    def Trapezoid(self, imgpath):
        k = float(self.ui.lineEdit_Part1_Tra_k.text())
        m = float(self.ui.lineEdit_Part1_Tra_m.text())
        trans_k = round(1 - k, 2)
        trans_m = round(1 - m, 2)  
        img = cv.imread(imgpath, 0)
        height, width = img.shape[0], img.shape[1]
        # 短邊的寬
        value = trans_k * height
        resize_gray = np.zeros([height, width]).astype(np.uint8)
        
        # height只縮一側
        distance = int( trans_m * height)
        for i in range(0, height - distance):
            temp = int(value - trans_k * (height - i)) 

            # wight縮兩側
            for j in range (temp, width - temp):
                # 每行非黑色區域的長度
                distance_w = int(width - temp) - int(temp + 0.5)
                distance_h = int(height - trans_m * height)
                # 縮小的倍率
                ratio_w = distance_w / width
                ratio_h = distance_h / height
                resize_gray[i][j] = img[int(i / ratio_h)][int((j - temp) / ratio_w)]
        return resize_gray

    # display Trapezoid
    def display_Part1_Trapezoidal_result(self, imagepath):
        
        img = self.Trapezoid(imagepath).astype(np.uint8)
        h, w = img.shape 
        bytesPerline = w * 1
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_Tra_output.setPixmap(pixmap)
## -------------------------------------------------------Part1 - Wavy----------------------------------------------
    # input image
    def button_clicked_input1_Wavy(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part1_Wavy = file_path
        print('path:', self.file_path_Part1_Wavy)

        # display on frame of label
        img = cv.imread(self.file_path_Part1_Wavy)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_Wavy_input.setPixmap(pixmap)
        return self.file_path_Part1_Wavy
    
    def Wavy(self, imgpath):
        A = int(self.ui.lineEdit_Part1_Wavy_A.text())
        img = cv.imread(imgpath, 0)
        height, width = img.shape[0], img.shape[1]
        resize_gray = np.zeros([height, width]).astype(np.uint8)

        for i in range(height):
            for j in range(width):
                offset_w = int(A * math.cos(2 * math.pi * i / 180))
                offset_h = int(A * math.sin(2 * math.pi * j / 180))
                add_offset_w = j + offset_w
                add_offset_h = i + offset_h
                if add_offset_w < width and add_offset_h < height and add_offset_w > 0 and add_offset_h > 0:
                    resize_gray[i][j] = img[(add_offset_h) % height][(add_offset_w) % width]
                else:
                    resize_gray[i][j] = 0
        return resize_gray
    
    # display Wavy
    def display_Part1_Wavy_result(self, imagepath):
        
        img = self.Wavy(imagepath).astype(np.uint8)
        h, w = img.shape 
        bytesPerline = w * 1
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_Wavy_output.setPixmap(pixmap)
## -------------------------------------------------------Part1 - Circular----------------------------------------------
    # input image
    def button_clicked_input1_Circular(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part1_Circular = file_path
        print('path:', self.file_path_Part1_Circular)

        # display on frame of label
        img = cv.imread(self.file_path_Part1_Circular)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_Cir_input.setPixmap(pixmap)
        return self.file_path_Part1_Circular
    
    def Circular(self, imgpath): 
        k = float(self.ui.lineEdit_Part1_Cir_k.text())
        img = cv.imread(imgpath, 0)   
        height, width = img.shape[0], img.shape[1]
        resize_gray = np.zeros([height, width]).astype(np.uint8)
        radius = height / 2
        for i in range(1, height):
            for j in range(1, width):
                temp = (radius ** 2 - (radius - i) ** 2) ** 0.5 * k
                b = int((j - radius) * radius / temp + radius)
                if (i >= 0) and (i < height) and (b >= 0) and (b < width):
                    resize_gray[i][j] = img[i][b]
                else:
                    resize_gray[i][j] = 0
        return resize_gray
    
    # display Circular
    def display_Part1_Circular_result(self, imagepath):
        
        img = self.Circular(imagepath).astype(np.uint8)
        h, w = img.shape 
        bytesPerline = w * 1
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_Cir_output.setPixmap(pixmap)
## -------------------------------------------------------Part2----------------------------------------------    
    # input image1
    def button_clicked_input2_1(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part2_1 = file_path
        print('path:', self.file_path_Part2_1)

        # display on frame of label
        img = cv.imread(self.file_path_Part2_1)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(351, 321, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_input1.setPixmap(pixmap)
        return self.file_path_Part2_1
    
    # input image2
    def button_clicked_input2_2(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part2_2 = file_path
        print('path:', self.file_path_Part2_2)

        # display on frame of label
        img = cv.imread(self.file_path_Part2_2)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(351, 321, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_input2.setPixmap(pixmap)
        return self.file_path_Part2_2
    
    # input image3
    def button_clicked_input2_3(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part2_3 = file_path
        print('path:', self.file_path_Part2_3)

        # display on frame of label
        img = cv.imread(self.file_path_Part2_3)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(351, 321, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_input3.setPixmap(pixmap)
        return self.file_path_Part2_3
    
    def Resize(self, imgpath, r = 1, c = 1):
        img = cv.imread(imgpath, 0)
        height, width = img.shape[0], img.shape[1]
        sr = height / r
        sc = width / c
        newimg = np.zeros([height, width], np.uint8)
        for i in range(r):
            for j in range(c):
                rf = i * sr
                cf = j * sc
                intr = int(rf)
                intc = int(cf)
                delr = rf - intr
                delc = cf - intc
                newimg[i, j] = img[intr - 1, intc - 1] * (1 - delr) * (1 - delc) + \
                img[intr, intc - 1] * delr * (1 - delc) + img[intr - 1, intc] * (1 - delr) * delc + \
                img[intr, intc] * delr * delc
        return newimg

    def Wavelet(self, imgpath1, imgpath2, imgpath3 = None):
        if imgpath3 is None:
            img1 = cv.imread(imgpath1, 0)
            img2 = cv.imread(imgpath2, 0)

            r1 = img1.shape[0]
            c1 = img1.shape[1]
            r2 = img2.shape[0]
            c2 = img2.shape[1]

            if r1!=r2 or c1!=c2:
                img2 = self.Resize(img2, r1, c1)
            tmp1 = pywt.dwt2(img1, 'haar')
            a1, (b1,c1,d1) = tmp1
            tmp2 = pywt.dwt2(img2, 'haar')
            a2, (b2,c2,d2) = tmp2
            a = (a1+a2)/2
            b = np.maximum(b1,b2)
            c = np.maximum(c1,c2)
            d = np.maximum(d1,d2)
            tmp = a, (b, c, d)
            img_new = pywt.idwt2(tmp, 'haar')

        else:
            img1 = cv.imread(imgpath1, 0)
            img2 = cv.imread(imgpath2, 0)
            img3 = cv.imread(imgpath3, 0)
            r1, c1 = img1.shape[0], img1.shape[1]
            r2, c2 = img2.shape[0], img2.shape[1]
            r3, c3 = img3.shape[0], img3.shape[1]

            if r1 != r2 or c1 != c2:
                img2 = self.Resize(img2, r1, c1)
            if r1 != r3 or c1 != c3:
                img3 = self.Resize(img3, r1, c1)
            tmp1 = pywt.dwt2(img1, 'haar')
            a1,(b1,c1,d1) = tmp1
            tmp2 = pywt.dwt2(img2, 'haar')
            a2, (b2, c2, d2) = tmp2
            tmp3 = pywt.dwt2(img3, 'haar')
            a3,(b3, c3, d3) = tmp3
            a = (a1 + a2 + a3) / 3
            b = np.maximum(b1, b2, b3)
            c = np.maximum(c1, c2, c3)
            d = np.maximum(d1, d2, d3)
            tmp = a, (b, c, d)
            img_new = pywt.idwt2(tmp, 'haar')
        return img_new
    
    # display Circular
    def display_Part2_result(self, imagepath1, imagepath2, imagepath3):
        
        img = self.Wavelet(imagepath1, imagepath2, imagepath3).astype(np.uint8)
        h, w = img.shape 
        bytesPerline = w * 1
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_output.setPixmap(pixmap)
## -------------------------------------------------------Part3----------------------------------------------    
# input image1
    def button_clicked_input3(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part3 = file_path
        print('path:', self.file_path_Part3)

        # display on frame of label
        img = cv.imread(self.file_path_Part3, cv.IMREAD_GRAYSCALE)
        img = img.astype(np.uint8)
        h, w = img.shape 
        bytesPerline = w * 1 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part3_input.setPixmap(pixmap)
        return self.file_path_Part3
    
    def slic_Seg(self, imagepath, n, com):
        img = io.imread(imagepath)
        segment = slic(img, n_segments = n, compactness = com)
        boundary_img = mark_boundaries(img, segment)
        segment_img = label2rgb(segment, img, kind = 'avg', bg_label = 0)
        return boundary_img, segment_img
    
    # display Circular
    def display_Part3_result(self, imagepath):
        n = int(self.ui.lineEdit_Part3_n.text())
        print(n)
        boundary_img, segment_img = self.slic_Seg(imagepath, n, 10)

        segment_img = segment_img.astype(np.uint8)
        h, w ,d = boundary_img.shape 
        bytesPerline = w * d

        qimg = QtGui.QImage(segment_img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part3_output_2.setPixmap(pixmap)


    
## -------------------------------------------------------controller----------------------------------------------     
    def setup_control(self):
        # Part 1
        self.ui.pushButton_Part1_Tra_input.clicked.connect(self.button_clicked_input1_Trapezoidal)
        self.ui.pushButton_Part1_Tra_generate.clicked.connect(lambda: self.display_Part1_Trapezoidal_result(self.file_path_Part1_Trapezoidal))
        self.ui.pushButton_Part1_Wavy_input.clicked.connect(self.button_clicked_input1_Wavy)
        self.ui.pushButton_Part1_Wavy_generate.clicked.connect(lambda: self.display_Part1_Wavy_result(self.file_path_Part1_Wavy))
        self.ui.pushButton_Part1_Cir_input.clicked.connect(self.button_clicked_input1_Circular)
        self.ui.pushButton_Part1_Cir_generate.clicked.connect(lambda: self.display_Part1_Circular_result(self.file_path_Part1_Circular))
        # Part 2
        self.ui.pushButton_Part2_input1.clicked.connect(self.button_clicked_input2_1)
        self.ui.pushButton_Part2_input2.clicked.connect(self.button_clicked_input2_2)
        self.ui.pushButton_Part2_input3.clicked.connect(self.button_clicked_input2_3)
        self.ui.pushButton_Part2_generate.clicked.connect(lambda: self.display_Part2_result(self.file_path_Part2_1, self.file_path_Part2_2, self.file_path_Part2_3))
        # Part 3
        self.ui.pushButton_Part3_input.clicked.connect(self.button_clicked_input3)
        self.ui.pushButton_Part3_generate.clicked.connect(lambda: self.display_Part3_result(self.file_path_Part3))
        return

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())