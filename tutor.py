
from transformers import pipeline

print("Loading AI tutor model...")

tutor_model = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

print("AI tutor model loaded successfully!")


def generate_answer(question, level="beginner"):
    prompt = (
        f"You are a helpful AI tutor. Explain the answer at a "
        f"{level} level using simple language.\n"
        f"Student question: {question}\n"
        f"Tutor answer:"
    )

    result = tutor_model(
        prompt,
        max_new_tokens=120,
        do_sample=False,
        return_full_text=False
    )

    return result[0]["generated_text"].strip()
