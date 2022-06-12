import cv2
from PIL import Image

image_path = 'cat.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')
for (x, y, w, h) in cat_face:
    glasses = glasses.resize((w, h//3))
    cat.paste(glasses, (x, y + h//4), glasses)
    cat.save('cat_with_glasses.png')

