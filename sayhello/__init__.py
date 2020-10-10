# -*- coding: utf-8 -*-
from flask import Flask # 原始Flask模块
from flask_bootstrap import Bootstrap # 渲染模板文件模块
from flask_moment import Moment # 时间信息模块
from flask_sqlalchemy import SQLAlchemy # 数据库模块

### 创建一个app实例
app = Flask('sayhello')

### 从config.py文件中读取配置信息
### 也可以直接采用例如: app.config['ADMIN_NAME'] = 'Ghz'
### 配置的名称必须为全大写形式，小写变量将不会读取。
app.config.from_pyfile('config.py')

### 该部分是为了注释掉jinjia2模板中的空白行
### 可参考: https://www.jianshu.com/p/9db09efd25aa
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

### 实例化SQLAlchemy类并传入app
db = SQLAlchemy(app)
### 实例化Bootstrap类并传入app
bootstrap = Bootstrap(app)
### 实例化Moment类并传入app
moment = Moment(app)

### 导入views.py等文件
from sayhello import views, errors, commands
