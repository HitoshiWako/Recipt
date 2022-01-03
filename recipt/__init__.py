from flask import Flask

from recipt.database import init_db
from recipt.model import Item

def create_app():
    app = Flask(__name__)
    app.config.from_object('recipt.config.Config')

    init_db(app)

    from . import mainpage
    app.register_blueprint(mainpage.bp)
    app.add_url_rule('/', endpoint='index')

    from . import admin
    app.register_blueprint(admin.bp)

    from . import item
    app.register_blueprint(item.bp)

    from . import shop
    app.register_blueprint(shop.bp)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

app = create_app()