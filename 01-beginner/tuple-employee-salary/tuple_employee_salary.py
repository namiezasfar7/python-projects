salary_list = []

for i in range(3):
	name = input('Input Name ')
	salary = float(input('Input Salary '))
	
	salary_list.append((name,salary))
	
max_name = ''
max_salary = 0

for emp in salary_list:
	emp_name = emp[0]
	emp_salary = emp[1]
	print('Employee : ',emp_name,'Salary : ',emp_salary)
	
	if emp_salary > max_salary:
		max_salary = emp_salary
		max_name = emp_name


print(salary_list)
print('Highest Salary is ',max_salary,max_name)
