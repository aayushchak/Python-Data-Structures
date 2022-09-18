'''Write a program that prompts for a file name, then open the file & reads through the file.
Print the content of the file in upper case.
File: words.txt
Web link of file: http://www.py4e.com/code3/words.txt'''

fname = input('Enter the file name: ')
x = open(fname)
for line in x:
  line = line.rstrip()
  line_cap = line.upper()
  print(line_cap)
  
  #can print in caps directly using
  #print(line.upper())
