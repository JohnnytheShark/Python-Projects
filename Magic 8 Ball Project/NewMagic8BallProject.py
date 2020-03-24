import random, sys, csv
#Create the class
class magic8ball:
    #Initialize the game
    def __init__(self,name):
        self.__name = name
        self.__mQuestions = []
        self.__start_game()
    #Start the game
    def __start_game(self):
        responses = ['IT IS CERTAIN','YOU MAY RELY ON IT','AS I SEE IT,YES', 'OUTLOOK LOOKS GOOD','MOST LIKELY','IT IS DECIDELY SO','WITHOUT A DOUBT','YES,DEFINITELY']
        endofAnswers = len(responses)
        questions = True
        print("Welcome " + self.__name)
        while questions:
            mQuest = input("Input a yes or no question: ")
            randomNumber = random.randint(0,endofAnswers)
            if mQuest == "":
                print("You didn't input a question. Good-Bye")
                sys.exit()
            else:
                print(responses[randomNumber])
    