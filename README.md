<<<<<<< HEAD
# Virtual AI Tutor

An AI-powered learning support web application that lets students ask questions, practise subject-based quizzes, view quiz scores, and receive learning recommendations with useful study resources.

## Features

- **AI Tutor:** Answers student questions using a Hugging Face text-generation model.
- **Learning levels:** Supports beginner, intermediate, and advanced prompts.
- **Subject-based quizzes:** Quiz topics include Python, Artificial Intelligence, and Machine Learning.
- **Quiz scoring:** Calculates the learner's score and percentage.
- **Personalized learning recommendations:** Uses a Scikit-learn Decision Tree classifier to suggest a next learning action based on quiz score and attempt count.
- **Study resources:** Displays links relevant to the recommended next step.
- **Web interface:** HTML, CSS, and JavaScript frontend served by FastAPI.

## Technology Stack

- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Scikit-learn
- HTML, CSS, JavaScript

## Project Structure

```text
virtual-ai-tutor-new/
├── main.py
├── tutor.py
├── quiz.py
├── recommender.py
├── static/
│   ├── index.html
│   └── style.css
└── venv/
```

The `venv/` folder is a local Python virtual environment and normally should not be committed to GitHub.

## Setup and Run

### 1. Open the project folder

Open a terminal in the project root.

### 2. Activate the virtual environment (Windows PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

If activation is blocked or you prefer not to activate it, run Uvicorn directly:

```powershell
.\venv\Scripts\python.exe -m uvicorn main:app --reload
```

### 3. Start the application

```powershell
python -m uvicorn main:app --reload
```

On first launch, the Hugging Face model may need to download, so startup can take time and requires an internet connection.

### 4. Open the app

- Website: http://127.0.0.1:8000/app
- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

Stop the server with `Ctrl+C`.

## How to Use

1. Open the website.
2. Enter a question in the AI Tutor and choose a learning level.
3. Choose a quiz subject and start the quiz.
4. Submit answers to see the score and percentage.
5. Review the learning recommendation and open the suggested resources.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic application status |
| GET | `/health` | Health check |
| GET | `/app` | Serves the frontend |
| POST | `/ask` | Generates a tutor answer |
| GET | `/quiz?subject=Python` | Loads quiz questions; `subject` can be `all`, `Python`, `AI`, or `Machine Learning` |
| POST | `/quiz/submit` | Grades quiz answers |
| POST | `/recommend` | Returns a learning recommendation and resources |

Use `/docs` to inspect the API request schemas.

## Machine Learning Recommendation Note

The current recommendation classifier is a demonstration model trained on a small, manually defined sample dataset. It illustrates how a Decision Tree can map quiz scores and attempt counts to learning suggestions. It has **not** been trained on real student histories and should not be described as a validated educational assessment model.

## Limitations and Future Improvements

- Expand and review the quiz question bank.
- Improve answer quality with a stronger model and more robust prompt formatting.
- Store learner progress in a database across sessions.
- Add authentication and student profiles if required.
- Evaluate recommendations using a larger, representative dataset.
- Add tests, deployment configuration, and accessibility checks.

## Troubleshooting

- If the app does not open, confirm the terminal is running Uvicorn from the project root.
- If the model is loading, wait for the model-loaded message; the first startup may take several minutes.
- If an import error appears, install the required dependencies in the project's virtual environment.
- If subject filtering returns no questions, check that the topic names in `quiz.py` match the dropdown values and backend filter logic.

## Acknowledgements

Built as a student hackathon project to demonstrate AI-assisted learning, quiz-based practice, and ML-driven study recommendations.
=======
# virtual-ai-tutor
>>>>>>> b8dbae0563224aa9a10f0f6840865cf2545269aa
