from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage, QColor, qRgb
from aritmatika import Ui_Dialog
from brightness import BrightnessDialog
from contrast import ContrastDialog

import matplotlib.pyplot as plt
import numpy as np
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def frameAritmatika(self):
        self.dialog_aritmatika = QDialog()
        self.ui_aritmatika = Ui_Dialog()
        self.ui_aritmatika.setupUi(self.dialog_aritmatika)
        self.dialog_aritmatika.show()

    def openImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if file_name:
            try:
                image = QtGui.QPixmap(file_name)
                label_width = self.label.width()
                label_height = self.label.height()
                scaled_image = image.scaled(label_width, label_height, QtCore.Qt.KeepAspectRatio)
                self.label.setPixmap(scaled_image)
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)

            except Exception as e:
             QtWidgets.QMessageBox.critical(None, "Error", f"Error opening image: {str(e)}")

    def saveAsImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(None, "Save Image As", 
                        "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            pixmap = self.label_2.pixmap()
            pixmap.save(file_name)

    def exitApplication(self):
        QtWidgets.QApplication.quit()

    def averageGrayscale(self):
        pixmap = self.label.pixmap()
        image = pixmap.toImage()
        width = image.width()
        height = image.height()
        grayscale_image = QImage(width, height, QImage.Format_RGB888)

        for y in range(height):
            for x in range(width):
                pixel_color = image.pixelColor(x, y)
                r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                gray_value = int((r + g + b) / 3)
                grayscale_color = QColor(gray_value, gray_value, gray_value)
                grayscale_image.setPixelColor(x, y, grayscale_color)

        pixmap_grayscale = QPixmap.fromImage(grayscale_image)
        self.label_2.setPixmap(pixmap_grayscale)

    def lightnessGrayscale(self):
        pixmap = self.label.pixmap()
        image = pixmap.toImage()
        width = image.width()
        height = image.height()
        grayscale_image = QImage(width, height, QImage.Format_RGB888)

        for y in range(height):
            for x in range(width):
                pixel_color = image.pixelColor(x, y)
                r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                gray_value = int((max(r, g, b) + min(r, g, b)) / 2)
                grayscale_color = QColor(gray_value, gray_value, gray_value)
                grayscale_image.setPixelColor(x, y, grayscale_color)

        pixmap_grayscale = QPixmap.fromImage(grayscale_image)
        self.label_2.setPixmap(pixmap_grayscale)

    def luminanceGrayscale(self):
        pixmap = self.label.pixmap()
        image = pixmap.toImage()
        width = image.width()
        height = image.height()
        grayscale_image = QImage(width, height, QImage.Format_RGB888)

        for y in range(height):
            for x in range(width):
                pixel_color = image.pixelColor(x, y)
                r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                grayscale_luminance = int(0.299 * r + 0.587 * g + 0.114 * b)
                grayscale_color = QColor(grayscale_luminance, grayscale_luminance, grayscale_luminance)
                grayscale_image.setPixelColor(x, y, grayscale_color)

        pixmap_grayscale = QPixmap.fromImage(grayscale_image)
        self.label_2.setPixmap(pixmap_grayscale)

    def flipHorizontal(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            flipped_pixmap = original_pixmap.transformed(QtGui.QTransform().scale(-1, 1))
            self.label_2.setPixmap(flipped_pixmap)

    def flipVertical(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            flipped_pixmap = original_pixmap.transformed(QtGui.QTransform().scale(1, -1))
            self.label_2.setPixmap(flipped_pixmap)

    def rotasi(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            rotated_pixmap = original_pixmap.transformed(QtGui.QTransform().rotate(90))
            self.label_2.setPixmap(rotated_pixmap)

    def translasi(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            delta_x, _ = QtWidgets.QInputDialog.getInt(None, "Translate Image", "Enter Delta X:")
            delta_y, _ = QtWidgets.QInputDialog.getInt(None, "Translate Image", "Enter Delta Y:")
        
        translated_pixmap = QtGui.QPixmap(original_pixmap)
        painter = QtGui.QPainter(translated_pixmap)
        painter.translate(delta_x, delta_y)
        painter.drawPixmap(0, 0, original_pixmap)
        painter.end()
        
        self.label_2.setPixmap(translated_pixmap)

    def uniformScaling(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            scale_factor, _ = QtWidgets.QInputDialog.getDouble(None, "Uniform Scaling", "Enter scaling factor:")
            if scale_factor > 0:
                scaled_pixmap = original_pixmap.scaled(original_pixmap.size() * scale_factor, QtCore.Qt.KeepAspectRatio)
                self.label_2.setPixmap(scaled_pixmap)
            else:
                QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please enter a positive scaling factor.")
    
    def nonUniformScaling(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            scale_factor_x, _ = QtWidgets.QInputDialog.getDouble(None, "Non-Uniform Scaling", "Enter X scaling factor:")
            scale_factor_y, _ = QtWidgets.QInputDialog.getDouble(None, "Non-Uniform Scaling", "Enter Y scaling factor:")
        
        if scale_factor_x > 0 and scale_factor_y > 0:
            width = int(original_pixmap.width() * scale_factor_x)
            height = int(original_pixmap.height() * scale_factor_y)
            scaled_pixmap = original_pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(scaled_pixmap)
        else:
            QtWidgets.QMessageBox.warning(None, "Invalid Input", "Please enter positive scaling factors for both X and Y.")

    def histogramEqualization(self):
        original_pixmap = self.label.pixmap()
        if original_pixmap:
            # Konversi pixmap ke QImage
            image = original_pixmap.toImage()
            width = image.width()
            height = image.height()

            grayscale_image = np.zeros((height, width), dtype=np.uint8)

            # Menghitung histogram
            histogram = [0] * 256
            for y in range(height):
                for x in range(width):
                    r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                    gray_value = int((r + g + b) / 3)
                    grayscale_image[y][x] = gray_value
                    histogram[gray_value] += 1

            # Menghitung cumulative histogram
            cumulative_histogram = [sum(histogram[:i+1]) for i in range(256)]

            # Normalisasi cumulative histogram
            max_pixel_value = width * height
            normalized_cumulative_histogram = [(cumulative_histogram[i] / max_pixel_value) * 255 for i in range(256)]

            # Menerapkan equalization pada citra
            equalized_image = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    equalized_image[y][x] = int(normalized_cumulative_histogram[grayscale_image[y][x]])

            equalized_qimage = QtGui.QImage(equalized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)
            equalized_pixmap = QtGui.QPixmap.fromImage(equalized_qimage)
            self.label_2.setPixmap(equalized_pixmap)

            # Buat histogram sebelum equalization
            plt.figure(figsize=(12, 6))
            plt.subplot(121)
            plt.hist(np.array(grayscale_image).ravel(), bins=256, range=(0, 256), density=True, color='b', alpha=0.6)
            plt.title('Histogram Sebelum Equalization')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')

            # Buat histogram sesudah equalization
            plt.subplot(122)
            equalized_image_flat = np.array(equalized_image).ravel()
            plt.hist(equalized_image_flat, bins=256, range=(0, 256), density=True, color='r', alpha=0.6)
            plt.title('Histogram Sesudah Equalization')
            plt.xlabel('Nilai Pixel')
            plt.ylabel('Frekuensi Relatif')

            plt.tight_layout()
            plt.show()

    def fuzzyHERGB(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

        equalized_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

        # Menghitung histogram untuk setiap saluran warna
        histograms = [np.zeros(256, dtype=int) for _ in range(3)]
        cumulative_histograms = [np.zeros(256, dtype=int) for _ in range(3)]

        for y in range(height):
            for x in range(width):
                r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                histograms[0][r] += 1
                histograms[1][g] += 1
                histograms[2][b] += 1

        # Menghitung cumulative histogram untuk setiap saluran warna
        for i in range(3):
            cumulative_histograms[i][0] = histograms[i][0]
            for j in range(1, 256):
                cumulative_histograms[i][j] = cumulative_histograms[i][j - 1] + histograms[i][j]

        # Normalisasi cumulative histogram
        max_pixel_value = width * height
        normalized_cumulative_histograms = [cumulative_histograms[i] / max_pixel_value * 255 for i in range(3)]

        # Menerapkan fuzzy equalization pada citra
        for y in range(height):
            for x in range(width):
                r, g, b, _ = QtGui.QColor(image.pixel(x, y)).getRgb()
                new_r = int(normalized_cumulative_histograms[0][r])
                new_g = int(normalized_cumulative_histograms[1][g])
                new_b = int(normalized_cumulative_histograms[2][b])
                equalized_image.setPixel(x, y, QtGui.qRgb(new_r, new_g, new_b))

        equalized_pixmap = QtGui.QPixmap.fromImage(equalized_image)
        self.label_2.setPixmap(equalized_pixmap)

        # Buat histogram sebelum fuzzy equalization
        plt.figure(figsize=(12, 6))
        plt.subplot(121)
        for i, color in enumerate(['r', 'g', 'b']):
            plt.hist(np.array([QtGui.QColor(image.pixel(x, y)).getRgb()[i] for x in range(width) for y in range(height)]),
                     bins=256, range=(0, 256), density=True, color=color, alpha=0.6, label=color.upper())
        plt.title('Histogram Sebelum Fuzzy Equalization')
        plt.xlabel('Nilai Pixel')
        plt.ylabel('Frekuensi Relatif')
        plt.legend()

        # Buat histogram sesudah fuzzy equalization
        plt.subplot(122)
        for i, color in enumerate(['r', 'g', 'b']):
            plt.hist(np.array([QtGui.QColor(equalized_image.pixel(x, y)).getRgb()[i] for x in range(width) for y in range(height)]),
                     bins=256, range=(0, 256), density=True, color=color, alpha=0.6, label=color.upper())
        plt.title('Histogram Sesudah Fuzzy Equalization')
        plt.xlabel('Nilai Pixel')
        plt.ylabel('Frekuensi Relatif')
        plt.legend()

        plt.tight_layout()
        plt.show()

    def fuzzyGreyscale(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

        grayscale_image = np.zeros((height, width), dtype=np.uint8)

        # Menghitung histogram
        histogram = [0] * 256
        for y in range(height):
            for x in range(width):
                pixel_value = QtGui.qGray(image.pixel(x, y))
                grayscale_image[y][x] = pixel_value
                histogram[pixel_value] += 1

        # Menghitung cumulative histogram
        cumulative_histogram = [sum(histogram[:i+1]) for i in range(256)]

        # Normalisasi cumulative histogram
        max_pixel_value = width * height
        normalized_cumulative_histogram = [(cumulative_histogram[i] / max_pixel_value) * 255 for i in range(256)]

        # Menerapkan fuzzy equalization pada citra grayscale
        fuzzy_equalized_image = np.zeros((height, width), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                fuzzy_equalized_image[y][x] = int(normalized_cumulative_histogram[grayscale_image[y][x]])

        fuzzy_equalized_qimage = QtGui.QImage(fuzzy_equalized_image.data, width, height, width, QtGui.QImage.Format_Grayscale8)
        fuzzy_equalized_pixmap = QtGui.QPixmap.fromImage(fuzzy_equalized_qimage)
        self.label_2.setPixmap(fuzzy_equalized_pixmap)

        # Buat histogram sebelum fuzzy equalization
        plt.figure(figsize=(12, 6))
        plt.subplot(121)
        plt.hist(np.array(grayscale_image).ravel(), bins=256, range=(0, 256), density=True, color='b', alpha=0.6)
        plt.title('Histogram Sebelum Fuzzy Equalization')
        plt.xlabel('Nilai Pixel')
        plt.ylabel('Frekuensi Relatif')

        # Buat histogram sesudah fuzzy equalization
        plt.subplot(122)
        fuzzy_equalized_image_flat = np.array(fuzzy_equalized_image).ravel()
        plt.hist(fuzzy_equalized_image_flat, bins=256, range=(0, 256), density=True, color='r', alpha=0.6)
        plt.title('Histogram Sesudah Fuzzy Equalization')
        plt.xlabel('Nilai Pixel')
        plt.ylabel('Frekuensi Relatif')

        plt.tight_layout()
        plt.show()

    def invers(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            inverted_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel = QtGui.QColor(image.pixel(x, y))
                    inverted_color = QtGui.QColor(255 - pixel.red(), 255 - pixel.green(), 255 - pixel.blue(), pixel.alpha())
                    inverted_image.setPixel(x, y, inverted_color.rgba())

            inverted_pixmap = QtGui.QPixmap.fromImage(inverted_image)
            self.label_2.setPixmap(inverted_pixmap)

    def histogramInput(self):
        file_name = self.label.pixmap()
        
        if file_name:
            image = QtGui.QImage(file_name)
            if not image.isNull():
               
                image_np = self.qimage_to_ndarray(image)
                plt.figure()
                plt.hist(image_np.ravel(), bins=256, range=(0, 256), density=True, color='red', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar')
                plt.show()

    def histogramOutput(self):
        file_name = self.label_2.pixmap()
        
        if file_name:
            image = QtGui.QImage(file_name)
            if not image.isNull():
               
                image_np = self.qimage_to_ndarray(image)
                plt.figure()
                plt.hist(image_np.ravel(), bins=256, range=(0, 256), density=True, color='green', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar')
                plt.show()

    def histogramInputOutput(self):
        file_name = self.label.pixmap()
        file_name2 = self.label_2.pixmap()
        
        if file_name and file_name2:
            image = QtGui.QImage(file_name)
            image2 = QtGui.QImage(file_name2)

            if image  and image is not None :
               
                image_np = self.qimage_to_ndarray(image)
                image_np2 = self.qimage_to_ndarray(image2)
                plt.figure()
                plt.hist(image_np.ravel(), bins=256, range=(0, 256), density=True, color='red', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar')

                plt.figure()
                plt.hist(image_np2.ravel(), bins=256, range=(0, 256), density=True, color='blue', alpha=0.7)
                plt.xlabel('Pixel Value')
                plt.ylabel('Normalized Frequency')
                plt.title('Histogram Gambar')
                plt.show()

    def qimage_to_ndarray(self, qimage):
        """
        Konversi QImage ke larik NumPy.
        """
        width = qimage.width()
        height = qimage.height()

        ptr = qimage.bits()
        ptr.setsize(height * width * 4)
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))

        # Mengabaikan channel alpha (RGBA), jika ada
        if arr.shape[2] == 4:
            arr = arr[:, :, :3]

        print(arr)    

        return arr
    
    def cropImg(self, x,y,lebar,tinggi):
        pixmap = self.label.pixmap()

        if pixmap:
           img = pixmap.toImage()
           

           crop_img = img.copy(x, y, lebar, tinggi)

           img_pixmap = QPixmap.fromImage(crop_img)

           self.label_2.setPixmap(img_pixmap)
           self.displayed_pixmap = img_pixmap
    
    def cropping(self):
        
        posisiX, ok = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan posisi x :", 0, 0, 500)
        posisiY, ok2 = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan posisi y :", 0, 0, 500)
        cropLebar, ok4 = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan nilai crop lebar gambar:", 0, 0, 1000)
        cropTinggi, ok3 = QtWidgets.QInputDialog.getInt(None, "Croping Image", "Masukan nilai crop tinggi gambar :", 0, 0, 1000)

        if ok and ok2 and ok3 and ok4:
            self.cropImg(posisiX,posisiY,cropLebar,cropTinggi)
    
    #To do merubah gambar menjadi 7 bit
    def eksekusi_7bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 7 bit (128 warna)
            bw_image = QImage(width, height, QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Kurangi setiap kanal warna ke dalam 7 bit (0-127)
                    r = (r * 127) // 255
                    g = (g * 127) // 255
                    b = (b * 127) // 255

                    # Set warna pada gambar 7 bit
                    bw_color = QColor(r * 255 // 127, g * 255 // 127, b * 255 // 127)
                    bw_image.setPixelColor(x, y, bw_color)

            # Tampilkan gambar 7 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)

    #To do merubah gambar menjadi 6 bit
    def eksekusi_6bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 6 bit (64 warna)
            bw_image = QImage(width, height, QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Kurangi setiap kanal warna ke dalam 6 bit (0-63)
                    r = (r * 63) // 255
                    g = (g * 63) // 255
                    b = (b * 63) // 255

                    # Set warna pada gambar 6 bit
                    bw_color = QColor(r * 255 // 63, g * 255 // 63, b * 255 // 63)
                    bw_image.setPixelColor(x, y, bw_color)

            # Tampilkan gambar 6 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)

    #To do merubah gambar menjadi 5 bit
    def eksekusi_5bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 5 bit (32 warna)
            bw_image = QImage(width, height, QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Kurangi setiap kanal warna ke dalam 5 bit (0-31)
                    r = (r * 31) // 255
                    g = (g * 31) // 255
                    b = (b * 31) // 255

                    # Set warna pada gambar 5 bit
                    bw_color = QColor(r * 255 // 31, g * 255 // 31, b * 255 // 31)
                    bw_image.setPixelColor(x, y, bw_color)

            # Tampilkan gambar 5 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)

    #To do merubah gambar menjadi 4 bit
    def eksekusi_4bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 4 bit (16 warna)
            bw_image = QImage(width, height, QImage.Format_Indexed8)

            # Atur palet warna (16 warna)
            for i in range(16):
                gray_value = i * 16
                bw_image.setColor(i, QColor(gray_value, gray_value, gray_value).rgb())

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = QColor(image.pixel(x, y))
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Tentukan warna pada gambar 4 bit berdasarkan warna asli
                    bw_index = int((r + g + b) / 48)  # 16-level grayscale

                    # Set indeks warna pada gambar 4 bit
                    bw_image.setPixel(x, y, bw_index)

            # Tampilkan gambar 4 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)
    #To do merubah gambar menjadi 3 bit

    def eksekusi_3bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 3 bit (8 warna)
            bw_image = QImage(width, height, QImage.Format_Indexed8)

            # Atur palet warna
            bw_image.setColor(0, QColor(0, 0, 0).rgb())   # Hitam
            bw_image.setColor(1, QColor(85, 85, 85).rgb()) # Abu-abu muda
            bw_image.setColor(2, QColor(170, 170, 170).rgb()) # Abu-abu tua
            bw_image.setColor(3, QColor(255, 0, 0).rgb()) # Merah
            bw_image.setColor(4, QColor(0, 255, 0).rgb()) # Hijau
            bw_image.setColor(5, QColor(0, 0, 255).rgb()) # Biru
            bw_image.setColor(6, QColor(255, 255, 0).rgb()) # Kuning
            bw_image.setColor(7, QColor(255, 0, 255).rgb()) # Ungu

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = QColor(image.pixel(x, y))
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Tentukan warna pada gambar 3 bit berdasarkan warna asli
                    if r < 64:
                        bw_index = 0  # Hitam
                    elif r < 128:
                        bw_index = 1  # Abu-abu muda
                    elif r < 192:
                        bw_index = 2  # Abu-abu tua
                    elif g < 64:
                        bw_index = 3  # Merah
                    elif g < 128:
                        bw_index = 4  # Hijau
                    elif g < 192:
                        bw_index = 5  # Biru
                    elif b < 128:
                        bw_index = 6  # Kuning
                    else:
                        bw_index = 7  # Ungu

                    # Set indeks warna pada gambar 3 bit
                    bw_image.setPixel(x, y, bw_index)

            # Tampilkan gambar 3 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)

    #To do merubah gambar menjadi 2 bit
    def eksekusi_2bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 2 bit (4 warna)
            bw_image = QImage(width, height, QImage.Format_Indexed8)

            # Atur palet warna
            bw_image.setColor(0, QColor(0, 0, 0).rgb())   # Hitam
            bw_image.setColor(1, QColor(85, 85, 85).rgb()) # Abu-abu muda
            bw_image.setColor(2, QColor(170, 170, 170).rgb()) # Abu-abu tua
            bw_image.setColor(3, QColor(255, 255, 255).rgb()) # Putih

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = QColor(image.pixel(x, y))
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Tentukan warna pada gambar 2 bit berdasarkan warna asli
                    if r < 128 and g < 128 and b < 128:
                        bw_index = 0  # Hitam
                    elif r < 192 and g < 192 and b < 192:
                        bw_index = 1  # Abu-abu muda
                    elif r < 224 and g < 224 and b < 224:
                        bw_index = 2  # Abu-abu tua
                    else:
                        bw_index = 3  # Putih

                    # Set indeks warna pada gambar 2 bit
                    bw_image.setPixel(x, y, bw_index)

            # Tampilkan gambar 2 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)

    #To do ubah gambar ke 1 bit
    def eksekusi_1bit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            # Buat gambar 1 bit (hitam-putih)
            bw_image = QImage(width, height, QImage.Format_Mono)

            for y in range(height):
                for x in range(width):
                    # Dapatkan warna asli pada posisi piksel (x, y)
                    pixel_color = QColor(image.pixel(x, y))
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Konversi warna ke hitam (0) atau putih (1)
                    gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
                    bw_index = 0 if gray_value < 128 else 1

                    # Set indeks warna pada gambar 1 bit
                    bw_image.setPixel(x, y, bw_index)

            # Tampilkan gambar 1 bit di label_2
            pixmap_bw = QPixmap.fromImage(bw_image)
            self.label_2.setPixmap(pixmap_bw)

    def threshold(self):
        pixmap = self.label.pixmap()
        image = pixmap.toImage().convertToFormat(QImage.Format_ARGB32)
        
        # Mendapatkan dimensi gambar
        width = image.width()
        height = image.height()
        
        # Buat gambar untuk menyimpan hasil thresholding
        threshold_image = QImage(width, height, QImage.Format_ARGB32)
        
        threshold_value = 127  # Kamu bisa mengubah ini sesuai kebutuhan
        
        for y in range(height):
            for x in range(width):
                # Dapatkan warna asli pada posisi piksel (x, y)
                pixel_color = QColor.fromRgba(image.pixel(x, y))
                r, g, b, a = pixel_color.red(), pixel_color.green(), pixel_color.blue(), pixel_color.alpha()
                
                # Menghitung nilai grayscale menggunakan metode Luminance
                gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
                
                # Menerapkan threshold
                if gray_value >= threshold_value:
                    new_value = 255
                else:
                    new_value = 0
                    
                threshold_color = QColor(new_value, new_value, new_value, a)
                
                # Set warna threshold pada gambar threshold
                threshold_image.setPixelColor(x, y, threshold_color)
        
        # Tampilkan gambar threshold di label_2
        pixmap_threshold = QPixmap.fromImage(threshold_image)
        self.label_2.setPixmap(pixmap_threshold)

    def segmentasi_citra(self):     
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    gx = 0
                    gy = 0

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            pixel_color = QtGui.QColor(input_qimage.pixel(x + dx, y + dy))
                            intensity = pixel_color.red()  # Using red channel for grayscale
                        
                            if dx == -1:
                                gx -= intensity
                            elif dx == 1:
                                gx += intensity
                            if dy == -1:
                                gy -= intensity
                            elif dy == 1:
                                gy += intensity

                    edge_intensity = min(int(abs(gx) + abs(gy)), 255)
                    output_qimage.setPixelColor(x, y, QtGui.QColor(edge_intensity, edge_intensity, edge_intensity))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)

    def highpass(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()
        img_np = np.zeros((height, width, 4), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()
                img_np[y, x, 3] = pixel_color.alpha()

        # Buat kernel High Pass Filter
        kernel = np.array([[-1, -1, -1],
                           [-1,  8, -1],
                           [-1, -1, -1]])

        # Pisahkan saluran warna
        blue_channel, green_channel, red_channel, alpha_channel = cv2.split(
            img_np)

        # Proses High Pass Filter pada setiap saluran warna RGB
        for channel in (blue_channel, green_channel, red_channel):
            filtered_channel = cv2.filter2D(channel, -1, kernel)
            channel[:] = filtered_channel

        # Gabungkan kembali saluran warna
        img_filtered = cv2.merge(
            [blue_channel, green_channel, red_channel, alpha_channel])

        img_filtered_qimage = QImage(
            img_filtered.data, width, height, img_filtered.strides[0], QImage.Format_ARGB32)
        pixmap_filtered = QPixmap.fromImage(img_filtered_qimage)

        self.label_2.setPixmap(pixmap_filtered)    

    def lowpass(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Terapkan filter low pass (average) 3x3
        kernel = np.ones((3, 3), dtype=np.float32) / 9.0
        img_filtered = cv2.filter2D(img_np, -1, kernel)

        # Konversi hasil filter kembali ke QImage
        img_filtered_qimage = QImage(
            img_filtered.data, width, height, img_filtered.strides[0], QImage.Format_RGB888)

        # Tampilkan gambar hasil filter di label_2
        pixmap_filtered = QPixmap.fromImage(img_filtered_qimage)
        self.label_2.setPixmap(pixmap_filtered)

    def unsharp_masking(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()
        img_np = np.zeros((height, width, 4), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()
                img_np[y, x, 3] = pixel_color.alpha()

        alpha = 1.5  # Sesuaikan alpha sesuai kebutuhan
        sigma = 2.0  # Sesuaikan sigma sesuai kebutuhan

        # Pisahkan saluran warna
        blue_channel, green_channel, red_channel, alpha_channel = cv2.split(
            img_np)

        # Proses unsharp masking pada setiap saluran warna RGB
        for channel in (blue_channel, green_channel, red_channel):
            blurred_image = cv2.GaussianBlur(channel, (0, 0), sigma)
            sharpened_image = cv2.addWeighted(
                channel, alpha + 1.0, blurred_image, -alpha, 0)
            channel[:] = cv2.addWeighted(
                channel, 1.0, sharpened_image, -0.5, 0)

        # Gabungkan kembali saluran warna
        img_filtered = cv2.merge(
            [blue_channel, green_channel, red_channel, alpha_channel])

        img_filtered_qimage = QImage(
            img_filtered.data, width, height, img_filtered.strides[0], QImage.Format_ARGB32)
        pixmap_filtered = QPixmap.fromImage(img_filtered_qimage)

        self.label_2.setPixmap(pixmap_filtered)

    def sharpen(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Kernel untuk efek sharpen
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]], dtype=np.float32)

        # Terapkan filter sharpen
        img_sharpened = cv2.filter2D(img_np, -1, kernel)

        # Konversi hasil filter kembali ke QImage
        img_sharpened_qimage = QImage(
            img_sharpened.data, width, height, img_sharpened.strides[0], QImage.Format_RGB888)

        # Tampilkan gambar hasil filter di label_2
        pixmap_sharpened = QPixmap.fromImage(img_sharpened_qimage)
        self.label_2.setPixmap(pixmap_sharpened)

    def gaussian_blur_3x3(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Terapkan filter Gaussian 3x3
        img_gaussian = cv2.GaussianBlur(img_np, (3, 3), 0)

        # Konversi hasil filter kembali ke QImage
        img_gaussian_qimage = QImage(
            img_gaussian.data, width, height, img_gaussian.strides[0], QImage.Format_RGB888)

        # Tampilkan gambar hasil filter di label_2
        pixmap_gaussian = QPixmap.fromImage(img_gaussian_qimage)
        self.label_2.setPixmap(pixmap_gaussian)

    def gaussian_blur_5x5(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Terapkan low pass filter (Gaussian blur)
        img_blur = cv2.GaussianBlur(img_np, (5, 5), 0)

        # Konversi hasil filter kembali ke QImage
        img_blur_qimage = QImage(
            img_blur.data, width, height, img_blur.strides[0], QImage.Format_RGB888)

        # Tampilkan gambar hasil filter di label_2
        pixmap_blur = QPixmap.fromImage(img_blur_qimage)
        self.label_2.setPixmap(pixmap_blur)

    def identity(self):
        pixmap = self.label.pixmap()
        if pixmap:
            self.label_2.setPixmap(pixmap)

    def robert(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Terapkan filter Robert untuk deteksi tepi
        kernel_x = np.array([[-1, 0],
                             [0, 1]], dtype=np.float32)
        
        kernel_y = np.array([[0, -1],
                             [1, 0]], dtype=np.float32)

        img_x = cv2.filter2D(img_np, -1, kernel_x)
        img_y = cv2.filter2D(img_np, -1, kernel_y)
        
        # Menggabungkan hasil deteksi tepi dari kedua kernel
        img_edge = cv2.add(np.abs(img_x), np.abs(img_y))

        # Konversi hasil deteksi tepi kembali ke QImage
        img_edge_qimage = QImage(img_edge.data, width, height, img_edge.strides[0], QImage.Format_RGB888)

        # Tampilkan gambar hasil deteksi tepi di label_2
        pixmap_edge = QPixmap.fromImage(img_edge_qimage)
        self.label_2.setPixmap(pixmap_edge)
    
    # todo gambar to sobel 
    def sobel(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Terapkan filter Sobel untuk deteksi tepi
        img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        img_sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=3)
        img_sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=3)
        img_sobel_x = cv2.convertScaleAbs(img_sobel_x)
        img_sobel_y = cv2.convertScaleAbs(img_sobel_y)
        img_edge = cv2.addWeighted(img_sobel_x, 1, img_sobel_y, 1, 0)

        # Konversi hasil deteksi tepi kembali ke QImage
        img_edge_qimage = QImage(img_edge.data, width, height, img_edge.strides[0], QImage.Format_Grayscale8)

        # Tampilkan gambar hasil deteksi tepi di label_2
        pixmap_edge = QPixmap.fromImage(img_edge_qimage)
        self.label_2.setPixmap(pixmap_edge)
    
    # todo gambar to prewit
    def prewit(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
        width = image.width()
        height = image.height()

        # Konversi gambar menjadi format NumPy
        img_np = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            for x in range(width):
                pixel_color = QColor(image.pixel(x, y))
                img_np[y, x, 0] = pixel_color.red()
                img_np[y, x, 1] = pixel_color.green()
                img_np[y, x, 2] = pixel_color.blue()

        # Terapkan filter Prewitt untuk deteksi tepi
        img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        kernel_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]], dtype=np.float32)

        kernel_y = np.array([[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]], dtype=np.float32)

        img_prewitt_x = cv2.filter2D(img_gray, -1, kernel_x)
        img_prewitt_y = cv2.filter2D(img_gray, -1, kernel_y)
        img_edge = cv2.addWeighted(np.abs(img_prewitt_x), 1, np.abs(img_prewitt_y), 1, 0)

        # Konversi hasil deteksi tepi kembali ke QImage
        img_edge_qimage = QImage(img_edge.astype(np.uint8), width, height, img_edge.strides[0], QImage.Format_Grayscale8)

        # Tampilkan gambar hasil deteksi tepi di label_2
        pixmap_edge = QPixmap.fromImage(img_edge_qimage)
        self.label_2.setPixmap(pixmap_edge)

    def roi(self):
        # Load the input image using PyQt5
        input_image = self.label.pixmap().toImage()

        # Get the width and height of the image
        width = input_image.width()
        height = input_image.height()

        # Create a QImage for the output image
        output_image = QImage(width, height, QImage.Format_RGB888)

        # Get the coordinates of the ROI (e.g., defined by the user)
        # For example, let's assume the ROI is a rectangle with coordinates (x1, y1) and (x2, y2)
        x1 = 100
        y1 = 100
        x2 = 200
        y2 = 200

        # Iterate through pixels and copy the ROI to the output image
        for y in range(y1, y2):
            for x in range(x1, x2):
                pixel_color = input_image.pixelColor(x, y)
                output_image.setPixelColor(x, y, pixel_color)

        # Convert the output image to a pixmap for display
        output_pixmap = QPixmap.fromImage(output_image)

        # Display the ROI
        self.label_2.setPixmap(output_pixmap)
        self.displayed_pixmap = output_pixmap  

    def applyErosionSquare3(self):
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the 3x3 neighborhood
                pixels = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Perform erosion by finding the minimum value in the neighborhood
                min_value = min(pixels)

                # Set the pixel in the output image to the minimum value
                output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.displayed_pixmap = output_pixmap    

    def applyErosionSquare5(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(2, height - 2):
            for x in range(2, width - 2):
                # Get the pixel values of the 5x5 neighborhood
                pixels = []
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Perform erosion by finding the minimum value in the neighborhood
                min_value = min(pixels)

                # Set the pixel in the output image to the minimum value
                output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.label_2.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyErosionCross3(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the cross-shaped neighborhood
                pixel_values = [
                    QColor(img.pixel(x, y - 1)).red(),
                    QColor(img.pixel(x, y + 1)).red(),
                    QColor(img.pixel(x - 1, y)).red(),
                    QColor(img.pixel(x + 1, y)).red(),
                    QColor(img.pixel(x, y)).red()
                ]

                # Perform erosion by finding the minimum value in the neighborhood
                min_value = min(pixel_values)

                # Set the pixel in the output image to the minimum value
                output_image.setPixel(x, y, qRgb(min_value, min_value, min_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.label_2.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyDilationSquare3(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the 3x3 neighborhood
                pixel_values = [
                    QColor(img.pixel(x - 1, y - 1)).red(),
                    QColor(img.pixel(x, y - 1)).red(),
                    QColor(img.pixel(x + 1, y - 1)).red(),
                    QColor(img.pixel(x - 1, y)).red(),
                    QColor(img.pixel(x, y)).red(),
                    QColor(img.pixel(x + 1, y)).red(),
                    QColor(img.pixel(x - 1, y + 1)).red(),
                    QColor(img.pixel(x, y + 1)).red(),
                    QColor(img.pixel(x + 1, y + 1)).red()
                ]

                # Perform dilation by finding the maximum value in the neighborhood
                max_value = max(pixel_values)

                # Set the pixel in the output image to the maximum value
                output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.label_2.setScaledContents(True)
        self.displayed_pixmap = output_pixmap

    def applyDilationSquare5(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(2, height - 2):
            for x in range(2, width - 2):
                # Get the pixel values of the 5x5 neighborhood
                pixel_values = []
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        pixel = img.pixel(x + i, y + j)
                        pixel_values.append(QColor(pixel).red())

                # Perform dilation by finding the maximum value in the neighborhood
                max_value = max(pixel_values)

                # Set the pixel in the output image to the maximum value
                output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.label_2.setScaledContents(True)
        self.displayed_pixmap = output_pixmap

    def applyDilationCross3(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Get the pixel values of the cross-shaped neighborhood
                pixel_values = [
                    QColor(img.pixel(x, y - 1)).red(),
                    QColor(img.pixel(x, y + 1)).red(),
                    QColor(img.pixel(x - 1, y)).red(),
                    QColor(img.pixel(x + 1, y)).red(),
                    QColor(img.pixel(x, y)).red()
                ]

                # Perform dilation by finding the maximum value in the neighborhood
                max_value = max(pixel_values)

                # Set the pixel in the output image to the maximum value
                output_image.setPixel(x, y, qRgb(max_value, max_value, max_value))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.label_2.setScaledContents(True)
        self.displayed_pixmap = output_pixmap
        
    def applyOpeningSquare9(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        # Define the structuring element size (9x9)
        structuring_element_size = 9

        # Calculate the padding size
        padding_size = structuring_element_size // 2

        for y in range(padding_size, height - padding_size):
            for x in range(padding_size, width - padding_size):
                # Get the pixel values of the 9x9 neighborhood
                pixels = []
                for i in range(-padding_size, padding_size + 1):
                    for j in range(-padding_size, padding_size + 1):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Check if all pixels in the neighborhood are white (255)
                if all(pixel == 255 for pixel in pixels):
                    # If all pixels are white, set the central pixel to white
                    output_image.setPixel(x, y, qRgb(255, 255, 255))
                else:
                    # Otherwise, set the central pixel to black
                    output_image.setPixel(x, y, qRgb(0, 0, 0))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.displayed_pixmap = output_pixmap
        
    def applyClosingSquare9(self):
        # Get the input image
        img = self.label.pixmap().toImage()

        width, height = img.width(), img.height()

        # Create an output image with the same size
        output_image = QImage(width, height, QImage.Format_RGB32)

        # Define the structuring element size (9x9)
        structuring_element_size = 9

        # Calculate the padding size
        padding_size = structuring_element_size // 2

        for y in range(padding_size, height - padding_size):
            for x in range(padding_size, width - padding_size):
                # Get the pixel values of the 9x9 neighborhood
                pixels = []
                for i in range(-padding_size, padding_size + 1):
                    for j in range(-padding_size, padding_size + 1):
                        pixel = img.pixel(x + i, y + j)
                        pixels.append(QColor(pixel).red())

                # Check if all pixels in the neighborhood are black (0)
                if all(pixel == 0 for pixel in pixels):
                    # If all pixels are black, set the central pixel to black
                    output_image.setPixel(x, y, qRgb(0, 0, 0))
                else:
                    # Otherwise, set the central pixel to white
                    output_image.setPixel(x, y, qRgb(255, 255, 255))

        output_pixmap = QPixmap.fromImage(output_image)
        self.label_2.setPixmap(output_pixmap)
        self.displayed_pixmap = output_pixmap  

    def applyRGBtoHSV(self):
         # Load the input image using PyQt5
        input_image = self.label.pixmap().toImage()

        # Get the width and height of the image
        width = input_image.width()
        height = input_image.height()

        # Create a QImage for the output HSV image
        output_image = QImage(width, height, QImage.Format_RGB888)

        # Perform RGB to HSV conversion by iterating through pixels
        for y in range(height):
            for x in range(width):
                pixel_color = input_image.pixelColor(x, y)
                r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()
                r, g, b = r / 255.0, g / 255.0, b / 255.0

                cmax = max(r, g, b)
                cmin = min(r, g, b)
                delta = cmax - cmin

                # Calculate hue (H)
                if delta == 0:
                    h = 0
                elif cmax == r:
                    h = 60 * (((g - b) / delta) % 6)
                elif cmax == g:
                    h = 60 * (((b - r) / delta) + 2)
                elif cmax == b:
                    h = 60 * (((r - g) / delta) + 4)

                # Calculate saturation (S)
                if cmax == 0:
                    s = 0
                else:
                    s = delta / cmax

                # Calculate value (V)
                v = cmax

                # Normalize hue to be in the range [0, 360]
                h = (h + 360) % 360

                # Normalize saturation and value to be in the range [0, 255]
                s = int(s * 255)
                v = int(v * 255)

                # Set the pixel color in the output image
                output_image.setPixel(x, y, QColor.fromHsv(int(h), int(s), int(v)).rgb())

            output_pixmap = QPixmap.fromImage(output_image)
            self.label_2.setPixmap(output_pixmap)
            self.label_2.setScaledContents(True)
            self.displayed_pixmap = output_pixmap
    
    def applyColorRGBtoYCrCb(self):
        # Load the input image using PyQt5
        input_pixmap = self.label.pixmap()
        if input_pixmap is not None and not input_pixmap.isNull():
            input_image = input_pixmap.toImage()

            # Get the width and height of the image
            width = input_image.width()
            height = input_image.height()

            # Create a QImage for the output YCrCb image
            output_image = QImage(width, height, QImage.Format_RGB32)  # Change format to RGB32

            for y in range(height):
                for x in range(width):
                    pixel_color = input_image.pixelColor(x, y)
                    r, g, b = pixel_color.red(), pixel_color.green(), pixel_color.blue()

                    # Calculate Y, Cr, and Cb components
                    y_val = int(0.299 * r + 0.587 * g + 0.114 * b)
                    cr_val = int(128 + 0.5 * r - 0.41869 * g - 0.08131 * b)
                    cb_val = int(128 - 0.16874 * r - 0.33126 * g + 0.5 * b)

                    # Ensure values are within valid range
                    y_val = min(max(y_val, 0), 255)
                    cr_val = min(max(cr_val, 0), 255)
                    cb_val = min(max(cb_val, 0), 255)

                    # Set the pixel color in the output image
                    output_image.setPixel(x, y, qRgb(y_val, cr_val, cb_val))  # Use qRgb instead

            output_pixmap = QPixmap.fromImage(output_image)
            self.label_2.setPixmap(output_pixmap)
            self.label_2.setScaledContents(True)
            self.displayed_pixmap = output_pixmap
        else:
            pass    

    def brightness(self):
        if self.label.pixmap() is not None:
            self.brightnes_dialog = BrightnessDialog(main_window=self)
            self.brightnes_dialog.exec_()
        else:
            QMessageBox.warning(
                MainWindow, "Peringatan", "Tidak ada gambar yang dibuka.")
            
    def contrast(self):
        if self.label.pixmap() is not None:
            self.contrast_dialog = ContrastDialog(main_window=self)
            self.contrast_dialog.exec_()
        else:
            QMessageBox.warning(
                MainWindow, "Peringatan", "Tidak ada gambar yang dibuka.")
            
    # def remove_bg(self):
    #     if self.label.pixmap() is not None:
    #         input_pixmap = self.label.pixmap()
    #         input_pixmap.save("temp_input.png")

    #         with open("temp_input.png", "rb") as input_file:
    #             output_data = remove(input_file.read())
    #             with open("temp_output.png", "wb") as output_file:
    #                 output_file.write(output_data)

    #         output_pixmap = QPixmap("temp_output.png")
    #         self.label_2.setPixmap(output_pixmap)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1062, 592)
        self.brightness_dialog=None
        self.contrast_dialog=None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 500, 500))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 20, 500, 500))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1062, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuAritmatika = QtWidgets.QMenu(self.menubar)
        self.menuAritmatika.setObjectName("menuAritmatika")
        self.menuGeometri = QtWidgets.QMenu(self.menubar)
        self.menuGeometri.setObjectName("menuGeometri")
        self.menuScaling = QtWidgets.QMenu(self.menuGeometri)
        self.menuScaling.setObjectName("menuScaling")
        self.menuFlipping = QtWidgets.QMenu(self.menuGeometri)
        self.menuFlipping.setObjectName("menuFlipping")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuColors = QtWidgets.QMenu(self.menubar)
        self.menuColors.setObjectName("menuColors")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuColors)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuColors)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        self.menuImage_Prossesing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Prossesing.setObjectName("menuImage_Prossesing")
        self.menuKonvolusi = QtWidgets.QMenu(self.menubar)
        self.menuKonvolusi.setObjectName("menuKonvolusi")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menuKonvolusi)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuSegmentasi_Citra = QtWidgets.QMenu(self.menubar)
        self.menuSegmentasi_Citra.setObjectName("menuSegmentasi_Citra")
        self.menuBackground_Removal = QtWidgets.QMenu(self.menubar)
        self.menuBackground_Removal.setObjectName("menuBackground_Removal")
        self.menuROI = QtWidgets.QMenu(self.menubar)
        self.menuROI.setObjectName("menuROI")
        self.menuMorfologi = QtWidgets.QMenu(self.menubar)
        self.menuMorfologi.setObjectName("menuMorfologi")
        self.menuDilasi = QtWidgets.QMenu(self.menuMorfologi)
        self.menuDilasi.setObjectName("menuDilasi")
        self.menuErosi = QtWidgets.QMenu(self.menuMorfologi)
        self.menuErosi.setObjectName("menuErosi")
        self.menuOpening = QtWidgets.QMenu(self.menuMorfologi)
        self.menuOpening.setObjectName("menuOpening")
        self.menuClosing = QtWidgets.QMenu(self.menuMorfologi)
        self.menuClosing.setObjectName("menuClosing")
        self.menuEkstraksi_Fitur = QtWidgets.QMenu(self.menubar)
        self.menuEkstraksi_Fitur.setObjectName("menuEkstraksi_Fitur")
        self.menuWarna = QtWidgets.QMenu(self.menuEkstraksi_Fitur)
        self.menuWarna.setObjectName("menuWarna")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openImage)

        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveAsImage)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exitApplication)

        self.actionUniform_Scaling = QtWidgets.QAction(MainWindow)
        self.actionUniform_Scaling.setObjectName("actionUniform_Scaling")
        self.actionUniform_Scaling.triggered.connect(self.uniformScaling)

        self.actionNon_Uniform_Scaling = QtWidgets.QAction(MainWindow)
        self.actionNon_Uniform_Scaling.setObjectName("actionNon_Uniform_Scaling")
        self.actionNon_Uniform_Scaling.triggered.connect(self.nonUniformScaling)

        self.actionCroping = QtWidgets.QAction(MainWindow)
        self.actionCroping.setObjectName("actionCroping")
        self.actionCroping.triggered.connect(self.cropping)

        self.actionHorizontal = QtWidgets.QAction(MainWindow)
        self.actionHorizontal.setObjectName("actionHorizontal")
        self.actionHorizontal.triggered.connect(self.flipHorizontal)

        self.actionVertical = QtWidgets.QAction(MainWindow)
        self.actionVertical.setObjectName("actionVertical")
        self.actionVertical.triggered.connect(self.flipVertical)

        self.actionTranslasi = QtWidgets.QAction(MainWindow)
        self.actionTranslasi.setObjectName("actionTranslasi")
        self.actionTranslasi.triggered.connect(self.translasi)

        self.actionRotasi = QtWidgets.QAction(MainWindow)
        self.actionRotasi.setObjectName("actionRotasi")
        self.actionRotasi.triggered.connect(self.rotasi)

        self.actionHistogram_Input = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Input.setObjectName("actionHistogram_Input")
        self.actionHistogram_Input.triggered.connect(self.histogramInput)

        self.actionHistogram_Output = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Output.setObjectName("actionHistogram_Output")
        self.actionHistogram_Output.triggered.connect(self.histogramOutput)

        self.actionHistogram_Input_Output = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Input_Output.setObjectName("actionHistogram_Input_Output")
        self.actionHistogram_Input_Output.triggered.connect(self.histogramInputOutput)

        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.actionAverage.triggered.connect(self.averageGrayscale)

        self.actionLightness = QtWidgets.QAction(MainWindow)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLightness.triggered.connect(self.lightnessGrayscale)

        self.actionLuminance = QtWidgets.QAction(MainWindow)
        self.actionLuminance.setObjectName("actionLuminance")
        self.actionLuminance.triggered.connect(self.luminanceGrayscale)

        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionBrightness.triggered.connect(self.brightness)

        self.actionContrast = QtWidgets.QAction(MainWindow)
        self.actionContrast.setObjectName("actionContrast")
        self.actionContrast.triggered.connect(self.contrast)

        self.actionInvers = QtWidgets.QAction(MainWindow)
        self.actionInvers.setObjectName("actionInvers")
        self.actionInvers.triggered.connect(self.invers)

        self.action1_bit = QtWidgets.QAction(MainWindow)
        self.action1_bit.setObjectName("action1_bit")
        self.action1_bit.triggered.connect(self.eksekusi_1bit)

        self.action2_bit = QtWidgets.QAction(MainWindow)
        self.action2_bit.setObjectName("action2_bit")
        self.action2_bit.triggered.connect(self.eksekusi_2bit)

        self.action3_bit = QtWidgets.QAction(MainWindow)
        self.action3_bit.setObjectName("action3_bit")
        self.action3_bit.triggered.connect(self.eksekusi_3bit)

        self.action4_bit = QtWidgets.QAction(MainWindow)
        self.action4_bit.setObjectName("action4_bit")
        self.action4_bit.triggered.connect(self.eksekusi_4bit)

        self.action5_bit = QtWidgets.QAction(MainWindow)
        self.action5_bit.setObjectName("action5_bit")
        self.action5_bit.triggered.connect(self.eksekusi_5bit)

        self.action6_bit = QtWidgets.QAction(MainWindow)
        self.action6_bit.setObjectName("action6_bit")
        self.action6_bit.triggered.connect(self.eksekusi_6bit)

        self.action7_bit = QtWidgets.QAction(MainWindow)
        self.action7_bit.setObjectName("action7_bit")
        self.action7_bit.triggered.connect(self.eksekusi_7bit)

        self.actionHE = QtWidgets.QAction(MainWindow)
        self.actionHE.setObjectName("actionHE")
        self.actionHE.triggered.connect(self.histogramEqualization)

        self.actionFHE = QtWidgets.QAction(MainWindow)
        self.actionFHE.setObjectName("actionFHE")
        self.actionFHE.triggered.connect(self.fuzzyHERGB)

        self.actionFHE_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionFHE_Grayscale.setObjectName("actionFHE_Grayscale")
        self.actionFHE_Grayscale.triggered.connect(self.fuzzyGreyscale)

        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionLow_Pass_Filter.triggered.connect(self.lowpass)

        self.actionHigh_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")
        self.actionHigh_Pass_Filter.triggered.connect(self.highpass)
        
        self.actionIdentify = QtWidgets.QAction(MainWindow)
        self.actionIdentify.setObjectName("actionIdentify")
        self.actionIdentify.triggered.connect(self.identity)

        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionRobert.setObjectName("actionRobert")
        self.actionRobert.triggered.connect(self.robert)

        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionSobel.triggered.connect(self.sobel)

        self.actionPrewit = QtWidgets.QAction(MainWindow)
        self.actionPrewit.setObjectName("actionPrewit")
        self.actionPrewit.triggered.connect(self.prewit)

        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionSharpen.triggered.connect(self.sharpen)

        self.actionGaussian_Blur_3_x_3 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3_x_3.setObjectName("actionGaussian_Blur_3_x_3")
        self.actionGaussian_Blur_3_x_3.triggered.connect(self.gaussian_blur_3x3)

        self.actionGaussian_Blur_5_x_5 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_5_x_5.setObjectName("actionGaussian_Blur_5_x_5")
        self.actionGaussian_Blur_5_x_5.triggered.connect(self.gaussian_blur_5x5)

        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionUnsharp_Masking.triggered.connect(self.unsharp_masking)

        self.actionAritmatika = QtWidgets.QAction(MainWindow)
        self.actionAritmatika.setObjectName("actionAritmatika")
        self.actionAritmatika.triggered.connect(self.frameAritmatika)

        self.actionThreshold = QtWidgets.QAction(MainWindow)
        self.actionThreshold.setObjectName("actionThreshold")
        self.actionThreshold.triggered.connect(self.threshold)

        self.actionSegmentasi_Citra = QtWidgets.QAction(MainWindow)
        self.actionSegmentasi_Citra.setObjectName("actionSegmentasi_Citra")
        self.actionSegmentasi_Citra.triggered.connect(self.segmentasi_citra)

        self.actionBackground_Removal = QtWidgets.QAction(MainWindow)
        self.actionBackground_Removal.setObjectName("actionBackground_Removal")
        # self.actionBackground_Removal.triggered.connect(self.remove_bg)

        self.actionROI = QtWidgets.QAction(MainWindow)
        self.actionROI.setObjectName("actionROI")
        self.actionROI.triggered.connect(self.roi)

        self.actionSquare_3_dilasi = QtWidgets.QAction(MainWindow)
        self.actionSquare_3_dilasi.setObjectName("actionSquare_3_dilasi")
        self.actionSquare_3_dilasi.triggered.connect(self.applyDilationSquare3)

        self.actionSquare_5_dilasi = QtWidgets.QAction(MainWindow)
        self.actionSquare_5_dilasi.setObjectName("actionSquare_5_dilasi")
        self.actionSquare_5_dilasi.triggered.connect(self.applyDilationSquare5)

        self.actionCross_3_dilasi = QtWidgets.QAction(MainWindow)
        self.actionCross_3_dilasi.setObjectName("actionCross_3_dilasi")
        self.actionCross_3_dilasi.triggered.connect(self.applyDilationCross3)

        self.actionSquare_3_erosi = QtWidgets.QAction(MainWindow)
        self.actionSquare_3_erosi.setObjectName("actionSquare_3_erosi")
        self.actionSquare_3_erosi.triggered.connect(self.applyErosionSquare3)

        self.actionSquare_5_erosi = QtWidgets.QAction(MainWindow)
        self.actionSquare_5_erosi.setObjectName("actionSquare_5_erosi")
        self.actionSquare_5_erosi.triggered.connect(self.applyErosionSquare5)

        self.actionCross_3_erosi = QtWidgets.QAction(MainWindow)
        self.actionCross_3_erosi.setObjectName("actionCross_3_erosi")
        self.actionCross_3_erosi.triggered.connect(self.applyErosionCross3)

        self.actionSquare_9_opening = QtWidgets.QAction(MainWindow)
        self.actionSquare_9_opening.setObjectName("actionSquare_9_opening")
        self.actionSquare_9_opening.triggered.connect(self.applyOpeningSquare9)

        self.actionSquare_9_closing = QtWidgets.QAction(MainWindow)
        self.actionSquare_9_closing.setObjectName("actionSquare_9_closing")
        self.actionSquare_9_closing.triggered.connect(self.applyClosingSquare9)

        self.actionRGB = QtWidgets.QAction(MainWindow)
        self.actionRGB.setObjectName("actionRGB")

        self.actionRGB_to_HSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_HSV.setObjectName("actionRGB_to_HSV")
        self.actionRGB_to_HSV.triggered.connect(self.applyRGBtoHSV)

        self.actionRGB_to_YCrCb = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_YCrCb.setObjectName("actionRGB_to_YCrCb")
        self.actionRGB_to_YCrCb.triggered.connect(self.applyColorRGBtoYCrCb)
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuAritmatika.addAction(self.actionAritmatika)
        self.menuScaling.addAction(self.actionUniform_Scaling)
        self.menuScaling.addAction(self.actionNon_Uniform_Scaling)
        self.menuFlipping.addAction(self.actionHorizontal)
        self.menuFlipping.addAction(self.actionVertical)
        self.menuGeometri.addAction(self.menuScaling.menuAction())
        self.menuGeometri.addAction(self.actionCroping)
        self.menuGeometri.addAction(self.menuFlipping.menuAction())
        self.menuGeometri.addAction(self.actionTranslasi)
        self.menuGeometri.addAction(self.actionRotasi)
        self.menuView.addAction(self.actionHistogram_Input)
        self.menuView.addAction(self.actionHistogram_Output)
        self.menuView.addAction(self.actionHistogram_Input_Output)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminance)
        self.menuBit_Depth.addAction(self.action1_bit)
        self.menuBit_Depth.addAction(self.action2_bit)
        self.menuBit_Depth.addAction(self.action3_bit)
        self.menuBit_Depth.addAction(self.action4_bit)
        self.menuBit_Depth.addAction(self.action5_bit)
        self.menuBit_Depth.addAction(self.action6_bit)
        self.menuBit_Depth.addAction(self.action7_bit)
        self.menuColors.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuColors.addAction(self.actionBrightness)
        self.menuColors.addAction(self.actionContrast)
        self.menuColors.addAction(self.actionInvers)
        self.menuColors.addAction(self.actionThreshold)
        self.menuColors.addAction(self.menuBit_Depth.menuAction())
        self.menuImage_Prossesing.addAction(self.actionHE)
        self.menuImage_Prossesing.addAction(self.actionFHE)
        self.menuImage_Prossesing.addAction(self.actionFHE_Grayscale)
        self.menuEdge_Detection.addAction(self.actionRobert)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionPrewit)
        self.menuKonvolusi.addAction(self.actionLow_Pass_Filter)
        self.menuKonvolusi.addAction(self.actionHigh_Pass_Filter)
        self.menuKonvolusi.addAction(self.actionIdentify)
        self.menuKonvolusi.addAction(self.menuEdge_Detection.menuAction())
        self.menuKonvolusi.addAction(self.actionSharpen)
        self.menuKonvolusi.addAction(self.actionGaussian_Blur_3_x_3)
        self.menuKonvolusi.addAction(self.actionGaussian_Blur_5_x_5)
        self.menuKonvolusi.addAction(self.actionUnsharp_Masking)
        self.menuSegmentasi_Citra.addAction(self.actionSegmentasi_Citra)
        self.menuBackground_Removal.addAction(self.actionBackground_Removal)
        self.menuROI.addAction(self.actionROI)
        self.menuDilasi.addAction(self.actionSquare_3_dilasi)
        self.menuDilasi.addAction(self.actionSquare_5_dilasi)
        self.menuDilasi.addAction(self.actionCross_3_dilasi)
        self.menuErosi.addAction(self.actionSquare_3_erosi)
        self.menuErosi.addAction(self.actionSquare_5_erosi)
        self.menuErosi.addAction(self.actionCross_3_erosi)
        self.menuOpening.addAction(self.actionSquare_9_opening)
        self.menuClosing.addAction(self.actionSquare_9_closing)
        self.menuMorfologi.addAction(self.menuDilasi.menuAction())
        self.menuMorfologi.addAction(self.menuErosi.menuAction())
        self.menuMorfologi.addAction(self.menuOpening.menuAction())
        self.menuMorfologi.addAction(self.menuClosing.menuAction())
        self.menuWarna.addAction(self.actionRGB)
        self.menuWarna.addAction(self.actionRGB_to_HSV)
        self.menuWarna.addAction(self.actionRGB_to_YCrCb)
        self.menuEkstraksi_Fitur.addAction(self.menuWarna.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAritmatika.menuAction())
        self.menubar.addAction(self.menuGeometri.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuColors.menuAction())
        self.menubar.addAction(self.menuImage_Prossesing.menuAction())
        self.menubar.addAction(self.menuKonvolusi.menuAction())
        self.menubar.addAction(self.menuSegmentasi_Citra.menuAction())
        self.menubar.addAction(self.menuBackground_Removal.menuAction())
        self.menubar.addAction(self.menuROI.menuAction())
        self.menubar.addAction(self.menuMorfologi.menuAction())
        self.menubar.addAction(self.menuEkstraksi_Fitur.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAritmatika.setTitle(_translate("MainWindow", "Aritmatika"))
        self.menuGeometri.setTitle(_translate("MainWindow", "Geometri"))
        self.menuScaling.setTitle(_translate("MainWindow", "Scaling"))
        self.menuFlipping.setTitle(_translate("MainWindow", "Flipping"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuColors.setTitle(_translate("MainWindow", "Colors"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuImage_Prossesing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuKonvolusi.setTitle(_translate("MainWindow", "Konvolusi"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuSegmentasi_Citra.setTitle(_translate("MainWindow", "Segmentasi Citra"))
        self.menuBackground_Removal.setTitle(_translate("MainWindow", "Background Removal"))
        self.menuROI.setTitle(_translate("MainWindow", "ROI"))
        self.menuMorfologi.setTitle(_translate("MainWindow", "Morfologi"))
        self.menuDilasi.setTitle(_translate("MainWindow", "Dilasi"))
        self.menuErosi.setTitle(_translate("MainWindow", "Erosi"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuEkstraksi_Fitur.setTitle(_translate("MainWindow", "Ekstraksi Fitur"))
        self.menuWarna.setTitle(_translate("MainWindow", "Warna"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUniform_Scaling.setText(_translate("MainWindow", "Uniform Scaling"))
        self.actionNon_Uniform_Scaling.setText(_translate("MainWindow", "Non-Uniform Scaling"))
        self.actionCroping.setText(_translate("MainWindow", "Cropping"))
        self.actionHorizontal.setText(_translate("MainWindow", "Horizontal"))
        self.actionVertical.setText(_translate("MainWindow", "Vertical"))
        self.actionTranslasi.setText(_translate("MainWindow", "Translasi"))
        self.actionRotasi.setText(_translate("MainWindow", "Rotasi"))
        self.actionHistogram_Input.setText(_translate("MainWindow", "Histogram Input"))
        self.actionHistogram_Output.setText(_translate("MainWindow", "Histogram Output"))
        self.actionHistogram_Input_Output.setText(_translate("MainWindow", "Histogram Input Output"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.action1_bit.setText(_translate("MainWindow", "1 bit"))
        self.action2_bit.setText(_translate("MainWindow", "2 bit"))
        self.action3_bit.setText(_translate("MainWindow", "3 bit"))
        self.action4_bit.setText(_translate("MainWindow", "4 bit"))
        self.action5_bit.setText(_translate("MainWindow", "5 bit"))
        self.action6_bit.setText(_translate("MainWindow", "6 bit"))
        self.action7_bit.setText(_translate("MainWindow", "7 bit"))
        self.actionHE.setText(_translate("MainWindow", "HE"))
        self.actionFHE.setText(_translate("MainWindow", "FHE RGB"))
        self.actionFHE_Grayscale.setText(_translate("MainWindow", "FHE Grayscale"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionIdentify.setText(_translate("MainWindow", "Identity"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionPrewit.setText(_translate("MainWindow", "Prewit"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionGaussian_Blur_3_x_3.setText(_translate("MainWindow", "Gaussian Blur 3 x 3"))
        self.actionGaussian_Blur_5_x_5.setText(_translate("MainWindow", "Gaussian Blur 5 x 5"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAritmatika.setText(_translate("MainWindow", "Aritmatika"))
        self.actionThreshold.setText(_translate("MainWindow", "Threshold"))
        self.actionSegmentasi_Citra.setText(_translate("MainWindow", "Segmentasi Citra"))
        self.actionBackground_Removal.setText(_translate("MainWindow", "Background Removal"))
        self.actionROI.setText(_translate("MainWindow", "ROI"))
        self.actionSquare_3_dilasi.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_5_dilasi.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_3_dilasi.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_3_erosi.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_5_erosi.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_3_erosi.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_9_opening.setText(_translate("MainWindow", "Square 9"))
        self.actionRGB.setText(_translate("MainWindow", "RGB"))
        self.actionRGB_to_HSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.actionRGB_to_YCrCb.setText(_translate("MainWindow", "RGB to YCrCb"))
        self.actionSquare_9_closing.setText(_translate("MainWindow", "Square 9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
