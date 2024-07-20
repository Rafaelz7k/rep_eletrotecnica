import json
import random

def load_questions(file_questions):
    with open(file_questions, 'r', encoding='utf-8') as file:
        return json.load(file)

def ask_question(question):
    print(f"{question['question']}")
    for idx, option in enumerate(question['options'], start=1):
        print(f"{idx}. {option}")
    
    answer = input("Resposta: ")
    return int(answer) - 1

def check_answer(question, user_answer):
    correct_answer = question['correct']
    correct_idx = question['options'].index(correct_answer)
    if user_answer == correct_idx:
        print("Resposta correta!")
        return True
    else:
        print(f"Resposta errada! {question['explanation']}")
        return False

def main():
    questions = load_questions('questions.json')
    print(f"Total de questões: {len(questions)}")
    random.shuffle(questions)
    
    for question in questions:
        user_answer = ask_question(question)
        check_answer(question, user_answer)
        print()

if __name__ == "__main__":
    main()
