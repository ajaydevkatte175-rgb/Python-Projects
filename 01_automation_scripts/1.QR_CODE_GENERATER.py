# Basic QR code generator using the qrcode library in Python. This code creates a QR code for the URL 'https://docs.python.org/3/' and saves it as 'qr_code.png'.

import qrcode as qr

img = qr.make('https://docs.python.org/3/')
img.save('qr_code.png')


# Advanced QR code generator with customization options. This code allows you to specify the URL, error correction level, box size, and border size for the QR code.

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://docs.python.org/3/')
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='white')
img.save('custom_qr_code.png')
