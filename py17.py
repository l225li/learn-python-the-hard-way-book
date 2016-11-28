from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print "Does the output file exists? %r" % exists(to_file)

out_file = open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()