basic_salary = int(input("Enter your basic salary: "))

if basic_salary > 25000:

   hra = 35 * basic_salary

   da = 95 * basic_salary

elif basic_salary > 15000:

   hra = 0.2 * basic_salary

   da = 0.3 * basic_salary

else:

   hra = 0.4 * basic_salary

   da = 0.6 * basic_salary

gross_salary = basic_salary + hra + da

print(f"The gross salary is {gross_salary}.")