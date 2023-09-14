import qrcode
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/generate')
def generate_qr_code():
    input_url = request.args.get('inputUrl')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(input_url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_path = "qrcode.png"
    img.save(img_path)

    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
