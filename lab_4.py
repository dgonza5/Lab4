

"""
This program allows a user three tries to guess the correct answer to the question
question = "What is the captial of California". The answer is "Sacremento". 

We first set max_tries = 3. Then we create a loop iterate three times. For each iteration, 
we ask the user for the answer (user input). Then based on the answer the user gives, we check 
to see if the user input matches the answer. If so, print "Correct!", then termiate the loop with a 
break statement.

if the user could not guess the correct answer within the max_tries, then print 
"You have used up your allotment of guesses.", then print "The correct answer is "Sacramento".
"""

"""

main
    question = "What is the captial of California"
    answer = "Sacramento"
    ask(question, answer)
    

ask
    tries = 0
    loop three times
        increment tires by 1
        ask user input()
        check to see of user input is equal to the answer
            if so, print "Correct" then exit loop
    if not correct
        print to the user "You have used up your allotment of guesses."
        print the correct answer "The correct answer is "Sacramento""
        
main 
"""


def main():
    question = "What is the captial of California? "
    answer = "Sacramento"
    ask(question, answer)

def ask(question, answer, max_tries=3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries += 1
        ans = input(question) # Sacramento
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your allotment of guesses.")

main()


# == Equal 
# != Not Equal 
# > Greater Than 
# >= Greater than or equal to
# <
# <==