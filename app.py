import qrcode
import StringIO
from PIL import ImageFont
from PIL import ImageDraw

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

	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("OpenDyslexic-Regular.otf", 24)

	xoffset = 35
	yoffset = 3
	draw.text((xoffset, yoffset)," ".join(words),(0),font=font)
	del draw

	return serve_pil_image(img)
