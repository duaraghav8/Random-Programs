############################################################################################
#Number to Digital (Calculator Font)
############################################################################################

digits = {
	'0' : '\n --\n|  |\n|  |\n --',
	'1' : '\n\n\n|\n|',
	'2' : '--\n  |\n--\n|\n --',
	'3' : '--\n  |\n--\n  |\n--',
	'4' : '\n\n|  |\n --\n   |',
	'5' : ' --\n|\n --\n   |\n --',
	'6' : '\n\n|\n|__\n|__|',
	'7' : '\n\n--\n  |\n  |',
	'8' : ' --\n|  |\n --\n|  |\n --',
	'9' : ' --\n|  |\n --\n   |\n --'
};

def digital (number):
	space = [ '' for i in range (5) ];
	for count in range (5):
		for digit in number:
			adder = digits [digit].split ('\n') [count];
			if (len (adder) < 5): adder += ' ' * (5 - len (adder));
			space [count] += adder;
	return (space);

number = input ();
space = digital (number);
for line in space: print (line);
