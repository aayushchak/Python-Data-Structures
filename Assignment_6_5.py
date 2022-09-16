'''Write a code using find() and string slicing to extract the number at the end of the line below.
Convert the extracted value to floating point number and print out.
line: X-DSPAM-Confidence:0.8475'''

text = 'X-DSPAM-Confidence:0.8475'
pos = text.find(':')
x = text[pos+1:]
value = float(x)
print(value)
