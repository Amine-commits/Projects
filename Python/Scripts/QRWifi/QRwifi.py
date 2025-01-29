from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

save_path = Path(os.getenv("QR_SAVE_PATH"))

import qrcode

qr=qrcode.make("SSID:Keepitsafemain And Pass : BruteF0rceThisShit@@")

qr.save("QRWifi.png")

print("QR code saved as QRWifi.png") 