Myfile = open("two_cities_ascii.txt", "r")

#Φτιαχνω ενα string για να βαλω μεσα τους σωστους χαρακτηρες
alpha = ''

lhsta=('abcdefghijklmnopqrstuwyz \nABCDEFGHIJKLMNOPRSTUWYZ')

#Καθε χαρακτηρας της lhsta μπαινει σε μια λιστα
lmao = lhsta.replace('',' ').strip().split(' ')

for line in Myfile:
	for word in line.split():
		for character in word:
				for letter in lmao:
					if (character==letter):
						alpha += character
		alpha = alpha + ' '

#Οριστε το κείμενο με μόνο γράμματα και τον κενό χαρακτήρα (space)
print(alpha)
k = list((alpha.split(' ')))
k.pop()
nol=[]
i=0	
for word in k:
	nol.append(len(word))
for numb in nol:
	if (i>0):
		if (nol[i-1]+nol[i]==20):
			b= nol.pop(i)
			b= nol.pop(i-1)
	i+=1
for j in range(min(nol)+1,max(nol)+1):
	print("Οι λεξεις με ",j," γραμματα ειναι: ",nol.count(j))
Myfile.close()