from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from core import Examiner
from question_model import Question, SESSION  # Import Session
from pathlib import Path

app = FastAPI()
exam_generator = Examiner()

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

CURRENT_SET = next(exam_generator.generate_exam())


@app.get("/next")
async def next_question(request: Request):
    global CURRENT_SET
    try:
        CURRENT_SET = next(exam_generator.generate_exam())
    except StopIteration:
        CURRENT_SET = []
    return RedirectResponse(url="/", status_code=303)


@app.get("/answer/{question_id}/{correct}")
async def answer_question(question_id: int, correct: bool):
    with SESSION() as session:
        # Update tries in the database
        exam_generator.add_tries(question_id, correct)

        # Find the question in CURRENT_SET and update its attributes
        for question in CURRENT_SET:
            if question.id == question_id:
                # Re-fetch the question to get updated tries
                updated_question = session.query(Question).get(question_id)
                question.total_tries = updated_question.total_tries
                question.correct_tries = updated_question.correct_tries
                break

    return RedirectResponse(url="/", status_code=303)


@app.get("/")
async def get_questions(request: Request):
    return templates.TemplateResponse(
        "questions.html",
        {
            "request": request,
            "questions": CURRENT_SET,
            "questions_left": exam_generator.questions_left,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
