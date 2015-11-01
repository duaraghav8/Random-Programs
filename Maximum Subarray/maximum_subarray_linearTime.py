#Kadane's Algorithm Complexity O(n)

array = [int (i) for i in input ().split ()];
max_so_far = 0;
msf_pos = 0;
max_ending_here = 0;
meh_pos = 0;
start = 0;
fixStart = False;

for i in range (0, len (array)):
	max_ending_here += array [i];
	meh_pos = i;
	if ( (not fixStart) and (max_ending_here > 0) ):
		start = i;
		fixStart = True;

	if (max_ending_here < 0):
		max_ending_here = 0;
		meh_pos = 0;
		start = 0;
		fixStart = False;

	elif (max_ending_here > max_so_far):
		max_so_far = max_ending_here;
		msf_pos = i;

print (max_so_far, start, msf_pos);


