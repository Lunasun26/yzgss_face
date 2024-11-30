from PyQt5 import QtCore, QtGui, QtWidgets
from main3 import Ui_MainWindow
from camera import Ui_MainWindow2
from file import Ui_MainWindow3
from photo import Ui_MainWindow4
from decamera import Ui_MainWindow5
#from test import Ui_MainWindow6



class jiemian2(QtWidgets.QMainWindow,Ui_MainWindow2):
    def __init__(self):
        super(jiemian2,self).__init__()
        self.setupUi(self)  #加载相机识别模块 camera.py
        self.file.clicked.connect(self.back) #返回主界面功能按钮 连接下面的back函数

    def back(self):
        self.hide()           #隐藏此窗口
        self.log = loginWindow()
        self.log.show()       #显示登录窗口
                              #必须加上self


class jiemian3(QtWidgets.QMainWindow,Ui_MainWindow3):
    def __init__(self):
        super(jiemian3,self).__init__()
        self.setupUi(self)   #加载视频文件识别模块  file.py
        self.file.clicked.connect(self.back)  #返回主界面功能按钮 连接下面的back函数

    def back(self):
        self.hide()           #隐藏此窗口
        self.log = loginWindow()
        self.log.show()       #显示登录窗口

class jiemian4(QtWidgets.QMainWindow,Ui_MainWindow4):
    def __init__(self):
        super(jiemian4,self).__init__()
        self.setupUi(self)
        self.file.clicked.connect(self.back)  #返回主界面功能按钮 连接下面的back函数

    def back(self):
        self.hide()           #隐藏此窗口
        self.log = loginWindow()
        self.log.show()       #显示登录窗口



class jiemian5(QtWidgets.QMainWindow,Ui_MainWindow5):
    def __init__(self):
        super(jiemian5,self).__init__()
        self.setupUi(self)
        self.file.clicked.connect(self.back)  #返回主界面功能按钮 连接下面的back函数

    def back(self):
        self.hide()           #隐藏此窗口
        self.log = loginWindow()
        self.log.show()       #显示登录窗口


    def back(self):
        self.hide()           #隐藏此窗口
        self.log = loginWindow()
        self.log.show()       #显示登录窗口


#主界面
class loginWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(loginWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.camera)  #相机检测按钮   连接下面的camera_detect功能函数
        self.pushButton_2.clicked.connect(self.file_detect)  #视频文件检测按钮  连接下面的file_detect函数
        self.pushButton_3.clicked.connect(self.photo_detect)
        self.pushButton_4.clicked.connect(self.decamera)


    def file_detect(self):
        self.hide()
        self.jiemian3 = jiemian3() #加载视频文件识别界面
        self.jiemian3.show()

    def camera(self):
        self.hide()
        self.jiemian2 = jiemian2() #加载视频文件识别界面
        self.jiemian2.show()

    def photo_detect(self):
        self.hide()
        self.jiemian4 = jiemian4() #加载视频文件识别界面
        self.jiemian4.show()

    def decamera(self):
        self.hide()
        self.jiemian5 = jiemian5() #加载视频文件识别界面
        self.jiemian5.show()

    def test(self):
        self.hide()
        self.jiemian6 =jiemian6()
        self.jiemian6.show()



#运行窗口Login
if __name__=="__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    login_show = loginWindow()
    login_show.show()
    sys.exit(app.exec_())