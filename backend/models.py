#!usr/bin/python
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base

# Create engine and metadata
engine = create_engine('sqlite:///brewbook.db')
metadata = MetaData(bind=engine)

# Reflect tables into Python classes
Base = automap_base(metadata=metadata)
Base.prepare()

# Access the reflected classes
recipes = Base.classes.recipes
beans = Base.classes.beans
brews = Base.classes.brews



