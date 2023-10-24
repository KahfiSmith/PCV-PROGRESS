import cv2 
import sys

def hsv(image_path):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image

image_path = "squid crab.png"
hsv_pixels = hsv(image_path)

# Inisialisasi variabel boolean untuk mengontrol perulangan
selesai = False

# Iterasi melalui setiap pixel dalam gambar
for row in hsv_pixels:
    for pixel in row:
        h, s, v = pixel
        print(f"H: {h}, S: {s}, V: {v}")
        
        # Tambahkan kondisi untuk menghentikan perulangan
        if h == 100:  # Ganti dengan kondisi yang sesuai
            selesai = True
            break
    if selesai:
        break