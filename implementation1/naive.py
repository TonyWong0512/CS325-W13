sample=open('sample','r')
sample = sample.read()
lines = sample.split('\n')
for line in lines:
	elements = line.split(',')
	count = 0
	for i in range(len(elements)):
		for j in range(i+1,len(elements)):
			if i < j and elements[i] > elements[j]:
				count+=1
	print (count,len(elements))
