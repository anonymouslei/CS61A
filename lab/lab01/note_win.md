### Error Messsages
SynataxError: contained improper syntax(e.g. missing a colon after an if statement or forgetting to close parentheses/quotes)

IndentationError: contained improper indentation

TypeError: Attempted operation on incompatible types(e.g. trying to add a funciton with the wrong number of arguments


### 04Higher-order function
def make_adder(n):
	"""Return a function that takes one argument k and returns k + next
	
	>>> add_three = make_adder(3)
	>>> add_three(4)
	7
	"""
	# A def statement within another def statement
	def adder(k):
		return k+n
	return adder

in this section, I am interested in functions as arguments. I know little about that and hardly use it.
