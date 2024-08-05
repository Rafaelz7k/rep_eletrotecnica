import json

w_theme = ""
question_text = ""
options = [
    "",
    "",
    "",
    ""
]

correct_option = ""
explanation = ""

question_dict = {
    "theme": w_theme,
    "question": question_text,
    "options": options,
    "correct": correct_option,
    "explanation": explanation
}

try:
    with open("questions.json", "r", encoding="utf-8") as file:
        questions = json.load(file)
except FileNotFoundError:
    questions = []

questions.append(question_dict)

with open("questions.json", "w", encoding="utf-8") as file:
    json.dump(questions, file, indent=4, ensure_ascii=False)