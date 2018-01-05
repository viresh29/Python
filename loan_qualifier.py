
#This program determins weather a bank customer
#qualifies for a loan

min_salary = 30000 #minimum annual salary
min_years = 2      #minimum years on the job

# Get the customer's annual salary
salary = float(input("Enter your annual salary: "))

# Get the number of years on the current job.
years_on_job = int(input("Enter the number of years employed: "))

# determine weather the customer qualifies.
if salary >= min_salary:
    if years_on_job >= min_years:
        print("You qualify for loan.")
    else:
        print("You must have been employewd for at least", min_years, 'years to qualify.')
else:
    print("You must earn at least $", min_salary , ' per year to qualify.',sep='')
