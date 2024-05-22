from datetime import datetime
from flask import render_template, Blueprint

from .forms import PhotoForm

main = Blueprint('main', __name__)

@main.route('/', methods=["GET", "POST"])
def index():
    form = PhotoForm()

    if form.validate_on_submit():
        f = form.photo.data
        return "Photo submitted successfully!"

    return render_template('index.html', form=form)