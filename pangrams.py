def check(a):
	alphabet = set(('a', 'b', 'c', 'd', 'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n',
'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'))
	#a= set(list(a))
	a = raw_input()
	a= a.lower()
	a= a.replace(' ', '')

	a= set(a)
         
	if len(a)>=1 and len(a) <= 10**3:
		if alphabet.issubset(a):
			return "pangram"
		return "not pangram"
	return "enter a string less than 10^3"


print check("me h")
print  check('Wepromptly,judged antique ivory buckles for the prize')
print check("We promptly judged antique ivory buckles for the next prize")


