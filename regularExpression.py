import re 

regex = r'\w.\@\w.\.\w'

pattern = 'eduardo@email.net'

a=re.findall(regex,pattern)
print(a)
