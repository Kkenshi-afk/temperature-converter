import json
import random


with open("questions.json", "r") as f:
    questions = json.load(f)


score = 0
total = len(questions)  


question_number = 1
for q in questions:
    print("\nQuestion", question_number, "/", total, ":", q["question"])

    
    choices = list(q["choices"])

    
    random.shuffle(choices)

    
    index = 1
    for choice in choices:
        print(index, ")", choice)
        index += 1

    
    while True:
        cevap = input("Your selection (number): ")
        if cevap.isdigit():
            selection = int(cevap)
            if 1 <= selection <= len(choices):
                break
        print("Invalid login, try again!")

    
    if choices[selection - 1] == q["answer"]:
        print("✅ True!")
        score += 1
    else:
        print("❌ Wrong. correct answer:", q["answer"])

    
    question_number += 1


print("\nFinished! Your score:", score, "/", total)
