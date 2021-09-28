
# dictionary and variables that will be used
states = dict()
userStateInput = ""
userFactInput = ""

# loop to check for state or end
while userStateInput != "q": 

    userStateInput = input("Enter a state or q to quit: ")

    # Makes sure rest of code does not run when user enters "q"
    if userStateInput != "q": 

        # creation of list as value 
        states[userStateInput] = [] 

        # loops until user enters q, then back to state
        while userFactInput != "q": 

            userFactInput = input("Enter a fact about your state, type q when done: ")
        
            # Another check to see if user enters "q" for facts to append 
            if userFactInput != "q":

                states[userStateInput].append(userFactInput)
                


        # To make sure user does not get stuck in state input loop
        userFactInput = "" 


## To check dictionary outputs (optional)
print(states)