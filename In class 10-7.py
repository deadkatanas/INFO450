# Assignment 1

textList = ['Beware the Jabberwock, my son,',  'the jaws that bite, the claws that catch,', 'Beware the JubJub bird and shun', 'the frumious bandersnatch']
file = "caroll.txt"

with open(file, 'w') as file_object:
    
    for i in textList:

        file_object.write(i+"\n")



longestLine = ""



with open(file, 'r') as file_object:
    

    for line in file_object:

        out = file_object.readline()

        #print(line)
        #print(out)


        if len(out) > len(longestLine):

            longestLine = out




print(longestLine.strip('\n'))
print(len(longestLine) )





print(longestLine.lower())
