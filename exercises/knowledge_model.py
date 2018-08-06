from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Tv_rating(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__ ='tv rating'
	person_id=Column(Integer,primary_key=True)
	name=Column(String)
	tv_show=Column(Integer)
	rating=Column(Integer)
	gener=Column(String)

tv1=Tv_rating(person_id=1,name='noa',tv_show='the 70s show',rating=8.5,gener='comedy')
tv2=Tv_rating(person_id=2,name='jeniffer',tv_show='The house of cards',rating=5,gener=' political thriller ')
tv3=Tv_rating(person_id=3,name='john',tv_show='13 reasons why',rating=10,gener='teen drama')

def __repr__(self):
		return ("I love watching tv shows,especially the gener:  {}\n"
				"an example of a tv show is {}\n"
				"and I gave it rating of: {}\n"
				"my name is:{}").format(
					self.gener,
					self.tv_show,
					self.rating,
					self.name)
