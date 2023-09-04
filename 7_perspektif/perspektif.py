import cv2
import numpy as np
import matplotlib.pyplot as plt


Card = cv2.imread("WoNEz.png")
img4= cv2.cvtColor(Card,cv2.COLOR_RGB2BGR)
plt.figure(), plt.imshow(img4), plt.title("ID"), plt.axis("off"), plt.show()
print(img4.shape)

height = 300
width = 500
pts1 = np.float32([[10,5],[5,430],[438,100],[475,389]])
pts2= np.float32([[0,0],[0,height],[width,0],[width,height]])


matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)
imgOut = cv2.warpPerspective(img4, matrix, (width,height))
plt.figure(), plt.imshow(imgOut), plt.title("perspective"), plt.axis("off"), plt.show()