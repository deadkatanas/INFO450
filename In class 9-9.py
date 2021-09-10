## problem 1
list1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
list1.sort(reverse=True)
#print(list1)



## problem 2
list2=[]
for i in range(0, 30):
    list2.append(i**2)
#print(list2[:6])



## problem 3
list3=['M', 'na', 'i', 'Mi']
list4=['y','me','s','ke']

list5=[i+j for i, j in zip(list3, list4)]
output=""
for word in list5:
    output += word
    output += " "

#print(list3[0]+list4[0]+" "+list3[1]+list4[1]+" "+list3[2]+list4[2]+" "+list3[3]+list4[3])
#print(output)


## Assignment 1

input_list=["Mike",60], ["Joe", 75], ["Sue", 85], ["Anne", 80], ["George", 75]

print(input_list)




## Assignment 2

#int=input("Enter an integer: ")



number_list = list(range(1, 21, 2))

for x in number_list:

     print(x)