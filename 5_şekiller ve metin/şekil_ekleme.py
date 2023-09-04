import cv2
import numpy as np


# resim oluştur
img = np.zeros((512,512,3),np.uint8)
print(img.shape)

cv2.imshow("Siyah",img)

# çizgi
# resim, başlangıç noktası, bitiş noktası, renk
cv2.line(img,(0,0),(512,512),(0,255,0)) #BGR = (0,0,255)
cv2.imshow("Cizgi",img)

# dikdörtgen
# (resim, başlangıç,bitiş,renk)
cv2.rectangle(img,(0,0),(256,256),(255,0,0), cv2.FILLED)
cv2.imshow("Dikdörtgen",img)

# çember
#(resim, merkez,yarıçap,renk)
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("Cember",img)


# metin
#(resim,başlangıç noktası,font,kalınlık, renk)
cv2.putText(img, "Resim", (350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Metin",img)
