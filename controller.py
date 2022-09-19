from PySide6 import QtCore 
from PySide6.QtGui import QImage, QPixmap,QFont, QImageReader
from PySide6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication, 
                             QPushButton, QLabel, QFileDialog, QVBoxLayout, 
                             QLineEdit)
from PySide6.QtCore import QSize
# from PySide6.QtWidgets import *
# from PySide6.QtCore import QThread, pyqtSignal
from PySide6.QtWidgets import  QMessageBox
import time
import os
import sys
import cv2 as cv
import pydicom
import pathlib
import matplotlib.pyplot as plt
from UI import Ui_MainWindow
class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()
    def setup_control(self):
        #self.ui.button_exit.clicked.connect(lambda:self.close())
        self.ui.openfile.clicked.connect(self.open_file)
        self.ui.run.clicked.connect(self.display_img)
        #self.ui.run.clicked.connect(self.display_dicom)
    def open_file(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "Open file Window", "../") # start path        
        self.img_path = filename
        

        #self.ui.statusbar.showMessage(f"video path: {self.video_path}")
    def display_img(self):
        #self.img = cv.imread(self.img_path)
        # height, width, channel = self.img.shape
        # bytesPerline = 3 * width
        # self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        # self.ui.label_img.setPixmap(QPixmap.fromImage(self.qimg))
        path=pathlib.Path(self.img_path)
        path_extension=path.suffixes
        name=['.dcm']
        if path_extension==name:
            
            out_path = './output.png'
            ds = pydicom.read_file(self.img_path)  #读取.dcm文件
            img = ds.pixel_array  # 提取图像信息
            print(img.shape)
            #plt.imshow(img)
            #plt.show()
            cv.imwrite(out_path,img)  
            self.img_path=out_path
        #if self.img_path is not None:
            # 還需要對圖片進行重新調整大小
        img = QImageReader(self.img_path)
        scale = 800 / img.size().width()
        height = int(img.size().height() * scale)
        img.setScaledSize(QSize(800, height))
        img = img.read()
        # 開啟設定好的圖片
        pixmap = QPixmap(img)
        self.ui.label_img.setPixmap(pixmap)
        self.ui.file_path.setText(self.img_path)

