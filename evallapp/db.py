from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.decl_api import DeclarativeMeta

import config

engine = create_engine(config.Config.SQLALCHEMY_DATABASE_URI)
db_session = scoped_session(
    sessionmaker(autoflush=False,
                 autocommit=False,
                 bind=engine)
)

Base: DeclarativeMeta = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from evallapp.models.core import Works, WorksMistakes, MistakesCodes, MistakesTypes, EducationProfile
    Base.metadata.create_all(bind=engine)
