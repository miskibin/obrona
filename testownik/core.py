from questions import QUESTIONS, get_question_url
from pydantic import BaseModel, AnyHttpUrl, validator
from typing import Generator, Optional
import random


class QuestionModel(BaseModel):
    id: int
    question: str
    answer_url: Optional[AnyHttpUrl] = None

    @validator("answer_url", always=True)
    def set_answer_url(cls, v, values):
        if "id" in values:
            return get_question_url(values["id"])
        return v


class ExamGenerator:
    empty_question = QuestionModel(
        id=0, question="Empty", answer_url="https://michalskibinski109.github.io/obrona"
    )

    def __init__(self):
        self.questions = list(QUESTIONS.items())

    @property
    def questions_left(self):
        return len(self.questions)

    def generate_exam(self) -> Generator[list[QuestionModel], None, None]:
        while self.questions_left > 0:
            if self.questions_left < 3:
                self.questions += [self.empty_question * (3 - self.questions_left)]
            ids = random.sample(range(len(self.questions)), 3)

            questions = [
                QuestionModel(id=self.questions[id][0], question=self.questions[id][1])
                for id in ids
            ]
            # remove questions from list
            self.questions = [q for i, q in enumerate(self.questions) if i not in ids]
            yield questions
