import qrcode
import tkinter as tk
from tkinter import ttk

def generate_qr_code():
    input_url = url_entry.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_url)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save("qrcode.png")

    result_label.config(text="QR code generated successfully")

root = tk.Tk()
root.title("QR Code Generator")

url_label = ttk.Label(root, text="Enter URL to generate QR code")
url_label.pack()

url_entry = ttk.Entry(root)
url_entry.pack()

generate_button = ttk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()




