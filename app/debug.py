from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Owner, Pet, Handler, Job)

if __name__ == '__main__':

    engine = create_engine('sqlite:///pet_app.db')
    #Base.metadata.create_all(engine)
   
    Session = sessionmaker(bind=engine)
    session = Session()

    #3✅ One to Many
    #Getting an owners pets
    #Use session.query and first to grab the first owner
    first_owner=session.query(Owner).first()
    print(first_owner)
    print("\n\n")
    #use session.query and filter_by to get the owners pets from Pet
    pets=session.query(Pet).filter(Pet.owner_id==first_owner.id).all()
    for pet in pets:
        print(pet.breed)
    print("\n\n")
    #print out your owners pets
  

    #Getting a pets owner
    #Use session.query and first to grab the first pet
    first_pet=session.query(Pet).first()
    print(first_pet)
    print("\n\n")
    #Use session.query and filter_by to get the owner associated with this pet
    pet_owner=session.query(Owner).filter(Owner.id==first_pet.owner_id).first()
    print(pet_owner.name)
    print("\n\n")

    #4✅ Head back to models to build out a Many to Many 
#--------------------------------------------

#6.✅ Many to Many 
    #Use session.query and .first to get the first handler
    first_handler=session.query(Handler).first()
    print(first_handler)
    print("\n\n")
    #Use session.query and the .filter_by to grab the jobs
    jobs=session.query(Job).filter(Job.handler_id==first_handler.id).all()
    #Print the jobs
    for job in jobs:
        print(job)
    print("\n\n")
    #Use the handler_jobs to query pets for the associated pet to each job.
    for job in jobs:
        pet_id=session.query(Job.pet_id).filter(Job.h).first()
        print(pet_id)
    #Optional breakpoint for debugging
    #import ipdb; ipdb.set_trace()