from flask import Flask, render_template, request, jsonify
from PIL import Image
import base64
from io import BytesIO
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    # Get the base64-encoded image data from the request
    image_data = request.form['imageData']

    # Create a PIL Image object from the base64 data
    image = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1])))

    # Generate a unique filename for the image
    filename = str(uuid.uuid4()) + '.png'

    # Save the image with the unique filename in the static folder
    image.save('static/' + filename)

    return jsonify({'message': 'Image saved successfully.', 'filename': filename})

if __name__ == '__main__':
    app.run(debug=True)
