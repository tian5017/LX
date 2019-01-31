import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

aa = re.compile(r'(\d+)/(\d+)/(\d+)')
bb = aa.sub(r'\3-\1-\2', text)
print(bb)
