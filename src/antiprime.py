## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	i=1
	nd1=0
	y=x - 1
	nd2=0
	while(i <= x):
		if (x%i == 0):
			nd1=nd1 + 1
		i=i + 1
	while(y >= 1):
		i=1
		while(i<=y):
			if (y%i == 0):
				nd2 = nd2 +1
			i=i + 1
		if (nd2 >= nd1):
			res = 'not anti-prime'
			return('not anti-prime')
			y=0
		else:
			y=y - 1
			nd2=0

	if (nd2<nd1):
		res = 'anti-prime'

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
		return("anti-prime")

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys
	if len(sys.argv) > 1:
		x = int(sys.argv[1])
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))
