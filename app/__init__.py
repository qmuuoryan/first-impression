from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail






def create_app(config_name):
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)

     # configure UploadSet
    configure_uploads(app,photos)
class Config:

    mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    #........
    mail.init_app(app)
#........