from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Float, String
from sqlalchemy.dialects.mysql import INTEGER
from app import engine, Base, database


class Student(Base):
    __tablename__ = "student"
    pid = Column(INTEGER(11), primary_key=True, autoincrement=True)
    name = Column(String(10))
    sex = Column(String(10), comment="male or female")
    score = Column(Float, server_default="0.0")


if __name__ == "__main__":
    Base.metadata.drop_all()
    Base.metadata.create_all()
    db = database(engine, Student)
    db.add(name="王豪", sex="male", score=76.4)
    # obj = db.session.query(Student)
    # print(obj)
    # print(type(obj))
    # for i in dir(obj):
    #     if not i.startswith("_"):
    #         print(f"{i} --> |{getattr(obj, i)}|  {type(getattr(obj, i))}")
    # for i in db.session.query(Student).values():
    #     print(i)
    # print(db.session.query(Student).values())
    print(db.session.query(Student).one())


"""
# TODO
1. 在ipython命令行中先查询所有内容存在结果， 但是在另一个终端中进入mysql， 并删掉该表中的所有的数据， 继续用ipython查询，
   依然可以查到, 也就是出现了幻读, 即便我重新创建一个engine, 与session也不能解决问题， 这是为什么？
2. 上述问题在我调用session.commit()后消失， 这也许是为了保证事务原子性的一个特征
3. 在ipython中的session没有结束的情况下， 在vscode中运行这段代码
   发现查询结果会被阻塞住，直到ipython中的session调用close
"""
