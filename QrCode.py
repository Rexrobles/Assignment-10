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
data = "https://www.facebook.com/reximman.robles/"
qr.add_data('data')
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black")
img.save("qr.png")



