import os
import sys
from sayhello import app

### SQLlite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

### 采用的本地sqlite数据库存储
dev_db = prefix + os.path.join(os.path.dirname(app.root_path),'data.db')
### SECRET_KEY 程序密钥
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
### 该变量决定是否追踪对象的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False

### ‘DATABASE_URI’从环境变量里面读取，可在环境变量内设置采用mysql数据库存储
### 格式URI: mysql://username:password@host:port/databasename
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI',dev_db)
