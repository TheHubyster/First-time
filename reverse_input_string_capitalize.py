# variables
strg = input("Enter your string: ") # user string
stlen = len(strg) # length of string
print(strg) # print initial string

counter = stlen -1 # counter
newstrg = "" # blank string

for rev in range(stlen):
    newstrg += strg[counter] # newstiring has initial string added
    counter = counter -1 # counter counts down

newstrg2 = newstrg.capitalize() # First character is capitalized
# using print("\n",newstr2) adds a new line without a leading space
print("\n" + newstrg2)