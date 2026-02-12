from flask import Flask
from .routes.category_routes import category_bp
from config import Config
from pymongo import MongoClient

db=None

def create_app():
    app=Flask(__name__)
    
    app.register_blueprint(category_bp)
    app.config.from_object(Config)
    global db

    try:
        client=MongoClient(app.config['MONGO_URI'])
        db=client.get_default_database()

    except Exception as e:
        print(f'Erro ao conectar com o Banco de dados: {e}')

    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app