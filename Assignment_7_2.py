'''Write a program that prompts for a file nam, then opens the file & reads through the file looking
for lines of the form:
X-DSPAM-Confidence:  0.8475
Count these lines & extract the floating point values from each of the lines &
compute the average of those values & produce an output.
FILE: mbox-short.txt
WEB LINK: http://www.py4e.com/code3/mbox-short.txt'''

fname = input('Enter the file name: ')
x = open(fname)
avg = 0.0
count = 1
tot = 0.0
for line in x:
  line = line.rstrip()
  if line.startswith('X-DSPAM-Confidence:'):
    count += 1
    col_pos = line.find(':')
    val = line[col_pos+1:]
    val = val.strip()
    float_val = float(val)
    tot += float_val

avg = tot/count
print('Average spam confidence:',avg)
