# write a program will find all such numbers which are divisible by 7 but not multilple of 5
# condition : numbers to be between 2000 and 3200 both to be included
# result should be in a comma seperated sequence in a singlr line 

# nums =[]
# for i in range(2000,3200):
#     if (i%7==0) and (i%5!=0):
#         nums.append(str(i))
# print(",".join(nums))  

# Print Statement example

nums=[str(i) for i in range(2000,3200) if i%7==0 and i%5!=0]
print(','.join(nums))