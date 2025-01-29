# if not done yet, install qrcode module with pip install qrcode

import qrcode # Import the qrcode module
qr=qrcode.make("SSID:Keepitsafemain" "/////" "Pass:BruteF0rceThisShit@@") # Create a QR code

qr.save("QRWifi.png") # Save the QR code as a PNG file

print("QR code saved as QRWifi.png") # Print a message to the console