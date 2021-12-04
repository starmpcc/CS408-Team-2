'''
sample web with flask_web
'''
import os
API_HOME = "/root/CS408-Team-2/web"
SQL_HOME = os.path.join(API_HOME, "sqldb_dir")
if not os.path.exists(SQL_HOME):
    os.makedirs(SQL_HOME, exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jfidsjfsdi7813y8hjds87hj'
    SQLALCHMEY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_FILE = os.environ.get('DEV_DATABASE_FILE') or \
        os.path.join(SQL_HOME, 'data-dev.sqllite')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(SQL_HOME, 'data-dev.sqlite')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
