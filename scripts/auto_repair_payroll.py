

base_hours = 40
ot_multiplier = 1.5

hours = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly pay rate: "))

# calculate and display the gross pay
if hours > base_hours:
    overtime_hours = hours - base_hours
    overtime_pay = overtime_hours * pay_rate * ot_multiplier

    gross_pay = base_hours * pay_rate + overtime_pay
else:
    gross_pay = hours * pay_rate

print('The gross pay is $', format(gross_pay, ',.2f'), sep='')
