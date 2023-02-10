import re

sentense= "Welcome to Regex programming Language using python"

value= re.split(r"\s",sentense)
print("Regex split value using \s    :",value)

value =re.split(r"\s+",sentense)
print("Regex split value using \s", value)

value=re.split(r'[a-f]',sentense)
print('Regex split using [a-f]:    ',value)