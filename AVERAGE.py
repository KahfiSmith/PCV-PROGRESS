import cv2
import numpy as np
import pandas as pd

def rata_rata(image_path):
    image = cv2.imread(image_path)
    r, g, b = cv2.split(image)
    avg_r = np.mean(r)
    avg_g = np.mean(g)
    avg_b = np.mean(b)

    return [avg_r, avg_g, avg_b]

image_path = "squid crab.png"
features = rata_rata(image_path)
feature_matrix = np.reshape(features, (1, len(features)))
data = pd.DataFrame(feature_matrix, columns=['Average R', 'Average G', 'Average B'])
data.to_excel('image_features.xlsx',index=False)


