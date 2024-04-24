import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG= False
    POSTGRESS_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR=os.path.join(basedir,"../db_directory")
    SQLALCHEMY_DATABASE_UR="sqlite:///"+ os.path.join(SQLITE_DB_DIR,"Reso.db")
    DEBUG=True
    