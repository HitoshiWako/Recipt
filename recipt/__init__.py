from flask import Flask

from recipt.database import init_db
from recipt.model import Item

def create_app():
    app = Flask(__name__)
    app.config.from_object('recipt.config.Config')

    init_db(app)

    from . import admin
    app.register_blueprint(admin.bp)

    from . import shop
    app.register_blueprint(shop.bp)

    @app.route('/item/<int:shop_id>')
    def show_shop(shop_id):
        return f'Shop ID:{shop_id}'
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

app = create_app()