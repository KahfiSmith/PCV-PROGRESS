from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import sys
import cv2
import numpy as np

class Ui_Dialog(object):

    def buka_gambar1(self):
        # Buka dialog untuk memilih file gambar
        filename = QFileDialog.getOpenFileName(
            None, "Pilih gambar", "", "Image files (*.jpg *.png)")

        # Jika file gambar dipilih
        if filename:
            # Konversi objek filename menjadi string
            filename_str = str(filename[0])

            # Baca gambar
            image = cv2.imread(filename_str)

            # Konversi gambar dari BGR ke RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Konversi gambar menjadi format QImage
            qimage = QImage(image_rgb.data, image_rgb.shape[1], image_rgb.shape[0],
                            image_rgb.shape[2] * image_rgb.shape[1], QImage.Format_RGB888)

            self.labelAsal1.setPixmap(QPixmap(qimage))
            self.labelAsal1.setScaledContents(True)

    def buka_gambar2(self):
        # Buka dialog untuk memilih file gambar
        filename = QFileDialog.getOpenFileName(
            None, "Pilih gambar", "", "Image files (*.jpg *.png)")

        # Jika file gambar dipilih
        if filename:
            # Konversi objek filename menjadi string
            filename_str = str(filename[0])

            # Baca gambar
            image = cv2.imread(filename_str)

            # Konversi gambar dari BGR ke RGB
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Konversi gambar menjadi format QImage
            qimage = QImage(image_rgb.data, image_rgb.shape[1], image_rgb.shape[0],
                            image_rgb.shape[2] * image_rgb.shape[1], QImage.Format_RGB888)
            self.labelAsal2.setPixmap(QPixmap(qimage))
            self.labelAsal2.setScaledContents(True)

    def operasi_penjumlahan(self):
        pixmap1 = self.labelAsal1.pixmap()
        if pixmap1 is None:
            return  # LabelAsal1 tidak memiliki gambar

        # Mendapatkan pixmap dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        if pixmap2 is None:
            return  # LabelAsal2 tidak memiliki gambar

        # Mengambil QImage dari pixmap1
        image1 = pixmap1.toImage()

        # Mengambil QImage dari pixmap2
        image2 = pixmap2.toImage()

        # Memastikan kedua gambar memiliki ukuran yang sama

        # Mengambil dimensi gambar
        width = image1.width()
        height = image1.height()

        # Inisialisasi QImage baru untuk menyimpan hasil penjumlahan
        result_image = QImage(width, height, QImage.Format_RGB888)

        # Lakukan penjumlahan pixel per pixel
        for x in range(width):
            for y in range(height):
                pixel1 = QColor(image1.pixel(x, y))
                pixel2 = QColor(image2.pixel(x, y))

                # Penjumlahan komponen RGB
                r = min(255, pixel1.red() + pixel2.red())
                g = min(255, pixel1.green() + pixel2.green())
                b = min(255, pixel1.blue() + pixel2.blue())

                # Set pixel hasil ke QImage
                result_image.setPixel(x, y, qRgb(r, g, b))

        # Konversi QImage hasil ke QPixmap
        result_pixmap = QPixmap.fromImage(result_image)

        # Tampilkan hasil di label_3
        self.label_3.setPixmap(result_pixmap)
        self.label_3.setScaledContents(True)

    def operasi_perkalian(self):
        # Dapatkan gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()
        width1 = image1.width()
        height1 = image1.height()
        bytes_per_line1 = image1.bytesPerLine()

        # Dapatkan gambar dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        image2 = pixmap2.toImage()
        width2 = image2.width()
        height2 = image2.height()
        bytes_per_line2 = image2.bytesPerLine()
        # Buat gambar hasil
        result_image = QImage(width1, height1, QImage.Format_RGB888)

        # Lakukan perkalian piksel per piksel
        for y in range(height1):
            for x in range(width1):
                # Dapatkan warna piksel dari kedua gambar
                color1 = QColor(image1.pixel(x, y))
                color2 = QColor(image2.pixel(x, y))

                # Hitung perkalian warna
                new_color = QColor(
                    min((color1.red() * color2.red()) // 255, 255),
                    min((color1.green() * color2.green()) // 255, 255),
                    min((color1.blue() * color2.blue()) // 255, 255)
                )

                # Set piksel pada gambar hasil
                result_image.setPixel(x, y, new_color.rgb())

        # Tampilkan gambar hasil di label_3
        self.label_3.setPixmap(QPixmap.fromImage(result_image))
        self.label_3.setScaledContents(True)

    def operasi_pengurangan(self):
        # Dapatkan gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()
        width1 = image1.width()
        height1 = image1.height()
        bytes_per_line1 = image1.bytesPerLine()

        # Dapatkan gambar dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        image2 = pixmap2.toImage()
        width2 = image2.width()
        height2 = image2.height()
        bytes_per_line2 = image2.bytesPerLine()

        # Buat gambar hasil
        result_image = QImage(width1, height1, QImage.Format_RGB888)

        # Lakukan pengurangan piksel per piksel
        for y in range(height1):
            for x in range(width1):
                # Dapatkan warna piksel dari kedua gambar
                color1 = QColor(image1.pixel(x, y))
                color2 = QColor(image2.pixel(x, y))

                # Hitung pengurangan warna
                new_color = QColor(
                    max((color1.red() - color2.red()), 0),
                    max((color1.green() - color2.green()), 0),
                    max((color1.blue() - color2.blue()), 0)
                )

                # Set piksel pada gambar hasil
                result_image.setPixel(x, y, new_color.rgb())

        # Tampilkan gambar hasil di label_3
        self.label_3.setPixmap(QPixmap.fromImage(result_image))
        self.label_3.setScaledContents(True)

    def operasi_pembagian(self):
        # Dapatkan gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()
        width1 = image1.width()
        height1 = image1.height()
        bytes_per_line1 = image1.bytesPerLine()

        # Dapatkan gambar dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        image2 = pixmap2.toImage()
        width2 = image2.width()
        height2 = image2.height()
        bytes_per_line2 = image2.bytesPerLine()

        # Buat gambar hasil
        result_image = QImage(width1, height1, QImage.Format_RGB888)

        # Lakukan pembagian piksel per piksel
        for y in range(height1):
            for x in range(width1):
                # Dapatkan warna piksel dari kedua gambar
                color1 = QColor(image1.pixel(x, y))
                color2 = QColor(image2.pixel(x, y))

                # Hindari pembagian oleh nol
                if color2.red() == 0 or color2.green() == 0 or color2.blue() == 0:
                    new_color = QColor(0, 0, 0)
                else:
                    # Hitung pembagian warna
                    new_color = QColor(
                        min(int((color1.red() / color2.red()) * 255), 255),
                        min(int((color1.green() / color2.green()) * 255), 255),
                        min(int((color1.blue() / color2.blue()) * 255), 255)
                    )

                # Set piksel pada gambar hasil
                result_image.setPixel(x, y, new_color.rgb())

        # Tampilkan gambar hasil di label_3
        self.label_3.setPixmap(QPixmap.fromImage(result_image))
        self.label_3.setScaledContents(True)

    def operasi_simpan(self):
        # Buka dialog untuk memilih lokasi penyimpanan
        filename, _ = QFileDialog.getSaveFileName(
            None, "Simpan Gambar", "", "Image files (*.png *.jpg)")

        # Jika lokasi penyimpanan dipilih
        if filename:
            # Dapatkan gambar dari label_3 pada Ui_MainWindow
            pixmap = self.label_3.pixmap()
            image = pixmap.toImage()

            # Simpan gambar ke lokasi yang dipilih
            if image.save(filename):
                print('tersimpan')
            else:
                print('gagal')

    def operasi_and(self):
        # Ambil gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()

        # Ambil gambar dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        image2 = pixmap2.toImage()

        # Pastikan kedua gambar memiliki dimensi yang sama
        if image1.size() == image2.size():
            # Buat gambar hasil yang kosong dengan dimensi yang sama
            width = image1.width()
            height = image1.height()
            result_image = QImage(width, height, QImage.Format_RGB888)

            # Lakukan operasi "AND" piksel per piksel
            for x in range(width):
                for y in range(height):
                    # Dapatkan warna piksel dari kedua gambar
                    color1 = QColor(image1.pixel(x, y))
                    color2 = QColor(image2.pixel(x, y))

                    # Lakukan operasi "AND" pada komponen warna (R, G, B)
                    new_red = color1.red() & color2.red()
                    new_green = color1.green() & color2.green()
                    new_blue = color1.blue() & color2.blue()

                    # Set piksel pada gambar hasil
                    result_color = QColor(new_red, new_green, new_blue)
                    result_image.setPixel(x, y, result_color.rgb())

            # Tampilkan hasilnya pada label_3
            self.label_3.setPixmap(QPixmap(result_image))
            self.label_3.setScaledContents(True)
        else:
            QMessageBox.warning(
                None, "Peringatan", "Dimensi kedua gambar tidak sama, operasi AND tidak dapat dilakukan.")

    def operasi_or(self):
        # Ambil gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()

        # Ambil gambar dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        image2 = pixmap2.toImage()

        # Pastikan kedua gambar memiliki dimensi yang sama
        if image1.size() == image2.size():
            # Buat gambar hasil yang kosong dengan dimensi yang sama
            width = image1.width()
            height = image1.height()
            result_image = QImage(width, height, QImage.Format_RGB888)

            # Lakukan operasi "OR" piksel per piksel
            for x in range(width):
                for y in range(height):
                    # Dapatkan warna piksel dari kedua gambar
                    color1 = QColor(image1.pixel(x, y))
                    color2 = QColor(image2.pixel(x, y))

                    # Lakukan operasi "OR" pada komponen warna (R, G, B)
                    new_red = color1.red() | color2.red()
                    new_green = color1.green() | color2.green()
                    new_blue = color1.blue() | color2.blue()

                    # Set piksel pada gambar hasil
                    result_color = QColor(new_red, new_green, new_blue)
                    result_image.setPixel(x, y, result_color.rgb())

            # Tampilkan hasilnya pada label_3
            self.label_3.setPixmap(QPixmap(result_image))
            self.label_3.setScaledContents(True)
        else:
            QMessageBox.warning(
                None, "Peringatan", "Dimensi kedua gambar tidak sama, operasi OR tidak dapat dilakukan.")

    def operasi_xor(self):
        # Ambil gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()

        # Ambil gambar dari labelAsal2
        pixmap2 = self.labelAsal2.pixmap()
        image2 = pixmap2.toImage()

        # Pastikan kedua gambar memiliki dimensi yang sama
        if image1.size() == image2.size():
            # Buat gambar hasil yang kosong dengan dimensi yang sama
            width = image1.width()
            height = image1.height()
            result_image = QImage(width, height, QImage.Format_RGB888)

            # Lakukan operasi XOR piksel per piksel
            for x in range(width):
                for y in range(height):
                    # Dapatkan warna piksel dari kedua gambar
                    color1 = QColor(image1.pixel(x, y))
                    color2 = QColor(image2.pixel(x, y))

                    # Lakukan operasi XOR pada komponen warna (R, G, B)
                    new_red = color1.red() ^ color2.red()
                    new_green = color1.green() ^ color2.green()
                    new_blue = color1.blue() ^ color2.blue()

                    # Set piksel pada gambar hasil
                    result_color = QColor(new_red, new_green, new_blue)
                    result_image.setPixel(x, y, result_color.rgb())

            # Tampilkan hasilnya pada label_3
            self.label_3.setPixmap(QPixmap(result_image))
            self.label_3.setScaledContents(True)
        else:
            QMessageBox.warning(
                None, "Peringatan", "Dimensi kedua gambar tidak sama, operasi XOR tidak dapat dilakukan.")

    def operasi_not(self):
        # Ambil gambar dari labelAsal1
        pixmap1 = self.labelAsal1.pixmap()
        image1 = pixmap1.toImage()

        # Buat gambar hasil yang kosong dengan dimensi yang sama
        width = image1.width()
        height = image1.height()
        result_image = QImage(width, height, QImage.Format_RGB888)

        # Lakukan operasi NOT piksel per piksel pada labelAsal1
        for x in range(width):
            for y in range(height):
                # Dapatkan warna piksel dari labelAsal1
                color1 = QColor(image1.pixel(x, y))

                # Lakukan operasi NOT pada komponen warna (R, G, B)
                new_red = 255 - color1.red()
                new_green = 255 - color1.green()
                new_blue = 255 - color1.blue()

                # Set piksel pada gambar hasil
                result_color = QColor(new_red, new_green, new_blue)
                result_image.setPixel(x, y, result_color.rgb())

        # Tampilkan hasil operasi NOT pada label_3
        self.label_3.setPixmap(QPixmap(result_image))
        self.label_3.setScaledContents(True)        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1301, 635)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.gambar1 = QtWidgets.QPushButton(Dialog)
        self.gambar1.setGeometry(QtCore.QRect(20, 20, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gambar1.setFont(font)
        self.gambar1.setObjectName("gambar1")
        self.labelAsal1 = QtWidgets.QLabel(Dialog)
        self.labelAsal1.setGeometry(QtCore.QRect(20, 80, 400, 400))
        self.labelAsal1.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAsal1.setText("")
        self.labelAsal1.setObjectName("labelAsal1")
        self.labelAsal2 = QtWidgets.QLabel(Dialog)
        self.labelAsal2.setGeometry(QtCore.QRect(450, 80, 400, 400))
        self.labelAsal2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAsal2.setText("")
        self.labelAsal2.setObjectName("labelAsal2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(880, 80, 400, 400))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gambar2 = QtWidgets.QPushButton(Dialog)
        self.gambar2.setGeometry(QtCore.QRect(240, 20, 200, 40))
        self.gambar2.setObjectName("gambar2")
        self.simpan = QtWidgets.QPushButton(Dialog)
        self.simpan.setGeometry(QtCore.QRect(460, 20, 200, 40))
        self.simpan.setObjectName("simpan")
        self.penjumlahan = QtWidgets.QPushButton(Dialog)
        self.penjumlahan.setGeometry(QtCore.QRect(20, 500, 200, 40))
        self.penjumlahan.setObjectName("penjumlahan")
        self.pengurangan = QtWidgets.QPushButton(Dialog)
        self.pengurangan.setGeometry(QtCore.QRect(240, 500, 200, 40))
        self.pengurangan.setObjectName("pengurangan")
        self.pembagian = QtWidgets.QPushButton(Dialog)
        self.pembagian.setGeometry(QtCore.QRect(460, 500, 200, 40))
        self.pembagian.setObjectName("pembagian")
        self.perkalian = QtWidgets.QPushButton(Dialog)
        self.perkalian.setGeometry(QtCore.QRect(680, 500, 200, 40))
        self.perkalian.setObjectName("perkalian")
        self.And = QtWidgets.QPushButton(Dialog)
        self.And.setGeometry(QtCore.QRect(20, 560, 200, 40))
        self.And.setObjectName("And")
        self.Or = QtWidgets.QPushButton(Dialog)
        self.Or.setGeometry(QtCore.QRect(240, 560, 200, 40))
        self.Or.setObjectName("Or")
        self.Xor = QtWidgets.QPushButton(Dialog)
        self.Xor.setGeometry(QtCore.QRect(460, 560, 200, 40))
        self.Xor.setObjectName("Xor")
        self.Not = QtWidgets.QPushButton(Dialog)
        self.Not.setGeometry(QtCore.QRect(680, 560, 200, 40))
        self.Not.setObjectName("Not")

        self.gambar1.clicked.connect(self.buka_gambar1)
        self.gambar2.clicked.connect(self.buka_gambar2)
        self.penjumlahan.clicked.connect(self.operasi_penjumlahan)
        self.perkalian.clicked.connect(self.operasi_perkalian)
        self.pengurangan.clicked.connect(self.operasi_pengurangan)
        self.pembagian.clicked.connect(self.operasi_pembagian)
        self.simpan.clicked.connect(self.operasi_simpan)
        self.And.clicked.connect(self.operasi_and)
        self.Or.clicked.connect(self.operasi_or)
        self.Xor.clicked.connect(self.operasi_xor)
        self.Not.clicked.connect(self.operasi_not)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gambar1.setText(_translate("Dialog", "Gambar 1"))
        self.gambar2.setText(_translate("Dialog", "Gambar 2"))
        self.simpan.setText(_translate("Dialog", "Simpan"))
        self.penjumlahan.setText(_translate("Dialog", "Penjumlahan"))
        self.pengurangan.setText(_translate("Dialog", "Pengurangan"))
        self.pembagian.setText(_translate("Dialog", "Pembagian"))
        self.perkalian.setText(_translate("Dialog", "Perkalian"))
        self.And.setText(_translate("Dialog", "AND"))
        self.Or.setText(_translate("Dialog", "OR"))
        self.Xor.setText(_translate("Dialog", "XOR"))
        self.Not.setText(_translate("Dialog", "NOT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
