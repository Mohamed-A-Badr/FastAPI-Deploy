from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

# * This is the database URL that will be used to connect to the database and create the tables

# TODO: Just uncomment your Database url and comment the other one
# TODO : Thanks Bro <3

# RDS Database
# SQLALCHEMY_DATABASE_URL = "postgresql://robobrain:graduation@gp.cdotyt702xan.eu-north-1.rds.amazonaws.com/graduation_project"

# Local Database
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:manga2023@localhost/db1"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:mypassword@localhost/GP-Database"

# Heroku Database
SQLALCHEMY_DATABASE_URL = "postgresql://dkiecfiabhrwhm:3f1f64e261703d9e2ef100f4799c5d7c5e266e7684ce7b0b050f66a99b262bcb@ec2-3-208-74-199.compute-1.amazonaws.com:5432/d8sdvil3outl59"

# * Create the engine that will be used to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# * Create the base that will be used to create the tables in the database
Base = declarative_base()

# * Create the session that will be used to create the tables
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


# * Create a function that will be used to get the database session and close it after the request is done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
