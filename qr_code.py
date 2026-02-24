import qrcode
from PIL import Image

image_url = "https://i.imgur.com/abc123.png"

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data(image_url)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# add logo
logo = Image.open("gri_logo.png")
logo = logo.resize((qr_img.size[0]//4, qr_img.size[1]//4))

pos = ((qr_img.size[0]-logo.size[0])//2,
       (qr_img.size[1]-logo.size[1])//2)

qr_img.paste(logo, pos)

qr_img.save("image_qr_logo.png")