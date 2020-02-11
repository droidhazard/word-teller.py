print("Think of a word or name in your mind which contains 5 letters")
print("Keeping that word in your mind answer the following question by looking at the chart.")

print("""
	1	2	3	4	5
	__________________
1	A	B	C	D	E
2	F	G	H	I	J
3	K	L	M	N	O
4	P	Q	R	S	T
5	U	V	W	X	Y
6	Z""")

one = input("Which line contains the first letter of your word ? enter line number >>> ")
two = input("Which line contains the second letter of your word ? enter line number >>> ")
three = input("Which line contains the third letter of your word ? enter line number >>> ")
four = input("Which line contains the fourth letter of your word ? enter line number >>> ")
five = input("Which line contains the fifth letter of your word ? enter line number >>> ")

print("Keeping that same word in your mind now answer the same questions from this chart. ")

print("""
	1	2	3	4	5	6
	_____________________
	A	F	K	P	U	Z
	B	G	L	Q	V
	C	H	M	R	W
	D	I	N	S	X
	E	J	O	T	Y) """)

one_b = input("Which line contains the first letter of your word ? enter line number >>> ")
two_b = input("Which line contains the second letter of your word ? enter line number >>> ")
three_b = input("Which line contains the third letter of your word ? enter line number >>> ")
four_b = input("Which line contains the fourth letter of your word ? enter line number >>> ")
five_b = input("Which line contains the fifth letter of your word ? enter line number >>> ")

a = str([one, one_b])
b = str([two, two_b])
c = str([three, three_b])
d = str([four, four_b])
e = str([five, five_b])

# print(a, b, c, d, e)
# (5, 1) (5, 2) (5, 3) (5, 4) (5, 5)


#print(a)
#print(type(a))

# a, first line

if a=="['1', '1']":
	a = "A"
elif a=="['1', '2']":
	a = "F"
elif a=="['1', '3']":
	a = "K"
elif a=="['1', '4']":
	a = "P"
elif a=="['1', '5']":
	a = "U"
elif a=="['1', '6']":
	a = "Z"
# a, second line

if a=="['2', '1']":
	a = "B"
elif a=="['2', '2']":
	a = "G"
elif a=="['2', '3']":
	a = "L"
elif a=="['2', '4']":
	a = "Q"
elif a=="['2', '5']":
	a = "V"

# a, third line

if a=="['3', '1']":
	a = "C"
elif a=="['3', '2']":
	a = "H"
elif a=="['3', '3']":
	a = "M"
elif a=="['3', '4']":
	a = "R"
elif a=="['3', '5']":
	a = "W"

# a, FOURTH line

if a=="['4', '1']":
	a = "D"
elif a=="['4', '2']":
	a = "I"
elif a=="['4', '3']":
	a = "N"
elif a=="['4', '4']":
	a = "S"
elif a=="['4', '5']":
	a = "X"

# a, FIVE line

if a=="['5', '1']":
	a = "E"
elif a=="['5', '2']":
	a = "J"
elif a=="['5', '3']":
	a = "O"
elif a=="['5', '4']":
	a = "T"
elif a=="['5', '5']":
	a = "Y"

# b, first line

if b=="['1', '1']":
	b = "A"
elif b=="['1', '2']":
	b = "F"
elif b=="['1', '3']":
	b = "K"
elif b=="['1', '4']":
	b = "P"
elif b=="['1', '5']":
	b = "U"
elif b=="['1', '6']":
	b = "Z"
# b, second line

if b=="['2', '1']":
	b = "B"
elif b=="['2', '2']":
	b = "G"
elif b=="['2', '3']":
	b = "L"
elif b=="['2', '4']":
	b = "Q"
elif b=="['2', '5']":
	b = "V"

# b, third line

if b=="['3', '1']":
	b = "C"
elif b=="['3', '2']":
	b = "H"
elif b=="['3', '3']":
	b = "M"
elif b=="['3', '4']":
	b = "R"
elif b=="['3', '5']":
	b = "W"

# b, FOURTH line

if b=="['4', '1']":
	b = "D"
elif b=="['4', '2']":
	b = "I"
elif b=="['4', '3']":
	b = "N"
elif b=="['4', '4']":
	b = "S"
elif b=="['4', '5']":
	b = "X"

# b, FIVE line

if b=="['5', '1']":
	b = "E"
elif b=="['5', '2']":
	b = "J"
