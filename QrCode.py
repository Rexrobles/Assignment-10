# Contact Tracing App
# Create a python program that will read QRCode using your webcam
# You may use any online QRCode generator to create QRCode
# All personal data are in QRCode 
# You may decide which personal data to include
# All data read from QRCode should be stored in a text file including the date and time it was read

# Qr code scanner
import cv2
import webbrowser
import datetime
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
det =  cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, one, _ = det.detectAndDecode(img)
    read = data   
    for Information in decode(img):
        txt = Information.data.decode('utf-8')
        print(txt)
        with open("QrCodeRecord.txt", 'a') as f:
            f.write(f'{txt} ')
            cap.release(txt)
            cv2.destroyAllWindows
            break
        
    cv2.imshow('My Scanner', img)
    if cv2.waitKey(1)==ord('a'):
        break
    
direct = webbrowser.open((str(read)))
cap.release(read)
cv2.destroyAllWindows 
