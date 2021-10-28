#def math():
#    if True and False:
#        return 8

#    elif False:
#        return 7
    
#    return 3


#x = math()

#print(x)

#######################

#def list_printer(my_list=[]):

#    if my_list != None and my_list:
#        print(my_list)

#    else:
#        print("No list found")



#list_printer()


############################


in_string= "world"
final_string= f"Hello, {in_string}!"
#print(final_string)

###############################

def function():
    return 1, 2, 3

x, _, _, = function()
#print(_)

################################

#for num in range(-2,-5,-1):
#    print(num, end=", ")





car={
    "number of doors": '4',
    "weight": "5,456 lbs",
    "color": "Black"
    }


def find_runner_up(score_list=[]):
    ru_score=""

    score_list.sort(reverse = True)
    print(score_list)

    if score_list == None:
        ru_score = "None"

    elif len(score_list) == 0:
        ru_score = "None"
    
    elif score_list[0] == score_list[1]:
        
        counter = score_list[0]
        list_len = score_list.count(counter)
        
        if len(score_list) == list_len:
            ru_score = "None"

        else:
            ru_score = score_list[score_list.count(counter)]

    else:
        ru_score = score_list[1]

    return ru_score


out = find_runner_up([1,2,3,4,5,5,5,5,5,5,5,5,5])
print(out)