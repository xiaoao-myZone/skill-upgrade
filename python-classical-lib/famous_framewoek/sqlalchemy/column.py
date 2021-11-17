from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.dialects.mysql import INTEGER
from app import engine, Base, database


class Collection(Base):
    __tablename__ = "collection"
    pid = Column(INTEGER(11), primary_key=True,
                 nullable=False, autoincrement=True)
    # nullable和autoincrement是否冲突？ 既然是autoincrement，那么就不能指定其值, 实际上没有冲突
    comment = Column(String(22), default="", nullable=True)
    # nullable和default不冲突？
    name = Column(String(30), server_default=text("'0'"))
    sex = Column(String(10), server_default=text("'nulll'"))
    age = Column(INTEGER(11), server_default=text("'0'"))


if __name__ == "__main__":
    Base.metadata.drop_all()
    Base.metadata.create_all()
    db = database(engine, Collection)
    # db.add(comment="ahha", name="Buby", sex="female")
    db.add()

"""
Conclusions:
    1. 对mysql来说， default默认为NULL， 通过nullable来控制NULL是否合法，这是一种约束条件
    2. sqlalchemy.sql.expression.text 会把其中的内容等效为sql语句中的字面意思, "0" 与"'0'"是等价表达方式
    3. 在2的基础上， "null"与"'null'"却有不同， 前者是数据类型null，后者是字符串null， 所以text中的字符串参数
       相当于将双引号去掉直接植入sql语句中的作用
    4. 根据文档描述， 当Column中选择primary_key=True时， 会自动将nullable设为False
"""
