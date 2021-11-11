
def user_input():
    end_seq = False
    while not end_seq:
        input_holder = input("Please enter a positive integer or q to quit ")

        if input_holder.lower() == "q":
            print("Thank you")
            end_seq = True
            final_input = 0

        else:
            try:
                input_holder = int(input_holder)

                if input_holder > 0:
                    final_input = input_holder
                    end_seq = True
                else:
                    print("Please enter a positive integer")
            except:
                print("Bad entry, try again ")

    return final_input



def p_triangle(row_wanted):
    
    starting_row = [1]

    if row_wanted == 1:
        return starting_row

    new_row = p_triangle(row_wanted - 1) #recursion

    for n in range(1, len(new_row)):
        final_row = new_row[n-1] + new_row[n]
        starting_row.append(final_row)

    starting_row.append(1)

    return starting_row


row_to_print = user_input()
print(p_triangle(row_to_print))