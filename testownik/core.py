from typing import Generator
import random
from question_model import Question, read_questions_from_db, SESSION
from loguru import logger
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class Examiner:
    empty_question = Question(
        id=0, question="Empty", answer_url="https://michalskibinski109.github.io/obrona"
    )

    def __init__(self):
        self.done_ids = set()
        self.questions = read_questions_from_db()

    @property
    def questions_left(self):
        return len(self.questions) - len(self.done_ids)

    def generate_exam(self) -> Generator[list[Question], None, None]:
        while True:
            questions = read_questions_from_db()
            questions = [q for q in questions if q.id not in self.done_ids]
            if len(questions) < 3:
                questions += [self.empty_question] * (3 - len(questions))
            ids = random.sample(range(len(questions)), 3)

            selected_questions = [questions[id] for id in ids]
            self.done_ids.update(q.id for q in selected_questions)
            yield selected_questions

            # Reset done_ids if all questions have been asked
            if len(self.done_ids) == len(self.questions):
                self.done_ids = set()

    def add_tries(self, question_id: int, correct: bool):
        with SESSION() as session:
            question = session.query(Question).get(question_id)
            question.total_tries += 1
            if correct:
                question.correct_tries += 1
            logger.info(f"Question {question_id} updated.")
            session.commit()
        return question
