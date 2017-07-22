import qrcode
import StringIO

import flask
app = flask.Flask(__name__)


def serve_pil_image(pil_img):
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'PNG', quality=70)
    img_io.seek(0)
    return flask.send_file(img_io, mimetype='image/png')

@app.route("/generate")
def generate_qr():
	url = flask.request.args.get('url')
	words = flask.request.args.get('words').split(',')
	img = qrcode.make(url)

	return serve_pil_image(img)
