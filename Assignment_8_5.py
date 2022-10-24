'''Open the file mbox-short.txt & read it line by line.
When you find a line that starts with From like the following line:
  From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line using split() & print out the second word in the line (entire address).
Then print out a count and end.
FILE: mbox-short.txt
WEB LINK: http://www.py4e.com/code3/mbox-short.txt'''

name = input('Enter the file name: ')
file = open(name)
word = []
count = 0
for line in file:
  line = line.rstrip()
  if line.startswith('From'):
    count += 1
    word = line.split()
    print(word[1])
    
print('There were',count,'lines in the file with From as the first word')
