
#list given
list1=[[5,7,8,7,"a","b","a",5],[6,9,0,9,6,0]]
 



#trying to iterate through the list to append
for i in list1:
    singletons = []
    for j in list1[i]:
        print(j)
        for k in list1[i]: 
            count = 0
            if j == list1[i][k]:
                count = count = 1
        if count == 1:
            singletons.append(j)
    print(list1[i])
    print(singletons)


# messages meant to print at the end 
#print("List " + list1[0] + " has the following singletons ")

#print("List " + list1[1] + " has the following singletons ")