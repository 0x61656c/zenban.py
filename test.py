data = {
	"a" : 1,
	"b" : 2,
	"c" : 3
}

def newEvent(data, input):
    """
    Var input must be a tuple of category and event text
        Example: ("Personal", "Get a job")
    """
    print(data[input[0]])

print(newEvent(data, ("a", "Get a job")))