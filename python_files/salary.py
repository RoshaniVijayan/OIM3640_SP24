# Salary Calculator

weekly_hours = 40
hourly_wage = 24
weeks_per_year = 50

weekly_pay = weekly_hours * hourly_wage
yearly_pay = weeks_per_year * weekly_pay 
monthly_pay = yearly_pay / 12

print("Your weekly pay:", weekly_pay)
print("Your monthly pay:", monthly_pay)
print("Your annual pay:", yearly_pay)
