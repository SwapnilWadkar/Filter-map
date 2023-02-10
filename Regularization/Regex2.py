import re
address = "78, hi 11     89 Main, 4th Cross, 123, Road, Marthalli, 5678 Bangalore, 560023, 67893 45"

# lastvalue= re.findall(r"\d",address)
# print(lastvalue)

# lastvalue = re.findall(r"\d+",address)
# print(lastvalue)

lastValues = re.findall(r"\d{6}", address)
print(lastValues)

lastValues = re.findall(r"\s\d{2}\s",address)
print(lastValues)

lastValues = re.findall(r"^\d{2}",address)
print(lastValues)
print("----------------")
lastValues = re.findall(r"\d{1,6}",address)
print(lastValues)
print("----------------")
