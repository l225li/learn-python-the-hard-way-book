#import the module
from sys import argv

#read from the arguments filename wanted to read by user
script, filename = argv

#use the given filename to open a file object
txt = open(filename)

#print the file name
print "Here's your file %r:" % filename
#read the file object and print it to user
print txt.read(20)
print txt.readline()
print txt.readline(10)
txt.close()

# #prompting user for filename again 
# print "Type the filename again:"
# file_again = raw_input("> ")
# #open the new filename given
# txt_again = open(file_again)
# #read and print the filename
# print txt_again.read()
# txt_again.close()