# encoding: utf-8

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 在Python3中才有这个enum模块，在python2中没有

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '929526'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,
                                                                                           password=PASSWORD,
                                                                                           host=HOSTNAME, port=PORT,
                                                                                           db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id",Integer,ForeignKey("article.id"),primary_key=True),
    Column("tag_id",Integer,ForeignKey("tag.id"),primary_key=True)
)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    tags = relationship("Tag", backref="articles", secondary=article_tag)

    def __repr__(self):
        return "<User(title:%s)>" % self.title


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Tag(name:%s)>" % self.name



# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(title="article1")
# article2 = Article(title="article2")
#
# tag1 = Tag(name='tag1')
# tag2 = Tag(name='tag2')
#
# article1.tags.append(tag1)
# article1.tags.append(tag2)
#
# article2.tags.append(tag1)
# article2.tags.append(tag2)
#
# session.add(article1)
# session.add(article2)
#
# session.commit()

article = session.query(Article).first()
print(article.tags)

tag = session.query(Tag).first()
print(tag.articles)