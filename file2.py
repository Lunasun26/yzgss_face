from moviepy.editor import VideoFileClip
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys
from keras.models import load_model
import numpy as np
from utils import preprocess_input
from tensorflow.compat.v1 import ConfigProto, InteractiveSession
from datetime import datetime

class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 663)
        MainWindow.setStyleSheet("background-color: rgb(67, 152, 255)")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Setup main title label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 591, 101))
        self.label.setStyleSheet("font: 44pt \"微软雅黑\"; color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label.setText("人脸表情视频检测")

        # Setup time display label
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 80, 201, 51))
        self.label_5.setStyleSheet("font: 24pt \"微软雅黑\"; color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")

        # Setup date display label
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 40, 250, 31))
        self.label_7.setStyleSheet("font: 26pt \"微软雅黑\"; color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")

        # Setup day of the week display label
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(740, 110, 51, 21))
        self.label_8.setStyleSheet("font: 12pt \"微软雅黑\"; color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")

        # Setup video display area
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 160, 741, 421))
        self.label_13.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.label_13.setObjectName("label_13")

        # Setup file selection button
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(0, 610, 61, 51))
        self.file.setStyleSheet("background-color: transparent;")
        self.file.setObjectName("file")

        # Setup shutdown button
        self.shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.shutdown.setGeometry(QtCore.QRect(970, 610, 61, 51))
        self.shutdown.setStyleSheet("background-color: transparent;")
        self.shutdown.setObjectName("shutdown")

        # Setup camera button
        self.camera = QtWidgets.QPushButton(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(890, 610, 61, 51))
        self.camera.setStyleSheet("background-color: transparent;")
        self.camera.setObjectName("camera")

        # Setup action button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 600, 131, 51))
        self.pushButton.setStyleSheet("font: 16pt \"Arial\"; background-color: rgb(188, 188, 188);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("选择文件")

        # Setup status label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 600, 141, 51))
        self.label_2.setStyleSheet("background-color: rgb(188, 188, 188); font: 12pt \"Arial\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Setup empty label
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 600, 81, 51))
        self.label_3.setStyleSheet("background-color: rgb(188, 188, 188); font: 12pt \"Arial\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        # Setup stop detection button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 600, 131, 51))
        self.pushButton_2.setStyleSheet("font: 16pt \"Arial\"; background-color: rgb(188, 188, 188);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("结束检测")

        MainWindow.setCentralWidget(self.centralwidget)

        config = ConfigProto()
        config.gpu_options.allow_growth = True
        session = InteractiveSession(config=config)

        emotion_model_path = 'trained_models/float_models/fer2013_mini_XCEPTION.33-0.65.hdf5'
        self.emotion_labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'sad', 5: 'surprise', 6: 'neutral'}
        detection_model_path = 'trained_models/facemodel/haarcascade_frontalface_default.xml'

        self.emotion_classifier = load_model(emotion_model_path, compile=False)
        self.face_detection = cv2.CascadeClassifier(detection_model_path)
        self.emotion_target_size = self.emotion_classifier.input_shape[1:3]

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.file_main)

    def file_main(self):
        fname, _ = QFileDialog.getOpenFileName(None, 'Open File', '', "Video Files (*.avi *.mp4);;All Files(*)")
        if fname:
            self.process_video(fname)

    def process_video(self, fname):
        clip = VideoFileClip(fname)
        for img in clip.iter_frames():
            if self.pushButton_2.isDown():
                self.label_13.setStyleSheet("background-color: rgb(236, 236, 236);")
                cv2.destroyAllWindows()
                self.label_3.setText('')
                break

            input_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_h, img_w, _ = np.shape(input_img)
            input_img = cv2.resize(input_img, (741, int(741 * img_h / img_w)))
            if self.label_13.isVisible():
                input_img = self.save_predict('temp.png')
                cv2.imwrite('res.png', input_img)
                self.label_13.setStyleSheet("image: url(./res.png)")

            if cv2.waitKey(30) & 0xFF == 27:
                break

    def general_predict(self, imggray, imgcolor):
        gray_image = np.expand_dims(imggray, axis=2)
        faces = self.face_detection.detectMultiScale(imggray, 1.3, 5)
        res = []
        if len(faces) == 0:
            return None
        for face_coordinates in faces:
            x1, y1, width, height = face_coordinates
            x1, y1, x2, y2 = x1, y1, x1 + width, y1 + height
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (self.emotion_target_size))
                gray_face = preprocess_input(gray_face, True)
                gray_face = np.expand_dims(gray_face, 0)
                gray_face = np.expand_dims(gray_face, -1)
                emotion_prediction = self.emotion_classifier.predict(gray_face)
                emotion_label_arg = np.argmax(emotion_prediction)
                res.append([emotion_label_arg, x1, y1, x2, y2])
            except:
                continue
        return res

    def save_predict(self, imgurl):
        imggray = cv2.imread(imgurl, 0)
        imgcolor = cv2.imread(imgurl, 1)
        ress = self.general_predict(imggray, imgcolor)
        if ress is None:
            return imgcolor
        for res in ress:
            label = self.emotion_labels[res[0]]
            lx, ly, rx, ry = res[1], res[2], res[3], res[4]
            cv2.rectangle(imgcolor, (lx, ly), (rx, ry), (0, 0, 255), 2)
            cv2.putText(imgcolor, label, (lx, ly), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 2, cv2.LINE_AA)
        return imgcolor

    def update_time(self):
        current_time = datetime.now()
        time_str = current_time.strftime("%H:%M:%S")
        date_str = current_time.strftime("%Y/%m/%d")
        weekday_str = datetime.now().strftime("%A")
        weekday_translation = {
            "Monday": "星期一", "Tuesday": "星期二", "Wednesday": "星期三",
            "Thursday": "星期四", "Friday": "星期五", "Saturday": "星期六", "Sunday": "星期日"
        }
        self.label_5.setText(time_str)
        self.label_7.setText(date_str)
        self.label_8.setText(weekday_translation[weekday_str])

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())