# This project was built with the following instructions from the course:
## Complete Python Programming Masterclass Beginner to advanced

Instructions:
1. Create a single Python File (.py)

2. Two modules need to be imported into your python file 'sys' module and 'random'

3. When a user runs the project, they should receive a prompt (printed message), asking them to
ask the magic 8 ball a question

4. The user will then type in a question and press the enter key.

5. Logic, built in the code, will then return a random response from the following:
  -IT IS CERTAIN
  -YOU MAY RELY ON IT
  -AS I SEE IT, YES
  -OUTLOOK LOOKS GOOD
  -MOST LIKELY
  -IT IS DECIDEDLY SO
  -WITHOUT A DOUBT
  -YES, DEFINITELY
  
6. The program should continue to run in a loop, returning a random answer to each question the person asks
If the user doesn't enter a question and presses the enter key the application should quit

# The second project had the following instructions:
Import the following modules: 
Random, Sys, and CSV

Build a class structure called magic8ball
Create a class __init__ method
Pass in the "self and "name" argument
Private property should be included called "__mQuestions" and make it equal to an empty list

Adding in the functionality: 
Create a new private method called "__start_game"
  Include Self Argument
This method will do the bulk of the work 
  Create a loop to prompt the user with a question
  If a question is asked it should return a random answer. if no question is asked then it should exit.
Each question asked should be appended to the “__mQuestions” list from the __init__ method

Lastly create a private method called "__write_questions"
  Include the "self" argument
Using the csv module this method should write all the questions to the provided “magic_questions.csv” document when the user exits the game.
  



