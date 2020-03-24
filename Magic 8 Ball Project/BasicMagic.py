import random
import sys

answers = ['IT IS CERTAIN','YOU MAY RELY ON IT','AS I SEE IT,YES', 'OUTLOOK LOOKS GOOD','MOST LIKELY','IT IS DECIDELY SO','WITHOUT A DOUBT','YES,DEFINITELY']
endofAnswers = len(answers)
prompt = True

while prompt:
    randomNumber = random.randint(0,endofAnswers)
    question = input("Please ask me a question.")
    if question == "":
        sys.exit()
    else:
        print(answers[randomNumber])

