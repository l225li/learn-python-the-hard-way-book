
def numbers_less_than (number,skip):
	i = 0
	numbers = []
	while i < number:
		print "At the top i is %d" %i
		numbers.append(i)

		i += skip
		print "Number now: ", numbers
		print "At the bottom i is %d"%i

	print "The numbers:"

	for num in numbers:
		print num

numbers_less_than(30,4)