
import random

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "topic": "Python",
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "def", "function", "define"],
        "correct_answer": "def"
    },
    {
        "id": 2,
        "topic": "Machine Learning",
        "question": "What does a machine learning model learn from?",
        "options": ["Data", "Only images", "Keyboards", "Electricity"],
        "correct_answer": "Data"
    },
    {
        "id": 3,
        "topic": "Python",
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "bool", "list"],
        "correct_answer": "bool"
    },
    {
        "id": 4,
        "topic": "AI",
        "question": "What does AI stand for?",
        "options": [
            "Automatic Internet",
            "Artificial Intelligence",
            "Advanced Input",
            "Applied Information"
        ],
        "correct_answer": "Artificial Intelligence"
    },
    {
        "id": 5,
        "topic": "Machine Learning",
        "question": "What is supervised learning?",
        "options": [
            "Learning from labelled examples",
            "Guessing without data",
            "Turning off a computer",
            "Deleting files"
        ],
        "correct_answer": "Learning from labelled examples"
    },
    {
        "id": 6,
        "topic": "Python",
        "question": "Which symbol starts a comment in Python?",
        "options": ["//", "#", "/*", "&"],
        "correct_answer": "#"
    },
    {
        "id": 7,
        "topic": "Python",
        "question": "Which collection stores items in an ordered, changeable sequence?",
        "options": ["tuple", "string", "list", "integer"],
        "correct_answer": "list"
    },
    {
        "id": 8,
        "topic": "Python",
        "question": "Which loop is commonly used to iterate over a list?",
        "options": ["repeat", "for", "repeat-until", "iterate"],
        "correct_answer": "for"
    },
    {
        "id": 9,
        "topic": "AI",
        "question": "Which is an example of artificial intelligence?",
        "options": [
            "A basic light switch",
            "A system that recognizes speech",
            "An ordinary notebook",
            "A simple ruler"
        ],
        "correct_answer": "A system that recognizes speech"
    },
    {
        "id": 10,
        "topic": "Machine Learning",
        "question": "What is a feature in a machine learning dataset?",
        "options": [
            "An input variable",
            "A computer screen",
            "A programming error",
            "A file extension"
        ],
        "correct_answer": "An input variable"
    },
    {
        "id": 11,
        "topic": "Machine Learning",
        "question": "What is the purpose of test data?",
        "options": [
            "To evaluate a trained model",
            "To delete the model",
            "To write comments",
            "To install Python"
        ],
        "correct_answer": "To evaluate a trained model"
    },
    {
        "id": 12,
        "topic": "Python",
        "question": "Which function displays output in Python?",
        "options": ["input()", "show()", "print()", "display_text()"],
        "correct_answer": "print()"
    },
    {
        "id": 13,
        "topic": "AI",
        "question": "Which field helps computers understand human language?",
        "options": [
            "Natural Language Processing",
            "Computer cabling",
            "File compression",
            "Screen design"
        ],
        "correct_answer": "Natural Language Processing"
    },
    {
        "id": 14,
        "topic": "Machine Learning",
        "question": "What is classification used for?",
        "options": [
            "Predicting categories",
            "Increasing screen brightness",
            "Formatting a document",
            "Renaming a folder"
        ],
        "correct_answer": "Predicting categories"
    },
    {
        "id": 15,
        "topic": "Python",
        "question": "Which keyword checks another condition after an if statement?",
        "options": ["otherwise", "elseif", "elif", "nextif"],
        "correct_answer": "elif"
    }
]

def get_quiz(subject="all"):
    if subject.lower() == "all":
        questions = QUIZ_QUESTIONS
    else:
        questions = [
            q for q in QUIZ_QUESTIONS
            if q["topic"].lower() == subject.lower()
        ]

    return [
        {
            "id": q["id"],
            "topic": q["topic"],
            "question": q["question"],
            "options": q["options"]
        }
        for q in random.sample(questions, min(5, len(questions)))
    ]


def grade_quiz(answers):
    """Calculate the student's score and topic performance."""
    score = 0
    topic_results = {}

    for question in QUIZ_QUESTIONS:
        question_id = question["id"]
        topic = question["topic"]

        if topic not in topic_results:
            topic_results[topic] = {"correct": 0, "total": 0}

        topic_results[topic]["total"] += 1

        if str(answers.get(question_id)) == question["correct_answer"]:
            score += 1
            topic_results[topic]["correct"] += 1

    total = len(answers)

    # Count only the questions answered in this quiz.
    selected_ids = {int(question_id) for question_id in answers}
    selected_questions = [
        question for question in QUIZ_QUESTIONS
        if question["id"] in selected_ids
    ]

    topic_results = {}
    for question in selected_questions:
        topic = question["topic"]

        if topic not in topic_results:
            topic_results[topic] = {"correct": 0, "total": 0}

        topic_results[topic]["total"] += 1

        if str(answers.get(question["id"])) == question["correct_answer"]:
            topic_results[topic]["correct"] += 1

    score = sum(
        1 for question in selected_questions
        if str(answers.get(question["id"])) == question["correct_answer"]
    )

    return {
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100) if total else 0,
        "topic_results": topic_results
    }
