# ex16.py
# reading and writing files

from sys import argv
script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")

input("?")

print("opening the file...")
target = open(filename, 'w+')

# 'w+' doesn't appear to work as described in the book. 'r+' allows read and APPEND, but 'w+' does not appear to work with print read
#print("printing current contents")
#print(target.read())

# not necessary because 'write' mode is being used, not 'append'
#print("truncating the file. goodbye!")
#target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("i'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# study drill 3, do all above in one line
target.write(f"{line1}\n{line2}\n{line3}\n")

print("and finally, we close it.")
target.close()