elif b=="['5', '3']":
	b = "O"
elif b=="['5', '4']":
	b = "T"
elif b=="['5', '5']":
	b = "Y"

c# c, first line

if c=="['1', '1']":
	c = "A"
elif c=="['1', '2']":
	c = "F"
elif c=="['1', '3']":
	c = "K"
elif c=="['1', '4']":
	c = "P"
elif c=="['1', '5']":
	c = "U"
elif c=="['1', '6']":
	c = "Z"
# c, second line

if c=="['2', '1']":
	c = "B"
elif c=="['2', '2']":
	c = "G"
elif c=="['2', '3']":
	c = "L"
elif c=="['2', '4']":
	c = "Q"
elif c=="['2', '5']":
	c = "V"

# c, third line

if c=="['3', '1']":
	c = "C"
elif c=="['3', '2']":
	c = "H"
elif c=="['3', '3']":
	c = "M"
elif c=="['3', '4']":
	c = "R"
elif c=="['3', '5']":
	c = "W"

# c, FOURTH line

if c=="['4', '1']":
	c = "D"
elif c=="['4', '2']":
	c = "I"
elif c=="['4', '3']":
	c = "N"
elif c=="['4', '4']":
	c = "S"
elif c=="['4', '5']":
	c = "X"

# c, FIVE line

if c=="['5', '1']":
	c = "E"
elif c=="['5', '2']":
	c = "J"
elif c=="['5', '3']":
	c = "O"
elif c=="['5', '4']":
	c = "T"
elif c=="['5', '5']":
	c = "Y"

# d, first line

if d=="['1', '1']":
	d = "A"
elif d=="['1', '2']":
	d = "F"
elif d=="['1', '3']":
	d = "K"
elif d=="['1', '4']":
	d = "P"
elif d=="['1', '5']":
	d = "U"
elif d=="['1', '6']":
	d = "Z"
# d, sedond line

if d=="['2', '1']":
	d = "B"
elif d=="['2', '2']":
	d = "G"
elif d=="['2', '3']":
	d = "L"
elif d=="['2', '4']":
	d = "Q"
elif d=="['2', '5']":
	d = "V"

# d, third line

if d=="['3', '1']":
	d = "C"
elif d=="['3', '2']":
	d = "H"
elif d=="['3', '3']":
	d = "M"
elif d=="['3', '4']":
	d = "R"
elif d=="['3', '5']":
	d = "W"

# d, FOURTH line

if d=="['4', '1']":
	d = "D"
elif d=="['4', '2']":
	d = "I"
elif d=="['4', '3']":
	d = "N"
elif d=="['4', '4']":
	d = "S"
elif d=="['4', '5']":
	d = "X"

# d, FIVE line

if d=="['5', '1']":
	d = "E"
elif d=="['5', '2']":
	d = "J"
elif d=="['5', '3']":
	d = "O"
elif d=="['5', '4']":
	d = "T"
elif d=="['5', '5']":
	d = "Y"

# e, first line

if e=="['1', '1']":
	e = "A"
elif e=="['1', '2']":
	e = "F"
elif e=="['1', '3']":
	e = "K"
elif e=="['1', '4']":
	e = "P"
elif e=="['1', '5']":
	e = "U"
elif e=="['1', '6']":
	e = "Z"
# e, seeone line

if e=="['2', '1']":
	e = "B"
elif e=="['2', '2']":
	e = "G"
elif e=="['2', '3']":
	e = "L"
elif e=="['2', '4']":
	e = "Q"
elif e=="['2', '5']":
	e = "V"

# e, thire line

if e=="['3', '1']":
	e = "C"
elif e=="['3', '2']":
	e = "H"
elif e=="['3', '3']":
	e = "M"
elif e=="['3', '4']":
	e = "R"
elif e=="['3', '5']":
	e = "W"

# e, FOURTH line

if e=="['4', '1']":
	e = "D"
elif e=="['4', '2']":
	e = "I"
elif e=="['4', '3']":
	e = "N"
elif e=="['4', '4']":
	e = "S"
elif e=="['4', '5']":
	e = "X"

# e, FIVE line

if e=="['5', '1']":
	e = "E"
elif e=="['5', '2']":
	e = "J"
elif e=="['5', '3']":
	e = "O"
elif e=="['5', '4']":
	e = "T"
elif e=="['5', '5']":
	e = "Y"

print("Was the word you thought ", a, b, c, d, e, " ?")