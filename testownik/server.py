from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from core import QuestionModel, ExamGenerator
from pathlib import Path

app = FastAPI()
exam_generator = ExamGenerator()

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


@app.get("/", response_model=List[QuestionModel])
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
