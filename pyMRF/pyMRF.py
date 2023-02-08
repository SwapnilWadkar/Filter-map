nums = range(1,11)
print("Number :",nums)

sq= lambda n: n*n
# Approach 1
# result = []
# for i in nums:
#     result.append(sq(i))
# print(result)   

# Approach 2
# result =[sq(i) for i in nums ]
# print("Result :",result)

#approach 3
#using map
mobject = map(sq, nums)
print("List of squares of numbers :", list(mobject))