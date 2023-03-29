from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

from models import Pet, Owner, Job, Handler

if __name__ == '__main__':
    engine = create_engine('sqlite:///pet_app.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    def _fk_pragma_on_connect(dbapi_con, con_record):
        dbapi_con.execute('pragma foreign_keys=ON')
    event.listen(engine, 'connect', _fk_pragma_on_connect)

#2.a ✅ Add delete methods for Pet and Owner to clear the database before each seeding
    
    

    # faker=Faker()

    # owner_1=Owner(faker.name(),faker.email(),faker.phone_number(),faker.address())
    # session.add(owner_1)
    # session.commit()

    # owner_1=session.query(Owner).first()

    # pet_1=Pet(faker.name(),faker.name(),faker.name(),faker.name(),owner_1.id)
    # session.add(pet_1)
    # session.commit()
#----------
#5.✅ Add Delete methods for Job and Handler
    session.query(Job).delete()
    session.query(Pet).delete()
    session.query(Owner).delete()
    session.query(Handler).delete()
    #Initialize faker
    faker=Faker()
    #Create an array for species with "CAT" and "Dog"
    species=['cat','dog']
    #Create an array of cat breeds
    cat_breeds=["bob cat","house cat"]
    #Create an array of dog breeds
    dog_breeds=['beagle','german shepard']
    #Create an array of temperaments 
    temperament=["loving","playful"]
    #Create an empty array for owners
    owners=[]
    owner=None
    #Create a for loop that iterates 50 times
    for i in range(50):
        #Create an owner using data from faker
       owner=Owner(faker.name(),faker.email(),faker.phone_number(),faker.address())
       session.add(owner)
       session.commit()
       owners.append(owner)

        #Use .add and .commit to save the owner one at a time, so we maintain the owner ID in our instance.
       
        #Append the owner to the owners array
       
    
    #Create an empty pets array
    pets=[]
    pet=None
    #Create a for loop that iterates over the owners array
    for owner in owners:
        #Create a for loop that iterates 1 - 3 times
        for i in range(3):
            #Use faker and the species, cat breeds, dog breeds and temperament array to create a pet
            pet=Pet(faker.name,species[random.randint(0,1)],dog_breeds[random.randint(0,1)],temperament[random.randint(0,1)],(i+1))
            #Use .add and .commit to save the pet to the database
            session.add(pet)
            session.commit()
            pets.append(pet)
            #Append the pet to the pets array
            
#3✅ run the seed file and head over to debug.py to test out your one to many
#----------------------------------------------------- 

#5.✅ Create a empty array set to handlers
    handlers=[]
    handler=None
    #Create a for loop that iterates 50 times
    for i in range(50):
        #Create a handler with faker data 
       handler=Handler(faker.name(),faker.email(),faker.phone_number(),random.randint(0,100))
       session.add(handler)
       session.commit()
       handlers.append(handler)
        #Use .add and .commit to save the handler to the database
        
        #Append handler to handlers
        
    
    #Create an array of requests, "Walk", "Drop-in" and "Boarding"
    request=["walk","drop-in","boarding"]
    #Create an empty array and set it to jobs
    jobs=[]
    job=None
    #Create a for loop that iterates over the handlers array
    for handler in handlers:
        #Create a for loop that iterates 1 - 10 times
        for i  in range(10):
            #Create a Job using faker, the request array and pets array
            job=Job(request[random.randint(0,2)],faker.date_this_century(),handler.hourly_rate,random.randint(1,len(pets)-1),random.randint(1,len(handlers)-1))
            #append the job to the jobs array
            session.add(job)
            session.commit()
            jobs.append(job)  
        #Bulk save the jobs (we wont need their id)
    
    #session.commit()
    session.close()

#6.✅ Run the seeds file and head over to debug.py to test out your Many to Many 