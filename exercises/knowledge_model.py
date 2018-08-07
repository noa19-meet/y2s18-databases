from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Tv_rating(Base):
	__tablename__ ='tv rating'
	person_id=Column(Integer,primary_key=True)
	name=Column(String)
	tv_show=Column(Integer)
	rating=Column(Integer)
	gener=Column(String)

	"""tv1=Tv_rating(person_id=1,name='noa',tv_show='the 70s show',rating=8.5,gener='comedy')
	tv2=Tv_rating(person_id=2,name='jeniffer',tv_show='The house of cards',rating=5,gener=' political thriller ')
	tv3=Tv_rating(person_id=3,name='john',tv_show='13 reasons why',rating=10,gener='teen drama')
	"""
	def __repr__(self):
		return ("I love watching tv shows,now im watching this gener:  {}\n"
				"an example of a tv show is {}\n"
				"and I gave it rating of: {}\n"
				"my name is:{}").format(
					self.gener,
					self.tv_show,
					self.rating,
					self.name)
