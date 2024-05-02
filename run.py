from flask import Flask
from app.main.routes import main

app = Flask(__name__, template_folder='app/templates')
app.config.from_object('config.Config')

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)