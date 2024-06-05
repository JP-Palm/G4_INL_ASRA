from flask import Flask, url_for
from app.main.routes import main
from app.main.api import api


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config.from_object('config.Config')

app.register_blueprint(main)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)