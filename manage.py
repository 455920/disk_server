# _*_ codding:utf-8 _*_
from app import create_app, db
from app.models import *
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask import render_template

app = create_app('default')


# 使app支持命令行操作
manager = Manager(app)
# 绑定app和db
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))

#添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)


@app.errorhandler(404)
def page_not_found(error):
    """
    404
    """
    return render_template("home/404.html"), 404


if __name__ == '__main__':
    manager.run()
