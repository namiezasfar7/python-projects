marks = []

total = 0
for i in range(5):
	mark = int(input('Input Mark '))
	marks.append(mark)
	total = total + marks[i]

average = total/len(marks)

print('Marks is ',marks)
print('Total is ',total)
print('Average is ',average)