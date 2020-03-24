import random, sys, csv
#Create the class
class magic8ball:
    #Initialize the game
    def __init__(self,name):
        #Create a new class with the given name
        self.__name = name
        #Empty list of Questions to be appended to later
        self.__mQuestions = []
        #Call to function later to be able to start the game
        self.__start_game()
    #Start the game
    def __start_game(self):
        #List/Array of Responses that are possible to return to the audience
        responses = ['IT IS CERTAIN','YOU MAY RELY ON IT','AS I SEE IT,YES', 'OUTLOOK LOOKS GOOD','MOST LIKELY','IT IS DECIDELY SO','WITHOUT A DOUBT','YES,DEFINITELY']
        #The length of the list
        endofAnswers = len(responses)
        #Declare a true variable to be able to run the code below
        questions = True
        #Welcome the user to the game
        print("Welcome " + self.__name)
        #Start the loop
        while questions:
            #Declare that the audience needs to input a yes or no question
            mQuest = input("Input a yes or no question: ")
            #This chooses a random response from the beginning of the list to the end of the list
            randomNumber = random.randint(0,endofAnswers)
            #If statement to see if the user has input a question
            if mQuest == "":
                #Close the loop
                print("You didn't input a question. Thank you for playing.")
                #Write all the questions that the user asked
                self.__write_questions()
                #Exit the game
                sys.exit()
            else:
                #print a random response
                print(responses[randomNumber])
                #append the question to the loop
                self.__mQuestions.append(mQuest)
    #Define another method. This function is used to write out to the CSV File
    def __write_questions(self):
        #Open the file
        f = open("magic_questions.csv", "a", newline="")
        #Declare a writer
        wrt = csv.writer(f)
        #For each question that was asked write it out
        for q in self.__mQuestions:
            wrt.writerow([q])
        #Close the file
        f.close()
    