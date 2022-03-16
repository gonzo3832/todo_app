from flask import Flask

def create_app():
    app = Flask(__name__)
    from apps.todo import views 
    app.register_blueprint(views.todo, url_prefix = "/todo")
    return app