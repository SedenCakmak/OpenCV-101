import cv2

#resmi içe aktarma
img = cv2.imread("collesseo.jpg",0)

#görselleştir
cv2.imshow("ilk resim",img)
cv2.waitKey(0)

k = cv2.waitKey(0) &0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("dost_gray.png",img)
    cv2.destroyAllWindows()
