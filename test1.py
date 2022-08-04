#soal nomor 1
def cek(list):
	ab = ["A","B","C","D","E","F","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	new_ab=[]
	new_alp=[]
	for i in list:
		if i in ab:
			new_ab.append(i)
		else:
			new_alp.append(i)
	for a in range(0,len(new_ab)-1):
		if new_ab[a] > new_ab[a+1]:
			new_ab[a],new_ab[a+1] = new_ab[a+1],new_ab[a]
	for b in range(0,len(new_alp)-1):
		if new_alp[b] > new_alp[b+1]:
			new_alp[b],new_alp[b+1] = new_alp[b+1],new_alp[b]
	return new_ab+new_alp


x = ["A","B",1,4,5,"E","C"]
print(cek(x))

#soal nomor 2
def pattern_count(x,y):
	z= 0
	y= 0
	lol = 0
	count=0
	while lol < len(x):
		if set in x[z:len(set)+y]:
			count+=1
			print(x[z:len(set)+y],"ok",count)
		else:
			print(x[z:len(set)+y],"no")
		lol+=1
		z+=1
		y+=1
	print(f"total match pattern:{count}")

x = "palindrome"
set ="ind"

pattern_count(x,set)

#soal nomor 3
def find_freq(text):
	text = text.replace(" ","")
	frekuensi = {}
	for abc in text:
		if abc in frekuensi:
			frekuensi[abc]+=1
		else:
			frekuensi[abc]=1
	return frekuensi

text= "Hello world"
print(find_freq(text))


