import os
from flask import Flask,current_app
from applications import config
from applications.config import LocalDevelopmentConfig
from applications.database import init_db
from applications.controllers import setup_routes 

app = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
        raise Exception("it's not for production")
    else:
        print("starting local development")
        app.config.from_object(LocalDevelopmentConfig)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/suneh/week5/db_directory/Reso.db'  # Replace with your actual database URI
    
    init_db(app)  # Initialize the database within the app context
    setup_routes(app)
    return app

app = current_app or create_app()
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)




