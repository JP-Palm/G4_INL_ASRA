from flask import Blueprint, jsonify, request, url_for
from .utils import get_prediction
import base64


api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/classify", methods=["POST"])
def classify_api():
    if 'photo' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
    file = request.files['photo']
    img_bytes = file.read()
    prediction, confidence = get_prediction(img_bytes)
    
    return jsonify({'prediction': prediction, 'confidence': confidence})