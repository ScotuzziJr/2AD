from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

# object that holds our models in metadata form
base = declarative_base() 

# SOLID principle applied - Single Responsability Principle
#   A class should do one thing and therefore it should have only a single reason to change

# Each class represents a model in our ORM (or a table in our relational database)
# Thinking of OOP in general, each model class acts like a data container and that's the reason we're 
# separating them, because a Distro class, for example, should only change if our model changes

class Distro(base):
    __tablename__  = "distro"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name           = Column(String)
    description    = Column(String)
    based_on       = Column(String)
    desktop        = Column(String, ForeignKey("desktop.name"))
    kernel         = Column(String, ForeignKey("kernel.name"))
    latest_version = Column(String)
    website        = Column(String)

    desktop_ref    = relationship("Desktop", backref="distro")
    kernel_ref     = relationship("Kernel", backref="distro")
    
    def __repr__(self):
        return f"<Distro(name={self.name}, kernel={self.kernel}, version={self.latest_version})>"

class Desktop(base):
    __tablename__  = "desktop"

    id             = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name           = Column(String, primary_key=True)
    latest_version = Column(String)

    def __repr__(self):
        return f"<Desktop(name={self.name}, version={self.latest_version})>"

class Kernel(base):
    __tablename__  = "kernel"

    id             = Column(UUID(as_uuid=True), default=uuid.uuid4)
    name           = Column(String, primary_key=True)
    latest_version = Column(String)

    def __repr__(self):
        return f"<Kernel(name={self.name}, version={self.latest_version})>"
