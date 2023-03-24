from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import DB_CONN_STRING
from .models import base
from .helpers.commons import recreate_database, populate_db

# stablishing db connection
db = create_engine(DB_CONN_STRING)
base.metadata.create_all(db)

# facotry of db session - we bind our 'db' variable which is running our engine
# the session allow us to perform operation over our db easily
Session = sessionmaker(bind=db)
s       = Session()

recreate_database(base, db)

populate_db(s)

# s.close()
