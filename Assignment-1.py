verse = "If you can keep your head when all about you\n Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n And yet don’t look too good, nor talk too wise:"

print(len(verse))

char_test= str(verse[12])
result= char_test.isupper()
print(result)


print('verse[12]'.isupper())


a = 'theirs and'
b = 'and not'
verse = verse.split(a)[-1].split(b)[0]
print(verse.strip())
