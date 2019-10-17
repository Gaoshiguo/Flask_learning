from flask_script import Manager
from app import app
from flask_migrate import Migrate,MigrateCommand
from exist import db
from models import Article
from models import User
manager = Manager(app)

#1.要使用migrate,必须先绑定app和db
migrate = Migrate(app,db)
#2.把migrate command添加到manager命令中
manager.add_command('db',MigrateCommand)

if __name__ == "__main__":
    manager.run()
