formatter = "%r, %r, %r, %r"
# Uses same format as described in above variable
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.", 
	"But it didn't sing.", # Because of the apostrophe in 'didn't', prints double quotes
	"So I said goodnight.")	