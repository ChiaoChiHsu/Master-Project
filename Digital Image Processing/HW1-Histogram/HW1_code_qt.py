import numpy as np
import cv2
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap, QColor


# base32 table
base32_dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
              "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18,
              "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27,
              "S": 28, "T": 29, "U": 30, "V": 31}

img_dic = {"JET.64": "img_JET", "LIBERTY.64": "img_LIBERTY", "LINCOLN.64": "img_LINCOLN", "LISA.64": "img_LISA"}
           
#宣告用來存讀進來的圖片
img_JET = np.zeros((64,64), dtype="int8")
img_LIBERTY = np.zeros((64,64), dtype="int8")
img_LINCOLN = np.zeros((64,64), dtype="int8")
img_LISA = np.zeros((64,64), dtype="int8")


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1239, 877)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 170, 1151, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_part2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_part2.setFont(font)
        self.label_part2.setObjectName("label_part2")
        self.verticalLayout_3.addWidget(self.label_part2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_op3_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_op3_2.setObjectName("comboBox_op3_2")
        self.comboBox_op3_2.addItem("")
        self.comboBox_op3_2.addItem("")
        self.comboBox_op3_2.addItem("")
        self.comboBox_op3_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_op3_2, 2, 2, 1, 1)
        self.lineEdit_op1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_op1.setObjectName("lineEdit_op1")
        self.gridLayout.addWidget(self.lineEdit_op1, 0, 2, 1, 1)
        self.Button_op2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Button_op2.setObjectName("Button_op2")
        self.gridLayout.addWidget(self.Button_op2, 1, 3, 1, 1)
        self.Button_op3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Button_op3.setObjectName("Button_op3")
        self.gridLayout.addWidget(self.Button_op3, 2, 3, 1, 1)
        self.comboBox_op3_1 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_op3_1.setObjectName("comboBox_op3_1")
        self.comboBox_op3_1.addItem("")
        self.comboBox_op3_1.addItem("")
        self.comboBox_op3_1.addItem("")
        self.comboBox_op3_1.addItem("")
        self.gridLayout.addWidget(self.comboBox_op3_1, 2, 1, 1, 1)
        self.lineEdit_op2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_op2.setObjectName("lineEdit_op2")
        self.gridLayout.addWidget(self.lineEdit_op2, 1, 2, 1, 1)
        self.comboBox_op2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_op2.setObjectName("comboBox_op2")
        self.comboBox_op2.addItem("")
        self.comboBox_op2.addItem("")
        self.comboBox_op2.addItem("")
        self.comboBox_op2.addItem("")
        self.gridLayout.addWidget(self.comboBox_op2, 1, 1, 1, 1)
        self.comboBox_op4 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_op4.setObjectName("comboBox_op4")
        self.comboBox_op4.addItem("")
        self.comboBox_op4.addItem("")
        self.comboBox_op4.addItem("")
        self.comboBox_op4.addItem("")
        self.gridLayout.addWidget(self.comboBox_op4, 3, 1, 1, 1)
        self.Button_op4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Button_op4.setObjectName("Button_op4")
        self.gridLayout.addWidget(self.Button_op4, 3, 3, 1, 1)
        self.Button_op1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Button_op1.setObjectName("Button_op1")
        self.gridLayout.addWidget(self.Button_op1, 0, 3, 1, 1)
        self.label_op2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_op2.setFont(font)
        self.label_op2.setObjectName("label_op2")
        self.gridLayout.addWidget(self.label_op2, 1, 0, 1, 1)
        self.comboBox_op1 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_op1.setObjectName("comboBox_op1")
        self.comboBox_op1.addItem("")
        self.comboBox_op1.addItem("")
        self.comboBox_op1.addItem("")
        self.comboBox_op1.addItem("")
        self.gridLayout.addWidget(self.comboBox_op1, 0, 1, 1, 1)
        self.label_op4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_op4.setFont(font)
        self.label_op4.setObjectName("label_op4")
        self.gridLayout.addWidget(self.label_op4, 3, 0, 1, 1)
        self.label_op1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_op1.setFont(font)
        self.label_op1.setObjectName("label_op1")
        self.gridLayout.addWidget(self.label_op1, 0, 0, 1, 1)
        self.label_op3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_op3.setFont(font)
        self.label_op3.setObjectName("label_op3")
        self.gridLayout.addWidget(self.label_op3, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 1151, 102))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_part1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_part1.setFont(font)
        self.label_part1.setObjectName("label_part1")
        self.verticalLayout.addWidget(self.label_part1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_his_JET = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_his_JET.setObjectName("Button_his_JET")
        self.horizontalLayout.addWidget(self.Button_his_JET)
        self.Button_his_LIBERTY = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_his_LIBERTY.setObjectName("Button_his_LIBERTY")
        self.horizontalLayout.addWidget(self.Button_his_LIBERTY)
        self.Button_his_LINCOLN = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_his_LINCOLN.setObjectName("Button_his_LINCOLN")
        self.horizontalLayout.addWidget(self.Button_his_LINCOLN)
        self.Button_his_LISA = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_his_LISA.setObjectName("Button_his_LISA")
        self.horizontalLayout.addWidget(self.Button_his_LISA)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_img_1 = QtWidgets.QLabel(Form)
        self.label_img_1.setGeometry(QtCore.QRect(40, 380, 256, 256))
        self.label_img_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_1.setText("")
        self.label_img_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_img_1.setObjectName("label_img_1")
        self.label_img_2 = QtWidgets.QLabel(Form)
        self.label_img_2.setGeometry(QtCore.QRect(340, 380, 256, 256))
        self.label_img_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_2.setText("")
        self.label_img_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_img_2.setObjectName("label_img_2")
        self.label_img_3 = QtWidgets.QLabel(Form)
        self.label_img_3.setGeometry(QtCore.QRect(640, 380, 256, 256))
        self.label_img_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_3.setText("")
        self.label_img_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_img_3.setObjectName("label_img_3")
        self.label_img_4 = QtWidgets.QLabel(Form)
        self.label_img_4.setGeometry(QtCore.QRect(940, 380, 256, 256))
        self.label_img_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_4.setText("")
        self.label_img_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_img_4.setObjectName("label_img_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_part2.setText(_translate("Form", "Part 2: Arithmetic Operations of an Image Array"))
        self.comboBox_op3_2.setItemText(0, _translate("Form", "JET.64"))
        self.comboBox_op3_2.setItemText(1, _translate("Form", "LIBERTY.64"))
        self.comboBox_op3_2.setItemText(2, _translate("Form", "LINCOLN.64"))
        self.comboBox_op3_2.setItemText(3, _translate("Form", "LISA.64"))
        self.lineEdit_op1.setPlaceholderText(_translate("Form", "please input int"))
        self.Button_op2.setText(_translate("Form", "generate"))
        self.Button_op3.setText(_translate("Form", "generate"))
        self.comboBox_op3_1.setItemText(0, _translate("Form", "JET.64"))
        self.comboBox_op3_1.setItemText(1, _translate("Form", "LIBERTY.64"))
        self.comboBox_op3_1.setItemText(2, _translate("Form", "LINCOLN.64"))
        self.comboBox_op3_1.setItemText(3, _translate("Form", "LISA.64"))
        self.lineEdit_op2.setPlaceholderText(_translate("Form", "please input int"))
        self.comboBox_op2.setItemText(0, _translate("Form", "JET.64"))
        self.comboBox_op2.setItemText(1, _translate("Form", "LIBERTY.64"))
        self.comboBox_op2.setItemText(2, _translate("Form", "LINCOLN.64"))
        self.comboBox_op2.setItemText(3, _translate("Form", "LISA.64"))
        self.comboBox_op4.setItemText(0, _translate("Form", "JET.64"))
        self.comboBox_op4.setItemText(1, _translate("Form", "LIBERTY.64"))
        self.comboBox_op4.setItemText(2, _translate("Form", "LINCOLN.64"))
        self.comboBox_op4.setItemText(3, _translate("Form", "LISA.64"))
        self.Button_op4.setText(_translate("Form", "generate"))
        self.Button_op1.setText(_translate("Form", "generate"))
        self.label_op2.setText(_translate("Form", "2. Multiply a constant"))
        self.comboBox_op1.setItemText(0, _translate("Form", "JET.64"))
        self.comboBox_op1.setItemText(1, _translate("Form", "LIBERTY.64"))
        self.comboBox_op1.setItemText(2, _translate("Form", "LINCOLN.64"))
        self.comboBox_op1.setItemText(3, _translate("Form", "LISA.64"))
        self.label_op4.setText(_translate("Form", "4. g(x,y) = f(x,y) - f(x-1,y)"))
        self.label_op1.setText(_translate("Form", "1. Add or subtract a constant"))
        self.label_op3.setText(_translate("Form", "3. Create a new image which is the average image of two input images."))
        self.label_part1.setText(_translate("Form", "Part 1: Histogram of image"))
        self.Button_his_JET.setText(_translate("Form", "JET.64"))
        self.Button_his_LIBERTY.setText(_translate("Form", "LIBERTY.64"))
        self.Button_his_LINCOLN.setText(_translate("Form", "LINCOLN.64"))
        self.Button_his_LISA.setText(_translate("Form", "LISA.64"))

        
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()     #UI.py中class名稱
        self.ui.setupUi(self)
        self.load_img("JET.64", img_JET)
        self.load_img("LIBERTY.64", img_LIBERTY)
        self.load_img("LINCOLN.64", img_LINCOLN)
        self.load_img("LISA.64", img_LISA)
        self.setup_control()

    #讀入圖片
    def load_img(self, filename, img_arr):
        with open(filename, "r") as f:
            data = f.read().splitlines()

        for i in range(64):
            for j in range(64):
                img_arr[i][j] = base32_dic[data[i][j]]


    # Histogram
    def show_histogram(self, img_arr):   #input img_name and img_arr to calculate histogram
        his_arr = np.zeros(32, np.uint16)
        for i in range(64):
            for j in range(64):
                his_arr[img_arr[i][j]] = his_arr[img_arr[i][j]] + 1


        # 畫直方圖
        hist_height = 256
        hist_width = 256
        hist_image = np.zeros((hist_height, hist_width), dtype=np.uint8) #要用uint8才能cv2正常顯示
        
        # Perform min-max scaling
        min_val = 0
        max_val = np.max(his_arr)
        scaled_matrix = (his_arr - min_val) / (max_val - min_val)*hist_height
        bin_width = hist_width // 32    #每條直方圖的寬度

        for i in range(32):
            x1 = i * bin_width
            x2 = (i + 1) * bin_width
            y1 = hist_height
            y2 =hist_height - int(scaled_matrix[i])
            color = (255)  # (B,G,R)藍色
            thickness = -1  # 將長方形填滿
            cv2.rectangle(hist_image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
            
        # hist_image = cv2.resize(hist_image, (256,256))
        height, width= hist_image.shape
        bytesPerline = width * 1
        self.myqimage = QImage(hist_image.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_1.setPixmap(QPixmap.fromImage(self.myqimage))
        return 

    #單純return不印出來
    def histogram(self, img_arr):   #input img_name and img_arr to calculate histogram
        his_arr = np.zeros(32, np.uint16)
        for i in range(64):
            for j in range(64):
                his_arr[img_arr[i][j]] = his_arr[img_arr[i][j]] + 1


        # 畫直方圖
        hist_height = 256
        hist_width = 256
        hist_image = np.zeros((hist_height, hist_width), dtype=np.uint8) #要用uint8才能cv2正常顯示
        
        # Perform min-max scaling
        min_val = 0
        max_val = np.max(his_arr)
        scaled_matrix = (his_arr - min_val) / (max_val - min_val) * hist_height
        bin_width = hist_width // 32    #每條直方圖的寬度

        for i in range(32):
            x1 = i * bin_width
            x2 = (i + 1) * bin_width
            y1 = hist_height
            y2 =hist_height - int(scaled_matrix[i])
            color = (255)  # (B,G,R)藍色
            thickness = -1  # 將長方形填滿
            cv2.rectangle(hist_image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
            
        # hist_image = cv2.resize(hist_image, (256,256))
        return hist_image

    def add_constant(self, img_arr, constant):
        # img_arr = img_arr + constant  #兩種寫法都可以
        img_add = np.add(img_arr.astype("uint16"), constant)    #先設uint16避免加完常數後overflow
        img_add = np.clip(img_add, 0, 31)   #將數值限定在31內，若大於31->其值=31
        his_origin = self.histogram(img_arr)
        his_add = self.histogram(img_add)

        #resize
        size = 256
        img_arr = cv2.resize(img_arr.astype("uint8"), (size,size))
        img_add= cv2.resize(img_add.astype("uint8"), (size,size))
        # his_origin = cv2.resize(self.histogram(img_arr), (size,size))
        # his_add = cv2.resize(self.histogram(img_add), (size,size))


        ##圖片印之前*8
        img_arr = np.multiply(img_arr, 8)
        img_arr = np.clip(img_arr, 0, 255)   #將數值限定在255內，若大於255->其值=255

        img_add = np.multiply(img_add, 8)
        img_add = np.clip(img_add, 0, 255)   #將數值限定在255內，若大於255->其值=255

        #轉回uint8,才能用cv2顯示
        img_add = img_add.astype("uint8")

        height, width= img_arr.shape
        bytesPerline = width * 1
        #原圖
        self.myqimage = QImage(img_arr.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_1.setPixmap(QPixmap.fromImage(self.myqimage))

        height, width= his_origin.shape
        bytesPerline = width * 1
        #原圖的直方圖
        self.myqimage = QImage(his_origin.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_2.setPixmap(QPixmap.fromImage(self.myqimage))

        #加完constant的圖
        self.myqimage = QImage(img_add.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_3.setPixmap(QPixmap.fromImage(self.myqimage))

        #加完constant的直方圖
        self.myqimage = QImage(his_add.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_4.setPixmap(QPixmap.fromImage(self.myqimage))
        return 
    
    def multiply_constant(self, img_arr, constant):
        # img_arr = img_arr + constant  #兩種寫法都可以
        img_multiply = np.multiply(img_arr.astype("uint16"), constant)  #先設uint16避免乘完常數後overflow
        img_multiply = np.clip(img_multiply, 0, 31)   #將數值限定在31內，若大於31->其值=31

        his_origin = self.histogram(img_arr)
        his_multiply =self.histogram(img_multiply)

        #resize
        size = 256
        img_arr = cv2.resize(img_arr.astype("uint8"), (size,size))
        img_multiply = cv2.resize(img_multiply.astype("uint16"), (size,size))
        
        ##圖片印之前*8
        img_arr = np.multiply(img_arr, 8)
        img_arr = np.clip(img_arr, 0, 255)   #將數值限定在255內，若大於255->其值=255

        img_multiply = np.multiply(img_multiply, 8)
        img_multiply = np.clip(img_multiply, 0, 255)   #將數值限定在255內，若大於255->其值=255
        
        #轉回uint8,才能用cv2顯示
        img_multiply = img_multiply.astype("uint8")
        height, width= img_arr.shape
        bytesPerline = width * 1
        #原圖
        self.myqimage = QImage(img_arr.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_1.setPixmap(QPixmap.fromImage(self.myqimage))

        #原圖的直方圖
        self.myqimage = QImage(his_origin.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_2.setPixmap(QPixmap.fromImage(self.myqimage))

        #加完constant的圖
        self.myqimage = QImage(img_multiply.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_3.setPixmap(QPixmap.fromImage(self.myqimage))

        #加完constant的直方圖
        self.myqimage = QImage(his_multiply.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_4.setPixmap(QPixmap.fromImage(self.myqimage))
        return

    def two_average(self, img_arr1, img_arr2):
        img_avg = (img_arr1 + img_arr2) / 2  
        img_avg = np.around(img_avg , 0).astype("uint8")    #轉回int
        his_avg =self.histogram(img_avg) 

        #resize
        size = 256
        img_avg = cv2.resize(img_avg.astype("uint8"), (size,size))
        height, width= img_avg.shape
        bytesPerline = width * 1
        #印出前*8
        img_avg = np.multiply(img_avg, 8)  

        self.myqimage = QImage(img_avg.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_1.setPixmap(QPixmap.fromImage(self.myqimage))
        self.myqimage = QImage(his_avg.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_2.setPixmap(QPixmap.fromImage(self.myqimage))
        return 

    def g_function(self, img_arr):
        img_g = np.zeros((64,64), dtype="int16")
        for i in range(64):
            for j in range(64):
                if i == 0:
                    img_g[i][j] = img_arr[i][j]
                else:
                    img_g[i][j] = img_arr[i][j] - img_arr[i-1][j]
        
        his_g =self.histogram(img_g) 
        img_g = np.clip(img_g, 0, 31)
        #resize
        size = 256
        img_g = cv2.resize(img_g, (size,size))
        height, width= img_g.shape
        bytesPerline = width * 1
        #印出前*8
        img_g = np.multiply(img_g, 8) 
        img_g = np.clip(img_g, 0, 255)   #將數值限定在31內，若大於31->其值=31
        img_g = img_g.astype("uint8")
        self.myqimage = QImage(img_g.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_1.setPixmap(QPixmap.fromImage(self.myqimage))
        self.myqimage = QImage(his_g.data, width, height, bytesPerline, QImage.Format_Grayscale8)
        self.ui.label_img_2.setPixmap(QPixmap.fromImage(self.myqimage))
        return 

    def setup_control(self):
        # TODO
        # self.ui.textEdit.setText('Happy World!')
        self.ui.Button_his_JET.clicked.connect(lambda: self.show_histogram(img_JET))                 
        self.ui.Button_his_LIBERTY.clicked.connect(lambda: self.show_histogram(img_LIBERTY))     
        self.ui.Button_his_LINCOLN.clicked.connect(lambda: self.show_histogram(img_LINCOLN))     
        self.ui.Button_his_LISA.clicked.connect(lambda: self.show_histogram(img_LISA))
        self.ui.Button_op1.clicked.connect(self.op1)    
        self.ui.Button_op2.clicked.connect(self.op2) 
        self.ui.Button_op3.clicked.connect(self.op3)
        self.ui.Button_op4.clicked.connect(self.op4)
        return

    def op1(self):
        op1_combobox_msg = self.ui.comboBox_op1.currentText()
        const = int(self.ui.lineEdit_op1.text())    #記得轉成int才能丟進add當參數
        if op1_combobox_msg == "JET.64":
            self.add_constant(img_JET, const)
        elif op1_combobox_msg == "LIBERTY.64":
            self.add_constant(img_LIBERTY, const)
        elif op1_combobox_msg == "LINCOLN.64":
            self.add_constant(img_LINCOLN, const)
        else:
            self.add_constant(img_LISA, const)


    def op2(self):
        op2_combobox_msg = self.ui.comboBox_op2.currentText()
        const = int(self.ui.lineEdit_op2.text())    #記得轉成int才能丟進add當參數
        if op2_combobox_msg == "JET.64":
            self.multiply_constant(img_JET, const)
        elif op2_combobox_msg == "LIBERTY.64":
            self.multiply_constant(img_LIBERTY, const)
        elif op2_combobox_msg == "LINCOLN.64":
            self.multiply_constant(img_LINCOLN, const)
        else:
            self.multiply_constant(img_LISA, const)

    def op3(self):
        op3_1_combobox_msg = self.ui.comboBox_op3_1.currentText()
        op3_2_combobox_msg = self.ui.comboBox_op3_2.currentText()
        if op3_1_combobox_msg == "JET.64":
            if op3_2_combobox_msg == "JET.64":
                self.two_average(img_JET, img_JET)
            elif op3_2_combobox_msg == "LIBERTY.64":
                self.two_average(img_JET, img_LIBERTY)
            elif op3_2_combobox_msg == "LINCOLN.64":
                self.two_average(img_JET, img_LINCOLN)
            else:
                self.two_average(img_JET, img_LISA)

        elif op3_1_combobox_msg == "LIBERTY.64":
            if op3_2_combobox_msg == "JET.64":
                self.two_average(img_LIBERTY, img_JET)
            elif op3_2_combobox_msg == "LIBERTY.64":
                self.two_average(img_LIBERTY, img_LIBERTY)
            elif op3_2_combobox_msg == "LINCOLN.64":
                self.two_average(img_LIBERTY, img_LINCOLN)
            else:
                self.two_average(img_LIBERTY, img_LISA)

        elif op3_1_combobox_msg == "LINCOLN.64":
            if op3_2_combobox_msg == "JET.64":
                self.two_average(img_LINCOLN, img_JET)
            elif op3_2_combobox_msg == "LIBERTY.64":
                self.two_average(img_LINCOLN, img_LIBERTY)
            elif op3_2_combobox_msg == "LINCOLN.64":
                self.two_average(img_LINCOLN, img_LINCOLN)
            else:
                self.two_average(img_LINCOLN, img_LISA)

        else:
            if op3_2_combobox_msg == "JET.64":
                self.two_average(img_LISA, img_JET)
            elif op3_2_combobox_msg == "LIBERTY.64":
                self.two_average(img_LISA, img_LIBERTY)
            elif op3_2_combobox_msg == "LINCOLN.64":
                self.two_average(img_LISA, img_LINCOLN)
            else:
                self.two_average(img_LISA, img_LISA)

    def op4(self):
        op4_combobox_msg = self.ui.comboBox_op4.currentText()
        if op4_combobox_msg == "JET.64":
            self.g_function(img_JET)
        elif op4_combobox_msg == "LIBERTY.64":
            self.g_function(img_LIBERTY)
        elif op4_combobox_msg == "LINCOLN.64":
            self.g_function(img_LINCOLN)
        else:
            self.g_function(img_LISA)

            



    #Qt小技巧(要寫在setup_control中)
    # self.ui.pushButton.clicked.connect(self.buttonClicked) # pushbutton觸發: self.ui.button名稱.clicked.connect(觸發的function)
    # msg = self.ui.lineEdit.text()     #將 lineEdit 的內容儲存至 msg 中



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())