from flask import Flask
import psycopg2

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lasdnfalskdnfl'
    
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
    return app
