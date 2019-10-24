from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exist import db
from models import User
manager = Manager(app)
#使用migrate绑定app和db
migrate = Migrate(app,db)
#将所有的迁移命令绑定到manager中
manager.add_command('db',MigrateCommand)


if __name__=='__main__':
    manager.run()