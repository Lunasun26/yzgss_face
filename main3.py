# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 593)
        MainWindow.setStyleSheet("background-color: rgb(67, 152, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 431, 101))
        self.label.setStyleSheet("font: 40pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label_4.setStyleSheet("image: url(1/Wi-Fi.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(100, 170, 371, 411))
        self.label_11.setStyleSheet("image:url(1/白框区域.png);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 10, 41, 21))
        self.label_6.setStyleSheet("image: url(1/battery.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 280, 321, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 210, 141, 61))
        self.pushButton.setStyleSheet("font: 16pt \"Arial\";\n"
"background-color: rgb(194, 194, 194);")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 210, 91, 61))
        self.label_2.setStyleSheet("image: url(1/摄像头 (1).png);\n"
"background-color: transparent;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 390, 141, 61))
        self.pushButton_2.setStyleSheet("font: 16pt \"Arial\";\n"
"background-color: rgb(194, 194, 194);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 390, 91, 61))
        self.label_3.setStyleSheet("image: url(1/视频.png);\n"
"background-color: transparent;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(130, 370, 321, 1))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 300, 91, 61))
        self.label_5.setStyleSheet("image: url(1/图片.png);\n"
"background-color: transparent;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 300, 141, 61))
        self.pushButton_3.setStyleSheet("font: 16pt \"Arial\";\n"
"background-color: rgb(194, 194, 194);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 480, 141, 61))
        self.pushButton_4.setStyleSheet("font: 16pt \"Arial\";\n"
                                      "background-color: rgb(194, 194, 194);")
        self.pushButton_4.setObjectName("pushButton4")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(140, 480, 91, 61))
        self.label_22.setStyleSheet("image: url(1/摄像头 (1).png);\n"
                                   "background-color: transparent;")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")



        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(130, 460, 321, 1))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")




        self.label.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_11.raise_()
        self.line_2.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.line_3.raise_()
        self.label_5.raise_()


        self.line_5.raise_()


        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_22.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 添加1个 状态栏
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName('statusbar')
        self.setStatusBar(self.statusbar)

        # 创建1个 QTimer计时器对象
        timer = QtCore.QTimer(self)

        # 发射timeout信号，与自定义槽函数关联
        timer.timeout.connect(self.showtime)

        # 启动计时器
        timer.start()

    # 自定义槽函数，用来在状态栏中显示当前日期时间
    def showtime(self):
        # 获取当前日期时间
        datetime = QtCore.QDateTime.currentDateTime()

        # 格式化日期时间
        text = datetime.toString('yyyy-MM-dd HH:mm:ss')

        # 在状态栏中显示日期时间
        self.statusbar.showMessage(text)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "人脸表情预测系统"))
        self.pushButton.setText(_translate("MainWindow", "实时检测"))
        self.pushButton_2.setText(_translate("MainWindow", "视频文件检测"))
        self.pushButton_3.setText(_translate("MainWindow", "图片检测"))
        self.pushButton_4.setText(_translate("MainWindow", "烦躁检测"))
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())