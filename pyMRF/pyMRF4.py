# take a sequence of inputs (numbers and comma seperated)
# sum of those numbers 
# input(1,2,3,4,5)
# output=15

userinput = input("Numbers with comma seperated :")

# lastnum = list(map(int, userinput.split(",")))
# print(sum(lastnum))
 

print(userinput)
lastnum =userinput.split(",")

result = 0
for i in lastnum:
    result+=int(i)
print(result)    
