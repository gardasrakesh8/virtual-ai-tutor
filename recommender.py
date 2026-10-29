
from sklearn.tree import DecisionTreeClassifier

# Sample training data: [quiz score, number of attempts]
X = [
    [20, 1], [35, 1],
    [45, 2], [60, 2],
    [75, 3], [90, 3],
    [95, 4]
]

y = [
    "Revise fundamentals",
    "Revise fundamentals",
    "Practise more questions",
    "Practise more questions",
    "Study the next topic",
    "Study the next topic",
    "Try advanced questions"
]

# Train the recommendation model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Learning resources for each recommendation
RESOURCES = {
    "Revise fundamentals": [
        {
            "title": "Python Tutorial",
            "url": "https://docs.python.org/3/tutorial/"
        },
        {
            "title": "Machine Learning Crash Course",
            "url": "https://developers.google.com/machine-learning/crash-course"
        }
    ],
    "Practise more questions": [
        {
            "title": "Python Practice",
            "url": "https://www.w3schools.com/python/"
        },
        {
            "title": "Machine Learning Exercises",
            "url": "https://www.kaggle.com/learn/intro-to-machine-learning"
        }
    ],
    "Study the next topic": [
        {
            "title": "Scikit-learn Tutorials",
            "url": "https://scikit-learn.org/stable/tutorial/index.html"
        },
        {
            "title": "Kaggle Learn",
            "url": "https://www.kaggle.com/learn"
        }
    ],
    "Try advanced questions": [
        {
            "title": "Advanced Python",
            "url": "https://docs.python.org/3/"
        },
        {
            "title": "Advanced Machine Learning",
            "url": "https://scikit-learn.org/stable/"
        }
    ]
}


def recommend_learning(score, attempts=1):
    score = max(0, min(100, score))
    attempts = max(1, attempts)

    recommendation = model.predict([[score, attempts]])[0]

    return {
        "score": score,
        "attempts": attempts,
        "recommendation": recommendation,
        "resources": RESOURCES[recommendation]
    }
