import cv2
from PIL import Image, ImageDraw
import numpy as np

path = './data/meixi.jpg'
img = Image.open(path)
img = np.array(img)
print(img)
# iw, ih = img.size
# print("img.size:", iw, ih)
draw = ImageDraw.Draw(img)
