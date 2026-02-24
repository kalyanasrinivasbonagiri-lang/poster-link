import qrcode

url = "https://raw.githubusercontent.com/kalyanasrinivasbonagiri-lang/poster-link/main/Poster%20final.png"

img = qrcode.make(url)
img.save("poster_qr.png")

print("QR created!")