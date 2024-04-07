import qrcode
qr = qrcode.QRCode(border=1.5)
qr.add_data(input('Enter url: '))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save('qr.png')