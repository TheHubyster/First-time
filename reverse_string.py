# variables
strg = "12345" # initial string
stlen = len(strg) # length of string
print(strg) # print initial string

counter = stlen -1 # counter
newstrg = "" # blank string
for rev in range(stlen):
    newstrg += strg[counter] # newstiring has initial string added
    counter = counter -1 # counter counts down

print(newstrg) # print new string in reverse
