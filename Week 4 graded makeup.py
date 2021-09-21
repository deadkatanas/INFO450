#create list
student_list=[['Harry', 37.31], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39], ["Mike", 27], ["Ella", 90]]

#loop to create second list of just scores to sort
scores =[]
for names in student_list:
    scores.append(names[1])

#sort scores min to max
sorted_score = sorted(scores)
print("Name   Score")

#loop to print names and scores based on score list using index to find pair 
for number in sorted_score:
    x = scores.index(number)
    print(student_list[x][0] + "   " + str(student_list[x][1]))