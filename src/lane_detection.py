import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

lane_img = cv2.imread("./imgs/lane_test.jpeg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(lane_img, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(gray, 150, 300, apertureSize=3)

canny_img = np.copy(canny)
height = canny_img.shape[0]
width = canny_img.shape[1]

print(f"Image width : {width}, height : {height}\n")

d = height // 10
epo1 = 2*d
epo2 = d*9
crop_img = canny_img[epo1:epo2] # height를 d등분해서 3번째 (2d ~ 3d-1)

# strengthen
strengthen_img = np.power(crop_img, 2)
crop_height = strengthen_img.shape[0]
crop_width = strengthen_img.shape[1]
print(f"Crop image width : {crop_width}, height : {crop_height}\n")

middles = []

start = time.time()
for i in range(len(strengthen_img)):
    lcur = crop_width // 2 - (crop_width // 4)
    rcur = crop_width // 2 + (crop_width // 4)

    while(strengthen_img[i][lcur] == 0 or strengthen_img[i][rcur] == 0):
        if strengthen_img[i][lcur] == 0:
            lcur -= 1
        if strengthen_img[i][rcur] == 0:
            rcur += 1
        if lcur < 0:
            lcur = 0
            break
        if rcur > crop_width - 1:
            rcur = crop_width - 1
            break

    middle = (rcur + lcur) // 2
    middles.append(middle)

# draw middle line
color = (255, 0, 0)
for i in range(epo1, epo2):
    canny_img = cv2.line(canny_img,(middles[i-epo1],i), (middles[i-epo1],i), color, 5)

plt.subplot(1, 2, 1)
plt.imshow(canny_img)
plt.subplot(1, 2, 2)
plt.imshow(crop_img)
plt.show()
x_center = np.mean(middles)

print(f"avg of middle point : {x_center}")
end = time.time()

print(f"running time : {end-start} sec")