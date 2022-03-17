from flask import Flask
from flask_wtf.csrf import CSRFProtect
from pathlib import Path 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = "g-cup",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        #__file__ 実行中の不アイルの場所
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_SECRET_KEY = "abcdef"
    )

    db.init_app(app)
    Migrate(app, db)

    csrf.init_app(app)

    from apps.todo import views 
    app.register_blueprint(views.todo, url_prefix = "/todo")
    return app