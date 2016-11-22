# -*- coding:utf-8 -*-
'''Flask程序对象的穿件必须在__init__.py文件里面完成，然后倒入引用每个包'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建项目对象
app = Flask(__name__)
### 加载配置文件内容
# 模块下的setting文件名，不用加py后缀
app.config.from_object('blog.setting')
# 环境变量，指向配置文件setting的路径
app.config.from_envvar('FLASKR_SETTINGS')

# 注意：FLASKR_SETTINGS环境变量需要手工单独设置，window下可以在命令行中输入：
# E:\workdir\blog> set FLASKR_SETTINGS=E:\python_ex\litterProject\blog\setting.py

# 创建数据库对象
db = SQLAlchemy(app)
from blog.model import User, Category
from blog.controller import blog_message