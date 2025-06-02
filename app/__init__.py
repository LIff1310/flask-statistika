from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    from app.controllers.statistik_controller import statistik_bp
    app.register_blueprint(statistik_bp)

    return app