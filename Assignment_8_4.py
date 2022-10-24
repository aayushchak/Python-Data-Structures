'''Open the file romeo.txt & read it line by line.
For each line split the line into a list of words using split() method.
The program should build a list of words.
For each word on each line check to see if he word is already in the list & if not append it to the list.
When the program completes, sort & print the resulting words in python sort() order.
FILE: romeo.txt
WEB LINK: http://www.py4e.com/code3/romeo.txt'''

name = input('Enter the file name: ')
file = open(name)
count = 0
word = []
line_list = []
word_list = []
for line in file:
  line = line.rstrip()
  line_list.append(line)
  word = line_list[count].split()
  for i in word:
    if i not in word_list:
      word_list.append(i)
  count += 1

word_list.sort()
print(word_list)
