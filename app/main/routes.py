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

@main.route('/', methods=["GET"])
def index():
    form = PhotoForm()

    return render_template('index.html', form=form)