import datetime

inputFormat = '%m/%d' #Input format
linkFormat = '%b_%d' #Wikipedia format

link = 'https://en.wikipedia.org/wiki/{}' #output link

while True:
	userInput = input("What date would you like a wikipedia link for? Use the MM/DD format. Enter 'quit' to exit.\n:")
	if userInput.upper() == 'QUIT':
		break
	
	try:
		date = datetime.datetime.strptime(userInput, inputFormat)
		output = link.format(date.strftime(linkFormat))
		print(output)
	#If valid date was not given	
	except ValueError:
		print("Input was not a valid date. Please try again (MM/DD format).")