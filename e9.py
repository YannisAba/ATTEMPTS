def listToString(s):
	str1 = ""
	for i in s: 
        	str1 += i
	return str1 


def StringToBinary(s):
	return [bin(ord(x))[2:].zfill(7) for x in s]


with open('ascii.txt','r') as file:
	lol = file.read()
lmao = lol.replace('  ',' ').strip().split(' ')
imagine = ""
list=[]
i = 1
for x in lmao:
	b = StringToBinary(x)
	list.append(b)
	if (len(lmao) == i):
		break
	i = i+1
	imagine = imagine + (listToString(b)) + "0100000"
imagine = imagine[:-7]

count1 = -1
count2 = -1
maximum1 = -1
maximum2 = -1
counter1 = 0
counter2 = 0
for num in imagine:
	count1 +=1
	count2 +=1
	if num== '1':
        	counter1 += 1
	else:
		maximum1=max(maximum1, counter1)
		counter1 = 0
	if num== '0':
		counter2 += 1
	else:
		maximum2=max(maximum2, counter2)
		counter2 = 0
print ("Η μεγαλυτερη ακολουθία από 1 είναι:",maximum1)
print ("Η μεγαλυτερη ακολουθία από 0 είναι:",maximum2)
file.close()