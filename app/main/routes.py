from datetime import datetime
from flask import render_template, Blueprint
import torch
from torchvision import models
import os
import base64
import uuid

from .forms import PhotoForm
from .utils import transform_image, get_prediction, save_image

main = Blueprint('main', __name__)

@main.route('/', methods=["GET", "POST"])
def index():
    form = PhotoForm()

    if form.validate_on_submit():
        file = form.photo.data
        img_bytes = file.read()
        prediction, confidence = get_prediction(img_bytes)
        encoded_img_bytes = base64.b64encode(img_bytes).decode('utf-8')
        
        # TODO We should do this sometime, but with proper handling of making folder if we don't have one for feedback_data
        unique_filename = str(uuid.uuid4()) + ".jpg"
        # class_folder = os.path.join('C:/python/maskin inlärning/first_cnn_with_chatgpt_4o/feedback_data', prediction)
        # save_image(img_bytes, class_folder, unique_filename)
        
        return render_template('result.html', prediction=prediction, confidence=confidence, image_bytes=encoded_img_bytes, filename=unique_filename)
    
    return render_template('index.html', form=form)