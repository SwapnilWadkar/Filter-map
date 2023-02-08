# Take a sequence of userr inputs (numbers and comma seperated)
# sum of those numbers 
# input : 1,2,3,4,5
# output :15

#Approach 1
# userinput = input("Enter the number of numbers: ")
# print(userinput)
# lstnum = userinput.split(",")

# result = 0
# for i in lstnum:
#     result+=int(i)
# print(result)    

#approach 2
userinput = input("Enter the number of numbers: ")
lstnum = list(map(int, userinput.split(",")))
print(sum(lstnum))

