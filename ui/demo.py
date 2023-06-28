# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
import image_recognition
import webbrowser


class MouseTracker(QWidget):
    def init(self):
        super().init()
        self.setMouseTracking(True)

    def isInLable(self, event):
        mp = event.pos()
        if (mp.x() > 20 and
                mp.y() > 20 and
                mp.x() < 20 + 971 and
                mp.y() < 20 + 671):
            return True
        else:
            return False


class ImageLabel(QLabel):
    def __init__(self, widget):
        super().__init__(widget)

    def setImage(self, path):
        self.image = QImage(path)

        if self.image.height() > 671 or self.image.width() > 971:
            self.image = self.image.smoothScaled(971, 671)

        if self.image.height() < 50 or self.image.width() < 50:
            self.image = self.image.smoothScaled(50, 50)

        self.setPixmap(QPixmap(self.image))

        self.result1, self.result2, self.result3 = image_recognition.classify(path)

    def setPixmap(self, image):
        super().setPixmap(image)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.mouse = MouseTracker()
        self.setAcceptDrops(True)
        self.setObjectName("MainWindow")
        self.resize(1200, 860)
        self.setMinimumSize(QtCore.QSize(1200, 860))
        self.setMaximumSize(QtCore.QSize(1200, 860))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(26)
        self.setFont(font)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.photoViewer = ImageLabel(self.centralwidget)
        self.centralwidget.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(66, 66, 113, 255), stop:1 rgba(0, 0, 0, 255));")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1000, 20, 181, 161))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(248, 228, 92);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.checkBreed())
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1000, 190, 181, 161))
        font = QtGui.QFont()
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(246, 211, 45)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.chooseImage())
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(26)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1000, 530, 181, 161))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(26)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(229, 165, 10)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.reset());
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 700, 321, 61))
        ffont = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(229, 165, 10)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = self.photoViewer
        self.label_2.setGeometry(QtCore.QRect(20, 20, 971, 671))
        self.label_2.setMinimumSize(QtCore.QSize(971, 671))
        self.label_2.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("background-color: rgba(200, 200, 200, 150);\n"
                                   "color: rgb(0,0,0);\n"
                                   "border: 4px dashed rgb(255, 255, 255);\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 700, 831, 61))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(222, 221, 218);\n"
                                   "text-align: center;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 770, 831, 31))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 810, 831, 31))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 770, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Fira Sans")
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(229, 165, 10)")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Klasyfikator ras psów"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Dodaj\nzdjęcie"))
        self.pushButton_4.setText(_translate("MainWindow", "Reset "))
        self.label.setText(_translate("MainWindow", "Rasa"))
        self.label_2.setText(_translate("MainWindow", "Upuść zdjęcie swojego psa tutaj"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", ""))
        self.label_6.setText(_translate("MainWindow", "Inne możliwe rasy"))

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasImage and self.mouse.isInLable(event):
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def chooseImage(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(), "Image files (*.jpg *.png *.jpeg)")
        if path[0] != '':
            self.label_2.setImage(path[0])


    def reset(self):
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_5.clear()
        self.label_2.setText("Upuść zdjęcie swojego psa tutaj")

    def checkBreed(self):
        self.label_3.setText(self.label_2.result1)
        self.label_4.setText(self.label_2.result2)
        self.label_5.setText(self.label_2.result3)

    def set_image(self, file_path):
        self.photoViewer.setImage(file_path)


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
