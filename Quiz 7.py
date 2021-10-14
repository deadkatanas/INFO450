
fileName = "accounts_rec.txt"
newFile = "updated_account_rec.txt"

list = []

with open(fileName) as file:

    for line in file:
        
        list.append(line.strip("\n"))
        
placeholder = []

newAccounts = dict()

for account in list:

    for word in account.split(" "):

        placeholder.append(word)


    newAccounts[placeholder[0]] = [placeholder[1], placeholder[2]]
    placeholder.clear()


for account in newAccounts:
    
    if newAccounts[account][0] ==  "White":
        newAccounts[account][0] = "Williamson"


    if account == "400":
       # int(newAccounts[account][1]) += 200
       break




with open(newFile, 'w') as file_object:


   for n in newAccounts:
       
       file_object.write(n+" " )

       for value in newAccounts[n]:
           file_object.write(value)








#print(newAccounts)

#with open(newFile, 'w') as file:

