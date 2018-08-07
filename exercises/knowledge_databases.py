from knowledge_model import Base, Tv_rating

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,tv_show,rating,gener):
	tvv=Tv_rating(
		name=name,
		tv_show=tv_show,
		rating=rating,
		gener=gener)
	session.add(tvv)
	session.commit()
add_article("hthr","the big bang",10,"comedy")

def query_all_articles():

	return session.query(Tv_rating).all()


def query_article_by_name(name1):
	return session.query(Tv_rating).filter_by(name=name1).all()
	
print(query_all_articles())
#print(query_article_by_name("hthr"))
def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
