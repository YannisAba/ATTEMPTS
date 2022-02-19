#Συναρτησεις
def listToString(s):
	str1 = ""
	for i in s: 
        	str1 += i
	return str1 

def StringToBinary(s):
	return [bin(ord(x))[2:].zfill(7) for x in s]


#main
with open('ascii.txt','r') as file:
	lol = file.read()
lmao = lol.replace('  ',' ').strip().split(' ')
imagine = ""
list=[]
for word in lmao:
	for letter in word:
		b = StringToBinary(letter)
		list.append(listToString(b))
	list.append("0100000")
list.pop()

list2=[]
for letter in list:
	list2.append(letter[:-5])
	list2.append(letter[5:])

str= (listToString(list2))
import textwrap
k=[]
k= textwrap.wrap(str, 16)
for i in range(0, len(k)):
	k[i] = int(k[i])
all=0
zygoi=0
dia3=0
dia5=0
dia7=0
for i in range(0, len(k)):
	if(k[i]%2==0):
		zygoi+=1
	if(k[i]//3==k[i]/3):
		dia3+=1
	if(k[i]//5==k[i]/5):
		dia5+=1
	if(k[i]//7==k[i]/7):
		dia7+=1
	all+=1
print("Το ποσοστο των ζυγων αριθμων ειναι: ",zygoi/all*100,"%")
print("Το ποσοστο των αριθμων που διαιρουνται ακριβως με το 3 ειναι: ",dia3/all*100,"%")
print("Το ποσοστο των αριθμων που διαιρουνται ακριβως με το 5 ειναι: ",dia5/all*100,"%")
print("Το ποσοστο των αριθμων που διαιρουνται ακριβως με το 7 ειναι: ",dia7/all*100,"%")