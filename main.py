import requests
import random
import time

amt = 0
difficulty = ""
link = ""
score = 0
questions = []
answers = {}
data = {}
difficulties = {"e": "easy", "m": "medium", "h": "hard"}
print("Welcome to the True/False General Knowledge Trivia!")

def ask():
    global amt
    global difficulty
    global link
    global data
    amt = int(input("How many questions would you like to be quizzed on? "))
    difficulty = input("Enter a difficulty:\n[E] Easy\n[M] Medium\n[H] Hard\n-------------\n")
    link = f"https://opentdb.com/api.php?amount={amt}&category=9&difficulty={difficulties[difficulty.lower()]}&type=boolean"
    quiz = requests.get(link)
    data = quiz.json()
    if data["response_code"] == 1:
        print("There are no questions available for the information you have entered")
        time.sleep(1)
        ask()


try:
    ask()
    for i in data["results"]:
        question = i["question"]
        if "&#039;" in question:
            question = question.replace("&#039;", "'")
        if "&quot;" in question:
            question = question.replace("&quot;", '"')
        questions.append(question)
        answers[question] = i["correct_answer"]

    print("-------------\nStarting Quiz...")
    for i in questions:
        answer = input(f"{i} True/False ")
        if answer.lower() == answers[i].lower():
            print("That's Correct")
            score +=1
        else:
            print("Incorrect")

    if (score / amt) * 100 >= 70:
        print(f"Amazing! You got {score} out of {amt} questions correct")
    elif (score / amt) * 100 < 50:
        print(f"Oh no! You got {score} out of {amt} questions correct")
    else:
        print(f"Nice! You got {score} out of {amt} questions correct, but you've got some learning to do")

except KeyError:
    print("You have entered invalid data")

