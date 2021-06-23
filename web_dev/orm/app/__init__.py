# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('app.secure')
# app.config.from_object('app.setting')
socketio = SocketIO(app, cors_allowed_origins="*")

def strip_underline(s):

    if s.endswith('_'):
        return s[:-1]
    else:
        return s

def to_dict(self):
    res = {}
    for i in self.__dict__:
        if not i.startswith('_'):
            if i.endswith('_'):
                res[i[:-1]] = self.__dict__[i]
            else:
                res[i] = self.__dict__[i]

    return res

# print(dir(db.Column(db.String(30), name="class")))

db.Model.to_dict = to_dict
db.Model.__table_args__ = {
    "mysql_charset": "utf8"
}


class Log(db.Model):
    __tablename__ = 'log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    msg_type = db.Column(db.String(10))
    code = db.Column(db.String(10))
    class_ = db.Column(db.String(30), name="class")
    tag = db.Column(db.String(30))
    object_ = db.Column(db.String(30), name="object")
    tool = db.Column(db.String(30))
    worksapce = db.Column(db.String(30))
    zh_msg = db.Column(db.String(100))
    en_msg = db.Column(db.String(100))
    zh_tip = db.Column(db.String(100))
    en_tip = db.Column(db.String(100))
    timeout = db.Column(db.Integer)
    timestamp = db.Column(db.Integer)


class Fun(db.Model):
    __tablename__ = 'fun'
    id_ = db.Column(db.Integer, primary_key=True,
                    autoincrement=True, name="id")
    name = db.Column(db.String(10))


db.init_app(app)  # db可以检索到哪些类继承于它
db.create_all(app=app)


@app.route("/", methods=["POST"])
def add_name():
    data = request.get_json()
    name = data["name"]
    fun = Fun(name=name)
    db.session.add(fun)
    db.session.commit()
    return jsonify({"code":0})

@app.route("/query", methods=["POST"])
def query():
    ret = []
    res = Fun.query.filter(Fun.id_.between(0, 2))
    # print(res) # 打印出sql
    for i in dir(res[0]):
        print("%s --> %s" % (i, getattr(res[0], i)))
    for i in res:
        
        data = i.to_dict()
        ret.append(data)
        # print(data) # db.Integer是长整形, print出来是1L
        # print(data["id"]+1)
    return jsonify({"code":0, "data": ret})

