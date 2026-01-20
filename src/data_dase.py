from sqlalchemy.orm import create_engine , sessionmaker

DATABASE_URL = ""

session = sessionmaker(autofulsh=False,bind=create_engine(DATABASE_URL))
