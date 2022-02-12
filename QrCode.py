# Contact Tracing App
# Create a python program that will read QRCode using your webcam
# You may use any online QRCode generator to create QRCode
# All personal data are in QRCode 
# You may decide which personal data to include
# All data read from QRCode should be stored in a text file including the date and time it was read

# Generating Qrcode
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
data = "https://www.facebook.com/reximman.robles"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")

# Qr code scanner
import cv2
import webbrowser

cap = cv2.VideoCapture(0)
det =  cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, one, _ = det.detectAndDecode(img)
    if data:
        read = data
        break
    cv2.imshow('QRCode Scanner', img)
    if cv2.waitKey(1)==ord('a'):
        break
    
direct = webbrowser.open((str(read)))
cap.release(read)
cv2.destroyAllWindows 