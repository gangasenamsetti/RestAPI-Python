# from sqlalchemy import create_engine
# #from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, declarative_base

# #DATABASE_URL="postgresql://username:password@localhost:5432/students_db"
# DATABASE_URL="postgresql://postgres:postgres@localhost:5432/students_new_db"
# engine=create_engine(DATABASE_URL,echo=True)

# SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base=declarative_base()



# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,Float,String
from pydantic import BaseModel

#user_name:password@localjost:5432
#create database products by right click on postgres/Databases
db_url="postgresql://postgres:postgres@localhost:5432/products"
engine=create_engine(db_url)
sessionmaker=sessionmaker(autocommit=False,autoflush=False,bind=engine)

from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Products(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True)
    price=Column(Integer)
    quantity=Column(Integer)

Base.metadata.create_all(bind=engine)

class Products(BaseModel):
    id:int
    price:int
    quantity:int

products_list=[
    Products(id=1,price=100,quantity=10),
    Products(id=2,price=100,quantity=10),
    Products(id=3,price=100,quantity=10),

]

def init_db():
    db=session()





