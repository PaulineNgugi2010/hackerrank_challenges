def char(a):
	length_of_string = len(a)
	if length_of_string <= 1 and length_of_string <= 10 ** 5:
		return "Enter a Valid String"
	else:
		for i in a:
			y= len(a)
		return y




print char("Pauline")


class StringSplosion(object):
    '''
    This is a class that does spring explosion
        i.e
        phone  => pphphophonphone
        ab     => aab
        like   => lliliklike

    '''

    def __init__(self , string):
        self.string = string

    def manipulate(self):
        output = ''
        for i in range(len(self.string)+1):
            output += self.string[:i]
        return output
print StringSplosion.manipulate("Grace")