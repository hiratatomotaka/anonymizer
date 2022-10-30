import cv2

class カメラ:
    def __init__(self):
        self.__cap = cv2.VideoCapture(0)
        
    def が撮影する(self):
        ret, img = self.__cap.read()
        return img

    def を止める(self):
        self.__cap.release()
        
    
