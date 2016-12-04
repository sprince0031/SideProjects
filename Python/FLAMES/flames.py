print "Program to find out your 'FLAMES' relationship ;)\n"

namelist1 = list();
namelist2 = list();
len1, len2 = [], [];

def reset(namelistx, namelisty):
	len1, len2 = [], [];
	for name in namelistx:
		len1.append(len(name));
	for name in namelisty:
		len2.append(len(name));
	return len1, len2;

name1 = raw_input("Enter your full name: ").upper()
name2 = raw_input("Enter your crush's full name: ").upper()
namelist1 = name1.split();
namelist2 = name2.split();

#Part where all the common alphabets are cancelled.
print "\nStep 1: Cancelling all common letters..."
def cancel():
	len1, len2 = reset(namelist1, namelist2);	
	x, i = 0, 0;
	while x < len(namelist1) :
		y = 0;
		while y < len1[i] :
			a, j = 0, 0;
			while a < len(namelist2) :
				b = 0;
				while b < len2[j] :
					try:
						if namelist1[x][y] == namelist2[a][b] :
							if y == 0 and b != 0 :
								namelist1[x] = namelist1[x][1:];
								namelist2[a] = namelist2[a][:b] + namelist2[a][b+1:];
							if y != 0 and b == 0 :
								namelist1[x] = namelist1[x][:y] + namelist1[x][y+1:];
								namelist2[a] = namelist2[a][1:];
							if y == 0 and b == 0 :
								namelist1[x] = namelist1[x][1:];
								namelist2[a] = namelist2[a][1:];
							if y != 0 and b != 0 :
								namelist1[x] = namelist1[x][:y] + namelist1[x][y+1:];
								namelist2[a] = namelist2[a][:b] + namelist2[a][b+1:];
							print namelist1
							print namelist2
							cancel() #No support for labels in python unlike in C or C++. Hence a recursive function is used here.
					except:
						break;
					b=b+1
				a=a+1
				j=j+1
			y=y+1
		x=x+1
		i=i+1
cancel()

finalName1, finalName2 = "","";
totLen1, totLen2 = 0, 0;
for word in namelist1:
	finalName1 += word
for word in namelist2:
	finalName2 += word
finalName = finalName1 + finalName2
totLen = len(finalName)

#Part where the flame is determined.
if totLen > 0:
	print "\nThe remaining string is " + finalName + " and it's length is",str(totLen) + '.'
	print "\nStep 2: Cancelling letters in 'FLAMES'..."
	def Flames(totLenx):
		flames = "FLAMES"
		x = 6
		while len(flames) > 1:
			if totLenx % x == 0:
				pos = x-1
				if pos == 0:
					flames = flames[1:]
					print flames
				if pos != 0:
					flames = flames[pos+1:] + flames[:pos]
					print flames 
			else:
				pos = (totLenx % x)-1
				if pos == 0:
					flames = flames[1:]
					print flames
				if pos != 0:
					flames = flames[pos+1:] + flames[:pos]
					print flames 
			x-=1
		return flames

	if totLen > 6:	
		finalFlames = Flames(totLen)

	else:
		if totLen == 6:
			print "FLAME"
			print "LAME"
			print "MEL"
			print "ME"
			print "M"
			finalFlames = 'M'
		elif totLen == 5:
			print "SFLAM"
			print "SFLA"
			print "FLA"
			print "AF"
			print "F"
			finalFlames = 'F'
		elif totLen == 4:
			print "ESFLA"
			print "ESFA"
			print "AES"
			print "ES"
			print "E"
			finalFlames = 'E'
		elif totLen == 3:
			print "MESFL"
			print "FLME"
			print "EFL"
			print "EF"
			print "F"
			finalFlames = 'F'
		elif totLen == 2:
			print "AMESF"
			print "ESFA"
			print "FAE"
			print "EF"
			print "E"
			finalFlames = 'E'
		elif totLen == 1:
			print "LAMES"
			print "AMES"
			print "MES"
			print "ES"
			print "S"
			finalFlames = 'S'
else:
	print "\nEither you're head over heels in love with yourself or both your names are anagrams of each other... :-O"

#Final result
try:
	if finalFlames == 'F':
		print "Awesome! The FLAMES calculator predicts that you two will be best friends :D"
	elif finalFlames == 'L':
		print "Congratulations! The FLAMES calculator predicts you two will fall in love <3"
	elif finalFlames == 'A':
		print "Awww... The FLAMES calculator predicts you two will have mutual affection towards each other :)"
	elif finalFlames == 'M':
		print "*Here comes the bride... All dressed in white...* The FLAMES calculator wishes you two a happy married life!!! O*"
	elif finalFlames == 'E':
		print "Oops! Sorry, but the FLAMES calculator predicts you two will be enemies! :("
	else:
		print "Tough luck... looks like someone is getting bro-zoned :P"
except:
	pass;

print "\nProgram by sprince0031"
print "***END OF PROGRAM***"
