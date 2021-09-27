input_text="this is a sample text with several words "
input_text+="this is a more same text with different words"

word_dict=dict()

list=input_text.split()

##print(list)

for name in list:
    if name not in word_dict:
        word_dict[name] = 1
    else:
        word_dict[name] += 1


print(word_dict) 



student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}


print(student[1]["age"])