# import pydicom
# from matplotlib import pyplot as plt
# filename = "test.dcm"
# ds = pydicom.dcmread(filename)
# data = ds.pixel_array
# plt.imshow(data, cmap='gray')
# plt.show()


import pydicom
import matplotlib.pyplot as plt
import scipy.misc
import cv2 as cv
in_path = './test.dcm'
out_path = './output.png'
ds = pydicom.read_file(in_path)  #读取.dcm文件
img = ds.pixel_array  # 提取图像信息
print(img.shape)
plt.imshow(img)
plt.show()
cv.imwrite(out_path,img)  

# import sys, time
# from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QApplication, 
#                              QPushButton, QLabel, QFileDialog, QVBoxLayout, 
#                              QLineEdit)
# from PyQt5.QtGui import QPixmap, QFont
# from PyQt5.Qt import QSize, QImageReader
# #import qdarkstyle


# class mainwindow(QMainWindow):
#     def __init__(self):
#         super(mainwindow, self).__init__()

#         layout = QVBoxLayout()
#         w = QWidget()
#         w.setLayout(layout)
#         self.setCentralWidget(w)

#         self.image_label = QLabel()
#         self.image_label.setFixedSize(800, 500)
#         layout.addWidget(self.image_label)

#         tmp_layout = QHBoxLayout()
#         btn = QPushButton("選擇圖片路徑")
#         tmp_layout.addWidget(btn)
#         btn.clicked.connect(self.load_image)

#         self.result = QLineEdit()
#         self.result.setPlaceholderText("車牌展示")
#         self.result.setReadOnly(True)
#         tmp_layout.addWidget(self.result)
#         layout.addLayout(tmp_layout)

#         #self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

#     def load_image(self):
#         fname, _ = QFileDialog.getOpenFileName(self, 'Open File', 
#                    'C://', "Image files (*.jpg *.png)")
#         if fname is not None:
#             # 還需要對圖片進行重新調整大小
#             img = QImageReader(fname)
#             scale = 800 / img.size().width()
#             height = int(img.size().height() * scale)
#             img.setScaledSize(QSize(800, height))
#             img = img.read()
#             # 開啟設定好的圖片
#             pixmap = QPixmap(img)
#             self.image_label.setPixmap(pixmap)
#             self.result.setText("車牌號放到這裡")


# if __name__ == '__main__':
#     app = QApplication([])
#     font = QFont()
#     font.setFamily("SimHei")
#     font.setPointSize(14)
#     app.setFont(font)
#     m = mainwindow()
#     m.show()
#     sys.exit(app.exec())