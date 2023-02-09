# write a program where the out to a sequence of numbers is cubes in a dictionary
# seq: 2 to 20 both included
# output: (2:8,3:27......)

start = int(input("Enter the starting number: "))
End = int(input("Enter a ending number : "))
result={}
for i in range (start,End+1):
    result[i] = i**3
print(result)    