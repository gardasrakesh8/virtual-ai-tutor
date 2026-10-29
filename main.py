
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI
from pydantic import BaseModel

from tutor import generate_answer
from quiz import get_quiz, grade_quiz
from recommender import recommend_learning

app = FastAPI(title="Virtual AI Tutor")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/app")
def serve_website():
    return FileResponse("static/index.html")


# -------------------------------
# 1. Request models
# -------------------------------

class TutorQuestion(BaseModel):
    question: str
    level: str = "beginner"


class QuizSubmission(BaseModel):
    answers: dict[int, str]


class RecommendationRequest(BaseModel):
    score: int
    attempts: int = 1


# -------------------------------
# 2. Home endpoint
# -------------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to Virtual AI Tutor!",
        "status": "AI Tutor is running"
    }


# -------------------------------
# 3. Health check endpoint
# -------------------------------

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# -------------------------------
# 4. Ask the AI tutor
# -------------------------------

@app.post("/ask")
def ask_tutor(data: TutorQuestion):
    question = data.question.strip()

    if not question:
        return {"answer": "Please enter a question."}

    answer = generate_answer(question, data.level)

    return {
        "question": question,
        "level": data.level,
        "answer": answer
    }


# -------------------------------
# 5. Get quiz questions
# -------------------------------

@app.get("/quiz")
def show_quiz(subject: str = "all"):
    return {"questions": get_quiz(subject)}

# -------------------------------
# 6. Submit quiz answers
# -------------------------------

@app.post("/quiz/submit")
def submit_quiz(data: QuizSubmission):
    return grade_quiz(data.answers)


# -------------------------------
# 7. Get a learning recommendation
# -------------------------------

@app.post("/recommend")
def learning_recommendation(data: RecommendationRequest):
    score = max(0, min(100, data.score))
    attempts = max(1, data.attempts)

    return recommend_learning(score, attempts)
