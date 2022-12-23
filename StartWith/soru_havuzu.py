import pandas as pd
import random 

def questions():
    questions = ["Hello, how are you? ","What is your name?","How old are you?"]
    random_question = random.choice(questions)
    return random_question