from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

# Minimal placeholder predict function
def predict(image_bytes):
    # This is a placeholder. Replace with model loading and predict.
    return {"pred": "normal", "confidence": 0.78}

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    img_bytes = file.read()
    pred = predict(img_bytes)
    return jsonify(pred)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
