from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PhotoForm(FlaskForm):
    photo = FileField(validators=[
        FileRequired(),
        FileAllowed(["jpg", "png"], "Images only!")
        ])