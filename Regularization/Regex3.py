import re
s = '''
<html>
<head>
<title>Current IP Address Allocations
</title>
</head>
<body>
IP Address are 172.45.78.109
LoopBack Address: 127.0.0.1
Computer 1: 10.67.89.101
Computer 2: 10.67.98.102
Computer 3: 12.68.98.102
</body>
</html>
'''
lstvalues=re.findall(r'\d+',s)
print(lstvalues)

lstvalue=re.findall(r'\d{3}',s)
print(lstvalue)

lstval=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
print(lstval)

lstva=re.findall(r"10.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print(lstva)