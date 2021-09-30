# import pymysql
import functools
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# pymysql.install_as_MySQLdb()
DB_URL = "{dialect}://{username}:{password}@{host}:"\
    "{port}/{database}?charset=utf8".format(
        dialect="mysql+pymysql", username="root",
        password="zxcasd", host="localhost", port=3306,
        database="test"
    )
# 不能用mysql+pymsql://...， 而要用mysql://..，并且pymysql.install_as_MySQLdb()
engine = create_engine(DB_URL)
Base = declarative_base(engine)


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    age = Column(Integer, nullable=False)
    addr = Column(String(10), nullable=True)

    def __repr__(self) -> str:
        return f"{self.__tablename__}: {self.id=} {self.name=} {self.age}"


def commit(func):
    @functools.wraps(func)
    def _wrapper(self, *args, **kwargs):
        try:
            ret = func(self, *args, **kwargs)
            self.session.commit()
            return ret
        except Exception as e:
            print(str(e))
            self.session.rollback()
            self._create_new_session()
    return _wrapper


class database(object):
    def __init__(self, engine, table) -> None:
        self.engine = engine
        self.session = sessionmaker(engine)()
        self.table = table

    def _create_new_session(self):
        self.session = sessionmaker(self.engine)()

    @commit
    def add(self, **kwargs):
        record = self.table(**kwargs)
        self.session.add(record)

    @commit
    def add_1(self, **kwargs):
        record = self.table()
        for k, v in kwargs.items():
            setattr(record, k, v)
        # print(f'{record._sa_instance_state.modified=}')
        # print(f'{record._sa_instance_state.expired=}')
        self.session.add(record)
        # print(f'{record._sa_instance_state.modified=}')
        # print(f'{record._sa_instance_state.expired=}')

    @commit
    def update(self, From, To):
        self._update(From, To)

    def _update(self, From, To):
        record = self.query(**From)
        for k, v in To.items():
            setattr(record, k, v)
        return record

    @commit
    def delete(self):
        pass

    @commit
    def query(self, **kwargs):
        return self.session.query(self.table).filter_by(**kwargs).first()


if __name__ == "__main__":
    # import pprint
    # Base.metadata.drop_all()
    Base.metadata.create_all()
    db = database(engine, Person)

    # a = db.table()
    # a.age = 22
    # pprint.pprint(a._sa_instance_state.__dict__)
    # b = db.table(name="Paul")
    # db.session.add(b)
    # pprint.pprint(b._sa_instance_state.__dict__)

    # # {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState>}
    # print(dir(db.session))
    # db.add(name="Andy", age=20)
    # print(db.query(id=1))
    # db.update(From={"id": 1}, To={"name": "Candy"})
    # 更新
    # record = db._update(From={"id": 2}, To={"age": 13})
    # print(record.__dict__)
    # pprint.pprint(record._sa_instance_state.__dict__)

    # db.session.add(record)
    # pprint.pprint(record._sa_instance_state.expired)
    # db.session.commit()
    # pprint.pprint(record._sa_instance_state.expired)

    db.add_1(name="ss", age=2)

"""
Conclusion:
    1. 不能用mysql+pymysql://...， 而要用mysql://..，并且pymysql.install_as_MySQLdb()
    2. 这是什么原因？（难道是pymysql的下载源不一样？） -_-||| 一般来说是拼错了
      https://cdn.mysql.com//Downloads/Connector-Python/mysql-connector-python-py3_8.0.26-1ubuntu21.04_amd64.deb
    3. 增: session.add(tb_ins)  但是注意， 当tb_ins指定了主键id后， 其实是update
    4. 改： 是一个隐式的过程， 只需要把通过session.query查到的tb_ins修改值， 就会被标记更改，
       通过session.add可以提交
    5. 创建table对象时加入字段与创建后加入字段， 再使用session.add， 效果是一样的， 但是当不可为空字段不全的时候，
       session.add会抛出错误， 估计delete也会抛错
    6. TODO 将db-sql中的试题尝试用sqlalchemy做出来
    7. 根据其官网上的特点， 就是它可以做到结尾开放式（open-ended）
    8. session.commit()后， 之前创建的record._sa_instance_state.expired会变为True
    9. 对于发现5， 为什么非要add后才会生效， 而查询出来的结果不需要add， commit就可以更新
"""
