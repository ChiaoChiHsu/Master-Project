import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap, QColor

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(973, 830)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 1441, 951))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_Part1_input = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_input.setGeometry(QtCore.QRect(160, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_input.setFont(font)
        self.pushButton_Part1_input.setObjectName("pushButton_Part1_input")
        self.label_Part1_input = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_input.setGeometry(QtCore.QRect(10, 50, 430, 430))
        self.label_Part1_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_input.setText("")
        self.label_Part1_input.setObjectName("label_Part1_input")
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setGeometry(QtCore.QRect(170, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_Part1_result = QtWidgets.QLabel(self.tab_4)
        self.label_Part1_result.setGeometry(QtCore.QRect(470, 50, 430, 430))
        self.label_Part1_result.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part1_result.setText("")
        self.label_Part1_result.setObjectName("label_Part1_result")
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setGeometry(QtCore.QRect(590, 20, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.pushButton_Part1_generate = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Part1_generate.setGeometry(QtCore.QRect(630, 570, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part1_generate.setFont(font)
        self.pushButton_Part1_generate.setObjectName("pushButton_Part1_generate")
        self.comboBox_Part1 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_Part1.setGeometry(QtCore.QRect(690, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part1.setFont(font)
        self.comboBox_Part1.setObjectName("comboBox_Part1")
        self.comboBox_Part1.addItem("")
        self.comboBox_Part1.addItem("")
        self.comboBox_Part1.addItem("")
        self.comboBox_Part1.addItem("")
        self.comboBox_Part1.addItem("")
        self.comboBox_Part1.addItem("")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(570, 510, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton_Part2_generate = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_generate.setGeometry(QtCore.QRect(650, 610, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_generate.setFont(font)
        self.pushButton_Part2_generate.setObjectName("pushButton_Part2_generate")
        self.label_Part2_input = QtWidgets.QLabel(self.tab)
        self.label_Part2_input.setGeometry(QtCore.QRect(10, 50, 430, 430))
        self.label_Part2_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_input.setText("")
        self.label_Part2_input.setObjectName("label_Part2_input")
        self.comboBox_Part2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_Part2.setGeometry(QtCore.QRect(700, 550, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_Part2.setFont(font)
        self.comboBox_Part2.setObjectName("comboBox_Part2")
        self.comboBox_Part2.addItem("")
        self.comboBox_Part2.addItem("")
        self.comboBox_Part2.addItem("")
        self.comboBox_Part2.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(130, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_Part2_result = QtWidgets.QLabel(self.tab)
        self.label_Part2_result.setGeometry(QtCore.QRect(470, 50, 430, 430))
        self.label_Part2_result.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part2_result.setText("")
        self.label_Part2_result.setObjectName("label_Part2_result")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(620, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.pushButton_Part2_input = QtWidgets.QPushButton(self.tab)
        self.pushButton_Part2_input.setGeometry(QtCore.QRect(160, 550, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part2_input.setFont(font)
        self.pushButton_Part2_input.setObjectName("pushButton_Part2_input")
        self.label_Part2_mode = QtWidgets.QLabel(self.tab)
        self.label_Part2_mode.setGeometry(QtCore.QRect(620, 560, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_Part2_mode.setFont(font)
        self.label_Part2_mode.setObjectName("label_Part2_mode")
        self.label_Part2_bar_gray = QtWidgets.QLabel(self.tab)
        self.label_Part2_bar_gray.setGeometry(QtCore.QRect(10, 500, 431, 31))
        self.label_Part2_bar_gray.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Part2_bar_gray.setText("")
        self.label_Part2_bar_gray.setObjectName("label_Part2_bar_gray")
        self.label_Part2_bar_result = QtWidgets.QLabel(self.tab)
        self.label_Part2_bar_result.setGeometry(QtCore.QRect(470, 500, 431, 31))
        self.label_Part2_bar_result.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_Part2_bar_result.setText("")
        self.label_Part2_bar_result.setObjectName("label_Part2_bar_result")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_Part3_generate = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3_generate.setGeometry(QtCore.QRect(620, 570, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3_generate.setFont(font)
        self.pushButton_Part3_generate.setObjectName("pushButton_Part3_generate")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(160, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_Part3_input = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_input.setGeometry(QtCore.QRect(10, 50, 430, 430))
        self.label_Part3_input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_input.setText("")
        self.label_Part3_input.setObjectName("label_Part3_input")
        self.label_Part3_result = QtWidgets.QLabel(self.tab_2)
        self.label_Part3_result.setGeometry(QtCore.QRect(470, 50, 430, 430))
        self.label_Part3_result.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Part3_result.setText("")
        self.label_Part3_result.setObjectName("label_Part3_result")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(600, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_Part3_input = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_Part3_input.setGeometry(QtCore.QRect(160, 510, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_Part3_input.setFont(font)
        self.pushButton_Part3_input.setObjectName("pushButton_Part3_input")
        self.lineEdit_Part3_k = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Part3_k.setGeometry(QtCore.QRect(690, 500, 51, 41))
        self.lineEdit_Part3_k.setObjectName("lineEdit_Part3_k")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(600, 510, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Part1_input.setText(_translate("Form", "Input Image"))
        self.label_15.setText(_translate("Form", "Original Image"))
        self.label_18.setText(_translate("Form", "Color Model Conversion"))
        self.pushButton_Part1_generate.setText(_translate("Form", "Generate"))
        self.comboBox_Part1.setItemText(0, _translate("Form", "RGB"))
        self.comboBox_Part1.setItemText(1, _translate("Form", "CMY"))
        self.comboBox_Part1.setItemText(2, _translate("Form", "HSI"))
        self.comboBox_Part1.setItemText(3, _translate("Form", "XYZ"))
        self.comboBox_Part1.setItemText(4, _translate("Form", "L*a*b*"))
        self.comboBox_Part1.setItemText(5, _translate("Form", "YUV"))
        self.label_22.setText(_translate("Form", "Color plane："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Part1"))
        self.pushButton_Part2_generate.setText(_translate("Form", "Generate"))
        self.comboBox_Part2.setItemText(0, _translate("Form", "Jet"))
        self.comboBox_Part2.setItemText(1, _translate("Form", "HSV"))
        self.comboBox_Part2.setItemText(2, _translate("Form", "Hot"))
        self.comboBox_Part2.setItemText(3, _translate("Form", "Cool"))
        self.label_11.setText(_translate("Form", "Input Grayscale Image"))
        self.label_12.setText(_translate("Form", "Pesudo-color Image"))
        self.pushButton_Part2_input.setText(_translate("Form", "Input Image"))
        self.label_Part2_mode.setText(_translate("Form", "Mode："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Part2"))
        self.pushButton_Part3_generate.setText(_translate("Form", "generate"))
        self.label_8.setText(_translate("Form", "Original Image"))
        self.label_9.setText(_translate("Form", "Color Segmentation"))
        self.pushButton_Part3_input.setText(_translate("Form", "Input Image"))
        self.label_26.setText(_translate("Form", "k values = "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Part3"))


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
## -------------------------------------------------------Part1----------------------------------------------  
    # input image
    def button_clicked_input1(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part1 = file_path
        print('path:', self.file_path_Part1)

        # display on frame of label
        img = cv.imread(self.file_path_Part1)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_input.setPixmap(pixmap)
        return self.file_path_Part1
    
    # RGB
    def RGB(self, imagepath):
        input_img = cv.imread(imagepath)
        RGB_img = input_img[:, :,::-1]
        return RGB_img
    # CMY
    def CMY(self, imagepath):
        CMY_img = 255 - self.RGB(imagepath)
        return CMY_img
    # HSV
    def HSV(self, imagepath):
        input_img = cv.imread(imagepath)
        HSV_img = cv.cvtColor(input_img, cv.COLOR_BGR2HSV)
        return HSV_img
    # XYZ
    def XYZ(self, imagepath):
        input_img = cv.imread(imagepath)
        input_img = input_img[:, :,::-1]
        XYZ_img = cv.cvtColor(input_img, cv.COLOR_RGB2XYZ)
        return XYZ_img
    # L*a*b*
    def Lab(self, imagepath):
        input_img = cv.imread(imagepath)
        input_img = input_img[:, :,::-1]
        Lab_img = cv.cvtColor(input_img, cv.COLOR_RGB2LAB)
        return Lab_img
    # YUV
    def YUV(self, imagepath):
        input_img = cv.imread(imagepath)
        input_img = input_img[:, :,::-1]
        YUV_img = cv.cvtColor(input_img, cv.COLOR_RGB2YUV)
        return YUV_img
    
    # display
    def display_Part1_result(self, imagepath):
        index = self.ui.comboBox_Part1.currentIndex()
        if index == 0:  
            img = self.RGB(imagepath)
        if index == 1:  
            img = self.CMY(imagepath)         
        elif index == 2:      
            img = self.HSV(imagepath)
        elif index == 3:      
            img = self.XYZ(imagepath)
        elif index == 4:      
            img = self.Lab(imagepath)
        elif index == 5:      
            img = self.YUV(imagepath)

        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part1_result.setPixmap(pixmap)
        
## -------------------------------------------------------Part2----------------------------------------------    
    # imput image
    def button_clicked_input2(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part2 = file_path
        print('path:', self.file_path_Part2)

        # display on frame of label
        img = cv.imread(self.file_path_Part2)
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray_img = gray_img.astype(np.uint8)
        h, w = gray_img.shape 
        bytesPerline = w * 1 
        
        qimg = QtGui.QImage(gray_img, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_input.setPixmap(pixmap)
        return self.file_path_Part2
    
    def pseudo(self, imagepath):
        index = self.ui.comboBox_Part2.currentIndex()
        input_img = cv.imread(imagepath)
        input_img = input_img[:, :,::-1]

        gray_bar = np.linspace(0, 255, 256)
        gray_bar = np.vstack((gray_bar, gray_bar))
        img_new = input_img
        color_bar = np.zeros((2, 265, 3))

        if index == 0:
            img_new = cv.applyColorMap(input_img, cv.COLORMAP_JET)
            color_bar = cv.applyColorMap(gray_bar.astype(np.uint8), cv.COLORMAP_JET)
        elif index == 1:
            img_new = cv.applyColorMap(input_img, cv.COLORMAP_HSV)
            color_bar = cv.applyColorMap(gray_bar.astype(np.uint8), cv.COLORMAP_HSV)
        elif index == 2:
            img_new = cv.applyColorMap(input_img, cv.COLORMAP_HOT)
            color_bar = cv.applyColorMap(gray_bar.astype(np.uint8), cv.COLORMAP_HOT)
        elif index == 3:
            img_new = cv.applyColorMap(input_img, cv.COLORMAP_COOL)
            color_bar = cv.applyColorMap(gray_bar.astype(np.uint8), cv.COLORMAP_COOL)
        img_new = img_new[:,:,::-1]
        color_bar = color_bar[:,:,::-1]
       
        return gray_bar, img_new, color_bar
    
    def display_Part2_result(self, imagepath):
        gray_bar, img_new, color_bar = self.pseudo(imagepath)
        
        # gray bar
        gray_bar = gray_bar.astype(np.uint8)
        h, w = gray_bar.shape 
        bytesPerline = w * 1 
        qimg = QtGui.QImage(gray_bar, w, h, bytesPerline, QtGui.QImage.Format_Grayscale8)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(431, 31, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_bar_gray.setPixmap(pixmap)

        # pseudo image
        img_new = img_new.astype(np.uint8)
        h, w ,d = img_new.shape
        bytesPerline = w * d 
        qimg = QtGui.QImage(img_new, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_result.setPixmap(pixmap)

        # color bar
        color_bar = color_bar.astype(np.uint8)
        h, w ,d = color_bar.shape
        bytesPerline = w * d 
        qimg = QtGui.QImage(color_bar, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(431, 31, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part2_bar_result.setPixmap(pixmap)
    
    
## -------------------------------------------------------Part3----------------------------------------------    
    # input image
    def button_clicked_input3(self): 
        # get image path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(filter = 'JPEG (*.jpg *.bmp)')     # 讀取圖片
        self.file_path_Part3 = file_path
        print('path:', self.file_path_Part3)

        # display on frame of label
        img = cv.imread(self.file_path_Part3)
        img = img[:, :,::-1]
        img = img.astype(np.uint8)
        h, w, d = img.shape 
        bytesPerline = w * d 
        
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part3_input.setPixmap(pixmap)
        return self.file_path_Part3
    
    def segmentation(self, imagepath, k):
        input_img = self.RGB(imagepath)
        X = input_img.reshape(-1, 3)
        kmean = KMeans(n_clusters = k, n_init = 10)
        kmean.fit(X)
        seg_img = kmean.cluster_centers_[kmean.labels_]
        seg_img = seg_img.reshape(input_img.shape).astype(np.uint8)
        return seg_img

    def display_Part3_result(self, imagepath):
        k = int(self.ui.lineEdit_Part3_k.text())
        img = self.segmentation(imagepath, k)

        img = img.astype(np.uint8)
        h, w , d = img.shape 
        bytesPerline = w * d 
        qimg = QtGui.QImage(img, w, h, bytesPerline, QtGui.QImage.Format_RGB888)   #轉成QImage
        pixmap = QtGui.QPixmap(qimg)    #轉成QPixmap
        pixmap = pixmap.scaled(430, 430, QtCore.Qt.KeepAspectRatio) #縮小圖片並保持比例
        self.ui.label_Part3_result.setPixmap(pixmap)

 ## -------------------------------------------------------controller----------------------------------------------     
    def setup_control(self):
        # Part 1
        self.ui.pushButton_Part1_input.clicked.connect(self.button_clicked_input1)
        self.ui.pushButton_Part1_generate.clicked.connect(lambda: self.display_Part1_result(self.file_path_Part1))
        # Part 2
        self.ui.pushButton_Part2_input.clicked.connect(self.button_clicked_input2)
        self.ui.pushButton_Part2_generate.clicked.connect(lambda: self.display_Part2_result(self.file_path_Part2))
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