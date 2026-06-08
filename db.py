from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

# Replace with your actual PostgreSQL credentials
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# SQLAlchemy Setup
engine = create_engine(DATABASE_URL,echo=True)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Define a sample table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    city=Column(String)

# Create the table
Base.metadata.create_all(engine)

# # Dependency to get DB session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Sample route to create a user
# @app.post("/users/")
# def create_user(name: str, age: int, db: Session = Depends(get_db)):
#     new_user = User(name=name, age=age)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

Session = sessionmaker(bind=engine)
session = Session()
session.add_all([
    User(name='mukhesh',age=22,city="hyd"),
    User(name='khesh',age=21,city="kakinada"),
    User(name='hesh',age=20,city="khaja")

])
session.commit()
session.close()
