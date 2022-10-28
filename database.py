import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
#Url bdd Postgres
DATABASE_URL = "postgresql://postgres:password@localhost/fastapi_database"#nom de votre bdd

engine = _sql.create_engine(DATABASE_URL)
#Creation du session pour notre bdd avec sqlalchemy
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
