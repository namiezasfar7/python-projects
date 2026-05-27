students = {}

num_of_students = int(input('Input Number of Students '))

total = 0

for i in range(num_of_students):
	name = input('Input Name ')
	mark = int(input('Input Marks '))
	
	total = total + mark
	
	students[name] = mark

average = total / num_of_students

highest_name = ''
highest_marks = 0

for name, marks in students.items():
	if marks > highest_marks:
		highest_marks = marks
		highest_name = name

print(students)
print('Average Mark of Class :', average)
print('Highest Mark is', highest_marks, 'by', highest_name)	