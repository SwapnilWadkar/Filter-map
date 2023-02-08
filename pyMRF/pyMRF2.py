nums = range(1,11)

even= lambda n :n%2== 0

filterobj = filter(even, nums)
print("Result using filter- even : ", list(filterobj))

mapobj= map(even,nums)
print("Result using map - even: ",list(mapobj))