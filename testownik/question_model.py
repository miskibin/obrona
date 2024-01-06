from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from questions import QUESTIONS
from sqlalchemy import inspect
from loguru import logger
from questions import get_question_url

Base = declarative_base()
ENGINE = create_engine("sqlite:///questions.db")
SESSION = sessionmaker(bind=ENGINE)


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer_url = Column(String)
    total_tries = Column(Integer, default=0)
    correct_tries = Column(Integer, default=0)

    def __repr__(self):
        return f"{self.id}: {self.question},  {self.correct_tries}/{self.total_tries})"


def read_questions_from_db():
    with SESSION() as session:
        questions = session.query(Question).all()
    return set(questions)


def create_and_populate_db():
    Base.metadata.create_all(ENGINE)
    inspector = inspect(ENGINE)
    tables = inspector.get_table_names()
    logger.info(f"Tables in database: {tables}")
    # check if questions table is empty
    if "questions" in tables:
        session = SESSION()
        if session.query(Question).first() is not None:
            logger.info("Database already populated.")
            return
    # Populate the database with questions
    session = SESSION()
    for key, question in QUESTIONS.items():
        session.add(
            Question(id=key, question=question, answer_url=get_question_url(key))
        )
    session.commit()
    logger.info("Database created and populated successfully.")


create_and_populate_db()
