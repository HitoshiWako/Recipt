from flask import Flask

from recipt.database import init_db
from recipt.model import Item

def create_app():
    app = Flask(__name__)
    app.config.from_object('recipt.config.Config')

    init_db(app)

    return app

app = create_app()