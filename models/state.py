#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
       
class State(BaseModel, Base):
    """ State class """
    from sqlalchemy.orm import relationship
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                        cascade="all, delete")

else:
    
    class State(BaseModel):
        """File Storage State Class"""
        name = ""
        
        @property
        def cities(self):  # +T6
            """Returns a list of City instances with state_id = id"""
            cities = []
            for thing in models.storage.all(City).values():
                if thing.state_id == self.id:
                    cities.append(thing)
            return cities
