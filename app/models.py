#1.✅ Update our models to include a One to Many association
# Pet >- Owner

#Import ForeignKey
from sqlalchemy import (PrimaryKeyConstraint, ForeignKey, Column, String, Integer, Float,  DateTime)

# import relationship and backref from sqlalchemy.orm 
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'
    __table_args__ = (PrimaryKeyConstraint('id'),)

    def __init__(self,name,species,breed,temperament,owner_id):
        self.id=None
        #self.name=name
        self.species=species
        self.breed=breed
        self.temperament=temperament
        self.owner_id=owner_id

    id = Column(Integer())
    name = Column(String())
    species = Column(String())
    breed = Column(String())
    temperament = Column(String())
    
    #1.a✅ Add  ForeignKey('owners.id') to owner)id
    owner_id = Column(Integer(),ForeignKey("owners.id"))


    
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Species {self.species}, "\
            + f"Breed {self.breed}, "\
            + f"Species {self.temperament} "\
            + f"Owner Id {self.owner_id}"

#1.b✅ Add an Owners table 
class Owner(Base):

    __tablename__="owners"

    def __init__(self,name,email,phone,address):
        self.id=None
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

    #Create the following columns
    # id -> type integer
    id=Column(Integer,primary_key=True)
    # name -> type string
    name=Column(String,nullable=False)
    # email -> type string
    email=Column(String,nullable=False)
    # phone -> type int
    phone=Column(Integer)
    # address -> type string
    address=Column(String)
    
    #1.c✅ Associate the Pet model with the owner Model
    pet=relationship('Pet', backref=backref('owner'))
    
    #add a __repr__ method that returns a string containing the id, name, email, phone and address of our class
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Address {self.address}"


#2.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

    # Note: If you still have your database from the previous lecture, you'll need to create a migration to update the pets table 
    # After running your migrations, go build out some seeds and test your one-to-many with debug.py
# -------------------------------

#4.✅ Update our Model to have a Many to Many association
# Pet-< Jobs >- Handlers

# Create a Handlers table 
class Handler(Base):

    __tablename__="handlers"

    def __init__(self,name,email,phone,hourly_rate):
        self.id=None
        self.name=name
        self.email=email
        self.phone=phone
        self.hourly_rate=hourly_rate

    #Create the following columns
    # id -> type integer
    id=Column(Integer,primary_key=True)
    # name -> type string
    name=Column(String,nullable=False)
    # email -> type string
    email=Column(String,nullable=True)
    # phone -> type int
    phone=Column(Integer)
    # hourly_rate -> type float
    hourly_rate=Column(Float,nullable=False)


   #add a __repr__ method that returns a string containing the id, name, email, phone and hourly_rate of our class
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Name:{self.name}, " \
            + f"Email: {self.email}, "\
            + f"Phone: {self.phone}, "\
            + f"Hourly Rate {self.hourly_rate}"


#Create a "jobs" table to serve as our join
class Job(Base):

    __tablename__="jobs"

    def __init__(self,request,date,fee,pet_id,handler_id):
        self.request=request
        self.date=date
        self.fee=fee
        self.pet_id=pet_id
        self.handler_id=handler_id

    #Create the following columns
    # id -> type integer
    id=Column(Integer,primary_key=True)
    # request -> type string
    request=Column(String,nullable=False)
    # date -> type datetime
    date=Column(DateTime,nullable=False)
    # fee -> type float
    fee=Column(Float,nullable=False)
    # pet_id -> type int with a ForeignKey('pet.id')
    pet_id=Column(Integer,ForeignKey("pets.id"))
    # handler_id -> type int with a ForeignKey('handlers.id') 
    handler_id=Column(Integer,ForeignKey("handlers.id"))
    

    #Associate the models with relationship(<ModelNameHere>, backref=backref(<TableNameHere>))
    pets=relationship("Pet",backref="jobs")
    hanlders=relationship("Handler",backref="jobs")

    #Add a __repr__ method that returns a string containing the id, request, date, notes, fee, pet_id and handler_id of our class
    def __repr__(self):
        return f"Id: {self.id}, " \
            + f"Request:{self.request}, " \
            + f"Date: {self.date}, "\
            + f"Fee: {self.fee}, "\
            + f"Pet Id {self.pet_id}"\
            + f"Handler Id {self.handler_id}"
    
#5.✅ Update your migrations by running `alembic revision --autogenerate -m` and `alembic upgrade head` 

#After running your migrations, go build out some seeds and test your many to many with debug.py
