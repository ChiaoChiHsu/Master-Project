import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QColor

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1450, 973)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1441, 961))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_Part2_size = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_size.setGeometry(QtCore.QRect(370, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_size.setFont(font)
        self.pushButton_Part2_size.setObjectName("pushButton_Part2_size")
        self.label_Part2_original = QtWidgets.QLabel(self.tab)
        self.label_Part2_original.setGeometry(QtCore.QRect(510, 140, 441, 441))
        self.label_Part2_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_original.setText("")
        self.label_Part2_original.setObjectName("label_Part2_original")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 340, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_00 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_00.setGeometry(QtCore.QRect(200, 300, 41, 31))
        self.lineEdit_00.setObjectName("lineEdit_00")
        self.lineEdit_01 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_01.setGeometry(QtCore.QRect(200, 340, 41, 31))
        self.lineEdit_01.setObjectName("lineEdit_01")
        self.lineEdit_02 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_02.setGeometry(QtCore.QRect(200, 380, 41, 31))
        self.lineEdit_02.setObjectName("lineEdit_02")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(250, 300, 41, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(250, 340, 41, 31))
        self.lineEdit_11.setObjectName("lineEdit_12")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(250, 380, 41, 31))
        self.lineEdit_12.setObjectName("lineEdit_13")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_20.setGeometry(QtCore.QRect(300, 300, 41, 31))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_21.setGeometry(QtCore.QRect(300, 340, 41, 31))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_22.setGeometry(QtCore.QRect(300, 380, 41, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.pushButton_Part2_coei = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_coei.setGeometry(QtCore.QRect(370, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_coei.setFont(font)
        self.pushButton_Part2_coei.setObjectName("pushButton_Part2_coei")
        self.comboBox_Part2_kernel = QtWidgets.QComboBox(self.tab)
        self.comboBox_Part2_kernel.setGeometry(QtCore.QRect(80, 480, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part2_kernel.setFont(font)
        self.comboBox_Part2_kernel.setObjectName("comboBox_Part2_kernel")
        self.comboBox_Part2_kernel.addItem("")
        self.comboBox_Part2_kernel.addItem("")
        self.comboBox_Part2_kernel.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 480, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_Part2_kernel = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_kernel.setGeometry(QtCore.QRect(370, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_kernel.setFont(font)
        self.pushButton_Part2_kernel.setObjectName("pushButton_Part2_kernel")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(700, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_Part2_result = QtWidgets.QLabel(self.tab)
        self.label_Part2_result.setGeometry(QtCore.QRect(970, 140, 441, 441))
        self.label_Part2_result.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_result.setText("")
        self.label_Part2_result.setObjectName("label_Part2_result")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(1170, 110, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_input_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_input_2.setGeometry(QtCore.QRect(10, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_input_2.setFont(font)
        self.pushButton_input_2.setObjectName("pushButton_input_2")
        self.lineEdit_size1 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_size1.setGeometry(QtCore.QRect(180, 190, 41, 31))
        self.lineEdit_size1.setObjectName("lineEdit_size1")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(230, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(250, 190, 41, 31))
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_Part3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3.setGeometry(QtCore.QRect(10, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3.setFont(font)
        self.pushButton_Part3.setObjectName("pushButton_Part3")
        self.label_Part3_sobel = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_sobel.setGeometry(QtCore.QRect(620, 490, 400, 400))
        self.label_Part3_sobel.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_sobel.setText("")
        self.label_Part3_sobel.setObjectName("label_Part3_sobel")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(800, 460, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(340, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_Part3_original = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_original.setGeometry(QtCore.QRect(170, 40, 400, 400))
        self.label_Part3_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_original.setText("")
        self.label_Part3_original.setObjectName("label_Part3_original")
        self.label_Part3_zero = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_zero.setGeometry(QtCore.QRect(620, 40, 400, 400))
        self.label_Part3_zero.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_zero.setText("")
        self.label_Part3_zero.setObjectName("label_Part3_zero")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(640, 0, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(310, 460, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_Part3_mrr = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_mrr.setGeometry(QtCore.QRect(170, 490, 400, 400))
        self.label_Part3_mrr.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_mrr.setText("")
        self.label_Part3_mrr.setObjectName("label_Part3_mrr")
        self.pushButton_input_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_input_3.setGeometry(QtCore.QRect(10, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_input_3.setFont(font)
        self.pushButton_input_3.setObjectName("pushButton_input_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_Part4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Part4.setGeometry(QtCore.QRect(720, 30, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part4.setFont(font)
        self.pushButton_Part4.setObjectName("pushButton_Part4")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(590, 110, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_Part4_local = QtWidgets.QLabel(self.tab_3)
        self.label_Part4_local.setGeometry(QtCore.QRect(480, 140, 441, 441))
        self.label_Part4_local.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part4_local.setText("")
        self.label_Part4_local.setObjectName("label_Part4_local")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(1040, 110, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_Part4_histogram = QtWidgets.QLabel(self.tab_3)
        self.label_Part4_histogram.setGeometry(QtCore.QRect(950, 140, 441, 441))
        self.label_Part4_histogram.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part4_histogram.setText("")
        self.label_Part4_histogram.setObjectName("label_Part4_histogram")
        self.label_Part4_original = QtWidgets.QLabel(self.tab_3)
        self.label_Part4_original.setGeometry(QtCore.QRect(10, 140, 441, 441))
        self.label_Part4_original.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part4_original.setText("")
        self.label_Part4_original.setObjectName("label_Part4_original")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(190, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_Part4_size = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_Part4_size.setGeometry(QtCore.QRect(440, 30, 61, 41))
        self.lineEdit_Part4_size.setPlaceholderText("")
        self.lineEdit_Part4_size.setObjectName("lineEdit_Part4_size")

        self.label_100 = QtWidgets.QLabel(self.tab_3)
        self.label_100.setGeometry(QtCore.QRect(510, 40, 31, 31))
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")

        self.label_101 = QtWidgets.QLabel(self.tab_3)
        self.label_101.setGeometry(QtCore.QRect(530, 30, 61, 41))
        self.label_101.setFrameShape(QtWidgets.QFrame.Box)
        self.label_101.setText("")
        self.label_101.setObjectName("label_101")

        self.pushButton_input_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_input_4.setGeometry(QtCore.QRect(70, 30, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_input_4.setFont(font)
        self.pushButton_input_4.setObjectName("pushButton_input_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 700, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Part2_size.setText(_translate("Form", "generate"))
        self.label.setText(_translate("Form", "box kernel size ="))
        self.label_4.setText(_translate("Form", "3x3 kernel coeiffient:"))
        self.pushButton_Part2_coei.setText(_translate("Form", "generate"))
        self.comboBox_Part2_kernel.setItemText(0, _translate("Form", " Lowpass Gaussian Filter Kernels"))
        self.comboBox_Part2_kernel.setItemText(1, _translate("Form", "Sharpening (Highpass) Spatial Filters"))
        self.label_5.setText(_translate("Form", "kernel:"))
        self.pushButton_Part2_kernel.setText(_translate("Form", "generate"))
        self.label_11.setText(_translate("Form", "original"))
        self.label_12.setText(_translate("Form", "result"))
        self.pushButton_input_2.setText(_translate("Form", "input image"))
        self.label_6.setText(_translate("Form", "*"))
        self.label_100.setText(_translate("Form", "*"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Part2"))
        self.pushButton_Part3.setText(_translate("Form", "generate"))
        self.label_26.setText(_translate("Form", "sobel"))
        self.label_8.setText(_translate("Form", "original"))
        self.label_9.setText(_translate("Form", " Marr-Hildreth and zero-crossing threshold"))
        self.label_14.setText(_translate("Form", " Marr-Hildreth"))
        self.pushButton_input_3.setText(_translate("Form", "input image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Part3"))
        self.pushButton_Part4.setText(_translate("Form", "generate"))
        self.label_10.setText(_translate("Form", "local enhancement method"))
        self.label_22.setText(_translate("Form", " histogram equalization method"))
        self.label_13.setText(_translate("Form", "original"))
        self.label_2.setText(_translate("Form", " region size, Sxy = "))
        self.pushButton_input_4.setText(_translate("Form", "input image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Part4"))
        self.label_3.setText(_translate("Form", "**kernel size較大和使用彩色影像需要較長之運算時間，請稍等謝謝**"))



## -------------------------------------------------------controllor----------------------------------------------
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()     #UI.py中class名稱
        self.ui.setupUi(self)
        self.setup_control()
        self.file_path = None

    
## -------------------------------------------------------Part2----------------------------------------------    
    # input and display image Part2
    def button_clicked_2(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter='JPEG (*.jpg)') # 讀取圖片
        self.file_path = file_path
        print('path:',self.file_path)
        # display original image in Part2-Part4
        image = cv2.imread(self.file_path)

        # 檢測是否為灰階
        is_grayscale = (image[:, :, 0] == image[:, :, 1]).all() and (
            image[:, :, 1] == image[:, :, 2]
        ).all()
        if is_grayscale:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            # display origianl image
            image = cv2.resize(img, (441, 441)) 
            h, w = image.shape       
            bytesPerline = w * 1
            image = image.astype(np.uint8)
            self.image = QImage(image, w, h, bytesPerline, QImage.Format_Grayscale8)
            self.ui.label_Part2_original.setPixmap(QPixmap.fromImage(self.image))
        else:
            image_RGB = cv2.imread(file_path)
            image_RGB = image_RGB[:, :,::-1]
            image_RGB = cv2.resize(image_RGB, (441, 441))
            h, w, d = image_RGB.shape        
            bytesPerline = w * d
            image_RGB = image_RGB.astype(np.uint8)
            self.image_RGB = QImage(image_RGB, w, h, bytesPerline, QImage.Format_RGB888)
            self.ui.label_Part2_original.setPixmap(QPixmap.fromImage(self.image_RGB))
        return self.file_path
    
    # box kernel
    def make_box_kernel(self,kernel_size):
        box_kernel = np.zeros((kernel_size, kernel_size), dtype=np.float32)
        for x in range(0, kernel_size):
            for y in range(0, kernel_size):
                box_kernel[x][y] = 1 / (kernel_size * kernel_size)
        return box_kernel

    # kernel_rotate
    def kernel_rotate(self,kernel):
        new_kernel = np.zeros((kernel.shape[0], kernel.shape[1]), dtype=np.float16)
        for i in range(0, kernel.shape[0]):
            for j in range(0, kernel.shape[1]):
                new_kernel[i][j] = float(
                    kernel[kernel.shape[0] - 1 - i][kernel.shape[1] - 1 - j]
                )
        return new_kernel

    # 若輸入圖像為灰階圖則執行此函數計算卷積
    def gray_operation(self,image, kernel):
        image_h, image_w = image.shape
        kernel = self.kernel_rotate(kernel)
        # padding
        padding_size = int(kernel.shape[0] / 2)
        padded_image = np.pad(
            image,
            ((padding_size, padding_size), (padding_size, padding_size)),
            mode="constant",
        )
        # operation
        convolved_image = np.zeros((image_h, image_w), dtype=np.float32)
        for x in range(image_h):
            for y in range(image_w):
                conv_sum = 0.0
                for kx in range(kernel.shape[0]):
                    for ky in range(kernel.shape[1]):
                        conv_sum += padded_image[x + kx, y + ky] * kernel[kx, ky]
                convolved_image[x, y] = int(conv_sum)
        return convolved_image

    # 若輸入圖像為RGB圖則執行此函數計算卷積
    def RGB_operation(self,image, kernel):
        image_h, image_w ,d= image.shape
        # padding
        padding_size = int(kernel.shape[0] / 2)
        new_height = image_h + 2 * padding_size
        new_width = image_w + 2 * padding_size
        # zero padding
        padded_image = np.zeros((new_height, new_width, d), dtype=np.uint8)

        # 將原始圖像放在新圖像的中央
        padded_image[padding_size:padding_size + image_h, padding_size:padding_size + image_w, :] = image

        # operation
        convolved_image = np.zeros((image_h, image_w, d), dtype=np.float16)
        for channel in range(0,d):
            for x in range(image_h):
                for y in range(image_w):
                    conv_sum = 0.0
                    for kx in range(kernel.shape[0]):
                        for ky in range(kernel.shape[1]):
                            conv_sum += padded_image[x + kx, y + ky,channel] * kernel[kx, ky]
                    convolved_image[x, y,channel] = int(conv_sum)
        return convolved_image

    #  kernel size generate
    def Part2_size(self,filename):
        kernel_size = self.ui.lineEdit_size1.text()
        print('kernel_size=',kernel_size)
        self.ui.label_7.setText(kernel_size)
    
        #load image
        image = cv2.imread(self.file_path)

        # 若kernel_size為偶數自動加一
        kernel_size =  int(kernel_size)
        if kernel_size % 2 == 0 :
            kernel_size = kernel_size + 1
        box_kernel = self.make_box_kernel(kernel_size)
        
        # 檢測是否為灰階
        is_grayscale = (image[:, :, 0] == image[:, :, 1]).all() and (
            image[:, :, 1] == image[:, :, 2]
        ).all()
        if is_grayscale:
            # print("灰度圖像")
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            smooth_image = self.gray_operation(image, box_kernel)   
            smooth_image = np.clip(smooth_image, 0, 255)
            smooth_image = cv2.resize(smooth_image, (441, 441)) 
            smooth_image = smooth_image.astype(np.uint8)
            h, w = smooth_image.shape       
            bytesPerline = w * 1
            self.smooth_image = QImage(smooth_image, w, h, bytesPerline, QImage.Format_Grayscale8)
            self.ui.label_Part2_result.setPixmap(QPixmap.fromImage(self.smooth_image))    
        else:
            # print("彩色圖像")
            image_RGB = cv2.imread(self.file_path)
            image_RGB = image_RGB[:, :,::-1]
            smooth_image = self.RGB_operation(image_RGB, box_kernel)
            smooth_image = np.clip(smooth_image, 0, 255)
            smooth_image = cv2.resize(smooth_image, (441, 441)) 
            smooth_image = smooth_image.astype(np.uint8)
            h, w ,d = smooth_image.shape       
            bytesPerline = w * d
            self.smooth_image = QImage(smooth_image, w, h, bytesPerline, QImage.Format_RGB888)
            self.ui.label_Part2_result.setPixmap(QPixmap.fromImage(self.smooth_image))

    #  3x3 kernel 自定義係數 generate
    def Part2_coei(self,filename):
        kernel = np.array([[self.ui.lineEdit_00.text(), self.ui.lineEdit_10.text(), self.ui.lineEdit_20.text()],
                          [self.ui.lineEdit_01.text(), self.ui.lineEdit_11.text(), self.ui.lineEdit_21.text()],
                          [self.ui.lineEdit_02.text(), self.ui.lineEdit_12.text(), self.ui.lineEdit_22.text()]]) 
        #load image
        image = cv2.imread(self.file_path)
        
        # 檢測是否為灰階
        is_grayscale = (image[:, :, 0] == image[:, :, 1]).all() and (
            image[:, :, 1] == image[:, :, 2]
        ).all()
        if is_grayscale:
            # print("灰度圖像")
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            smooth_image = self.gray_operation(image, kernel)   
            smooth_image = np.clip(smooth_image, 0, 255)
            smooth_image = cv2.resize(smooth_image, (441, 441)) 
            smooth_image = smooth_image.astype(np.uint8)
            h, w = smooth_image.shape       
            bytesPerline = w * 1
            self.smooth_image = QImage(smooth_image, w, h, bytesPerline, QImage.Format_Grayscale8)
            self.ui.label_Part2_result.setPixmap(QPixmap.fromImage(self.smooth_image))    
        else:
            # print("彩色圖像")
            image_RGB = cv2.imread(self.file_path)
            image_RGB = image_RGB[:, :,::-1]
            smooth_image = self.RGB_operation(image_RGB,kernel)
            smooth_image = np.clip(smooth_image, 0, 255)
            smooth_image = cv2.resize(smooth_image, (441, 441)) 
            smooth_image = smooth_image.astype(np.uint8)
            h, w ,d = smooth_image.shape       
            bytesPerline = w * d
            self.smooth_image = QImage(smooth_image, w, h, bytesPerline, QImage.Format_RGB888)
            self.ui.label_Part2_result.setPixmap(QPixmap.fromImage(self.smooth_image))
        
        return image, smooth_image
    
    # 選擇不同kernel generate
    def Part2_kernel(self,filename):
        lowpass_kernel = np.array([[0.3679, 0.6065, 0.3679],
                                   [0.6065, 1, 0.6065],
                                   [0.3679, 0.6065, 0.3679]])
        highpass_kernel = np.array([[0, 1, 0],
                                   [1, -4, 1],
                                   [0, 1, 0]])

        index = self.ui.comboBox_Part2_kernel.currentIndex()
        if index == 0:
            kernel = lowpass_kernel
        elif index == 1:
            kernel = highpass_kernel
        #load image
        image = cv2.imread(self.file_path)
        
        # 檢測是否為灰階
        is_grayscale = (image[:, :, 0] == image[:, :, 1]).all() and (
            image[:, :, 1] == image[:, :, 2]
        ).all()
        if is_grayscale:
            # print("灰度圖像")
            image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            smooth_image = self.gray_operation(image, kernel)   
            smooth_image = np.clip(smooth_image, 0, 255)
            smooth_image = cv2.resize(smooth_image, (441, 441)) 
            smooth_image = smooth_image.astype(np.uint8)
            h, w = smooth_image.shape       
            bytesPerline = w * 1
            self.smooth_image = QImage(smooth_image, w, h, bytesPerline, QImage.Format_Grayscale8)
            self.ui.label_Part2_result.setPixmap(QPixmap.fromImage(self.smooth_image))    
        else:
            # print("彩色圖像")
            image_RGB = cv2.imread(self.file_path)
            image_RGB = image_RGB[:, :,::-1]
            smooth_image = self.RGB_operation(image_RGB,kernel)
            smooth_image = np.clip(smooth_image, 0, 255)
            smooth_image = cv2.resize(smooth_image, (441, 441)) 
            smooth_image = smooth_image.astype(np.uint8)
            h, w ,d = smooth_image.shape       
            bytesPerline = w * d
            self.smooth_image = QImage(smooth_image, w, h, bytesPerline, QImage.Format_RGB888)
            self.ui.label_Part2_result.setPixmap(QPixmap.fromImage(self.smooth_image))
        
        return image, smooth_image
    
## -------------------------------------------------------Part3----------------------------------------------    
    # input and display image Part3
    def button_clicked_3(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter='JPEG (*.jpg)') # 讀取圖片
        self.file_path = file_path
        print('path:',self.file_path)
        # display original image in Part2-Part4
        image = cv2.imread(self.file_path)

        # 檢測是否為灰階
        is_grayscale = (image[:, :, 0] == image[:, :, 1]).all() and (
            image[:, :, 1] == image[:, :, 2]
        ).all()
        if is_grayscale:
            img = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
            # display origianl image
            image = cv2.resize(img, (400, 400)) 
            h, w = image.shape         # 取得圖片的高、寬、通道數
            bytesPerline = w * 1
            image = image.astype(np.uint8)
            self.image = QImage(image, w, h, bytesPerline, QImage.Format_Grayscale8)
            self.ui.label_Part3_original.setPixmap(QPixmap.fromImage(self.image))
        else:
            image_RGB = cv2.imread(self.file_path)
            image_RGB = image_RGB[:, :,::-1]
            image_RGB = cv2.resize(image_RGB, (400, 400)) 
            h, w, d = image_RGB.shape         # 取得圖片的高、寬、通道數
            bytesPerline = w * d
            image_RGB = image_RGB.astype(np.uint8)
            self.image_RGB = QImage(image_RGB, w, h, bytesPerline, QImage.Format_RGB888)
            self.ui.label_Part3_original.setPixmap(QPixmap.fromImage(self.image_RGB))

    # Part3 generate
    def Part3(self,filename):
        # gaussian kernel
        gaussian_kernel = np.array([[1, 2, 1],
                                    [2, 4, 2],
                                    [1, 2, 1]]) / 16

        laplacian_kernel = np.array([[1, 1, 1],
                                    [1, -8, 1],
                                    [1, 1, 1]])

        # Load an image
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        # LOG
        smooth_image = self.gray_operation(image, gaussian_kernel)
        laplacian_image = self.gray_operation(smooth_image, laplacian_kernel)
        # Detect zero-crossings
        zero_crossings = np.zeros(laplacian_image.shape, dtype=np.uint8)
        for i in range(1, laplacian_image.shape[0] - 1):
            for j in range(1, laplacian_image.shape[1] - 1):
                if (
                    laplacian_image[i, j] * laplacian_image[i + 1, j] < 0
                    or laplacian_image[i, j] * laplacian_image[i - 1, j] < 0
                    or laplacian_image[i, j] * laplacian_image[i, j + 1] < 0
                    or laplacian_image[i, j] * laplacian_image[i, j - 1] < 0
                ):
                    zero_crossings[i, j] = 255
                else:
                    zero_crossings[i, j] = 0

        zero_crossings = np.clip(zero_crossings, 0, 255)
        # laplacian_image clip
        laplacian_image = np.clip(laplacian_image, 0, 255)

        # sobel
        sobelx = np.array([[ -1, 0, 1 ],[ -2, 0, 2 ],[ -1, 0,1 ]])
        sobely = np.array([[ -1, -2, -1 ],[ 0, 0, 0 ],[ 1, 2, 1 ]])
        sobelx_image = self.gray_operation(image, sobelx)
        sobely_image = self.gray_operation(image, sobely)
        sobel = np.sqrt(sobelx_image**2 + sobely_image**2)

        # display  Marr-Hildreth
        laplacian_image = cv2.resize(laplacian_image, (441, 441)) 
        laplacian_image = laplacian_image.astype(np.uint8)
        h, w = laplacian_image.shape       
        bytesPerline = w * 1
        self.laplacian_image = QImage(laplacian_image, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Part3_mrr.setPixmap(QPixmap.fromImage(self.laplacian_image))    

        # display zero crossing
        zero_crossings = cv2.resize(zero_crossings, (441, 441)) 
        zero_crossings = zero_crossings.astype(np.uint8)
        self.zero_crossings = QImage(zero_crossings, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Part3_zero.setPixmap(QPixmap.fromImage(self.zero_crossings)) 

        # display sobel
        sobel = cv2.resize(sobel, (441, 441)) 
        sobel = sobel.astype(np.uint8)
        self.sobel = QImage(sobel, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Part3_sobel.setPixmap(QPixmap.fromImage(self.sobel)) 


## -------------------------------------------------------Part4----------------------------------------------  
    # input image Part4
    def button_clicked_4(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter='JPEG (*.jpg)') # 讀取圖片
        self.file_path = file_path
        print('path:',self.file_path)

        # display original image in Part2-Part4        
        img = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(img, (441, 441)) 
        h, w = image.shape         # 取得圖片的高、寬、通道數
        bytesPerline = w * 1
        image = image.astype(np.uint8)
        self.image = QImage(image, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Part4_original.setPixmap(QPixmap.fromImage(self.image))

    # histogram_equalization
    def histogram_equalization_gray(self,filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
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
        mapping_table = (cumulative_histogram - cumulative_histogram.min()
                         ) * 255 / (cumulative_histogram.max() - cumulative_histogram.min())
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

        # display
        print("histogram_equalized : ",equalized_image )
        equalized_image = cv2.resize(equalized_image, (441, 441)) 
        h, w = equalized_image.shape   
        bytesPerline = w * 1
        equalized_image = equalized_image.astype(np.uint8)
        self.equalized_image= QImage(equalized_image, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Part4_histogram.setPixmap(QPixmap.fromImage(self.equalized_image))
    
    # mirror_padding
    def mirror_padding(self,image, kernel_size):
        padding_size = int(kernel_size/2)
        h, w = image.shape
        padded_image = np.zeros((h + 2 * padding_size, w + 2 * padding_size), dtype=np.uint8)

        # Copy the original image to the center of the padded image
        padded_image[padding_size:padding_size + h, padding_size:padding_size + w] = image

        # Mirror padding for the top and bottom rows
        for i in range(padding_size):
            padded_image[i, padding_size:padding_size + w] = image[padding_size - i, :]

        for i in range(padding_size):
            padded_image[h + 2 * padding_size - i - 1, padding_size:padding_size + w] = image[h - i - 1, :]

        # Mirror padding for the left and right columns
        for i in range(padding_size):
            padded_image[padding_size:padding_size + h, i] = padded_image[padding_size:padding_size + h, padding_size - i]

        for i in range(padding_size):
            padded_image[padding_size:padding_size + h, w + 2 * padding_size - i - 1] = padded_image[padding_size:padding_size + h, w - i - 1]
        return padded_image
    
    # enhanced image
    def local_enhancement(self, filename):
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        kernel_size = self.ui.lineEdit_Part4_size.text()
        self.ui.label_101.setText(kernel_size)
        # 若kernel_size為偶數自動加一
        kernel_size =  int(kernel_size)
        if kernel_size % 2 == 0 :
            kernel_size = kernel_size + 1
        k0 = 0 
        k1 = 0.1
        k2 = 0 
        k3 = 0.1
        # C = 22.8  # for image 4-1.jpg
        C = 30  #image 4-2.jpg

        # padding
        pad_image = self.mirror_padding(image, kernel_size)
        # Calculate the average image intensity (global mean)
        global_mean = np.mean(image)
        # Calculate the global standard deviation of the image
        standard_deviation = np.std(image)

        image_h, image_w = image.shape
        
        enhance_image = np.zeros((image_h, image_w), dtype = np.uint16)
        # calculate g(x,y)
        for x in range(0, image_h):     # kernel掃描pad_image，kernel的左上角位置從pad_image的(0,0)到(image_h, image_w)
            for y in range(0, image_w):
                conv_sum = 0        # conv_sum儲存kernel覆蓋區域的影像灰階總和
                mask_mean = 0       # mask_mean儲存kernel覆蓋區域的影像灰階平均
                # kernel
                kernel_tmp = np.ones((kernel_size, kernel_size))       # 暫存kernel覆蓋區域的影像灰階

                # 計算kernel覆蓋區域的影像灰階平均、標準差
                for kx in range(0, kernel_size):
                    for ky in range(0, kernel_size):
                        # 把kernel覆蓋的image灰階值暫時存入kernel_tmp
                        kernel_tmp[kx][ky] = pad_image[x + kx][y + ky]
                        conv_sum = conv_sum + pad_image[x + kx][y + ky]
                mask_mean = conv_sum/(kernel_size**2)
                mask_standard_deviation = np.std(kernel_tmp)

                # 定義enhance_image
                if mask_mean >= (k0 * global_mean) and \
                    mask_mean <= (k1 * global_mean) and \
                        mask_standard_deviation >= (k2 * standard_deviation) and \
                            mask_standard_deviation <= (k2 * standard_deviation):
                    enhance_image[x][y] = C*image[x][y]
                else:
                    enhance_image[x][y] = image[x][y]
        enhance_image = np.clip(enhance_image, 0, 255)

        # display
        enhance_image = cv2.resize(enhance_image, (441, 441)) 
        enhance_image = enhance_image.astype(np.uint8)
        h, w = enhance_image.shape   
        bytesPerline = w * 1
        self.enhance_image = QImage(enhance_image, w, h, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_Part4_local.setPixmap(QPixmap.fromImage(self.enhance_image))
    
    def setup_control(self):
        self.ui.pushButton_input_2.clicked.connect(self.button_clicked_2)
        self.ui.pushButton_input_3.clicked.connect(self.button_clicked_3)
        self.ui.pushButton_input_4.clicked.connect(self.button_clicked_4)
        self.ui.pushButton_Part2_size.clicked.connect(lambda: self.Part2_size(self.file_path))
        self.ui.pushButton_Part2_coei.clicked.connect(lambda: self.Part2_coei(self.file_path))
        self.ui.pushButton_Part2_kernel.clicked.connect(lambda: self.Part2_kernel(self.file_path))
        self.ui.pushButton_Part3.clicked.connect(lambda: self.Part3(self.file_path))
        self.ui.pushButton_Part4.clicked.connect(lambda: self.local_enhancement(self.file_path))
        self.ui.pushButton_Part4.clicked.connect(lambda: self.histogram_equalization_gray(self.file_path))

        return

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())