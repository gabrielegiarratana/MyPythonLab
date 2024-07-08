from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):
    pass

class JobDependencies(Base):
    __tablename__ = "job_dependencies"
    new_job_id = Column(String, primary_key=True)
    dep_job_id = Column(String)

    def __init__(self, id: str, dep_id: str):
        self.job_id = id
        self.dep_job_id = dep_id
    def __repr__(self):
        return f"Job dependencies(id={self.job_id}, dep_job_id={self.dep_job_id!r})"

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/postgres")
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)



if __name__ == "__main__":

    new_job_id = "test orm"
    # init
    init_db()
    session = Session()

    #define new job dep
    new_job_dependency = JobDependencies(new_job_id, f"{new_job_id} dep")

    # adding new job dep
    session.add(new_job_dependency)
    session.commit()

    query = select(JobDependencies).where(JobDependencies.job_id == new_job_id)
    bird = session.execute(query).scalar_one()
    bird


    #deleting job dep
    session.delete(new_job_dependency)
    session.commit()
