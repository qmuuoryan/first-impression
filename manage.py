from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role
from app.models import User,Role,Review
from flask_migrate import Migrate, MigrateCommand

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role=Role )
if __name__ == '__main__':
    manager.run()
