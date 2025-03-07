from flask import Flask
from flask_migrate import Migrate
from app.database import db
from app.routes import expense_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    Migrate(app, db)

    @app.route("/", methods=["GET"])
    def home():
        return {"message": "Welcome to expense tracker API"}

    app.register_blueprint(expense_routes)

    return app
