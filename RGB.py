import cv2 

def rgb(image_path):
    
    image = cv2.imread(image_path)
    b, g, r = cv2.split(image)
    pixels = cv2.merge((r, g, b))
    return pixels

image_path = "squid crab.png"
pixels =  rgb(image_path)
for pixel in pixels:
    print(f"R: {pixel[0]}, G: {pixel[1]}, B: {pixel[2]}")

