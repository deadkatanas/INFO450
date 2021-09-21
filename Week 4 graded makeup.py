
student_list=[['Harry', 37.31], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39], ["Mike", 27], ["Ella", 90]]

scores =[]
for names in student_list:
    scores.append(names[1])



sorted_score = sorted(scores)

print("Name   Score")
n=0


for number in sorted_score:
    #print(number)
    x = scores.index(number)
    #print(x)
    #print(i)
    print(student_list[x][0] + "   " + str(student_list[x][1]))