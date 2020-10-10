from datetime import datetime
from sayhello import db

### 建立数据库模型: id,name,body,timestamp
class Message(db.Model):
    ### id为整型，作为主键
    id = db.Column(db.Integer,primary_key=True)
    ### name为长度不超过20的字符串
    name = db.Column(db.String(20))
    ### body为长度不超过200的字符串
    body = db.Column(db.String(200))
    ### timestamp为时间日期
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
